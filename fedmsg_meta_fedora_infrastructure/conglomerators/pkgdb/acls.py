import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import gravatar_url


class BySubject(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'pkgdb.acl.update' in msg['topic']

    def matches(self, a, b, **config):
        """ The comments must all be on the same bodhi update """
        a, b = a['msg'], b['msg']
        if a['username'] != b['username']:
            return False
        return True

    def merge(self, constituents, **config):
        msg = constituents[0]['msg']
        username = msg['username']  # This will be the same amongst all msgs

        ms = constituents  # shorthand
        agents = self.list_to_series([m['msg']['agent'] for m in ms])
        acls = self.list_to_series([m['msg']['acl'] for m in ms])
        packages = self.list_to_series([m['msg']['package_name'] for m in ms])
        statuses = self.list_to_series([m['msg']['status'] for m in ms])
        branches = self.list_to_series([
            m['msg']['package_listing']['collection']['branchname']
            for m in ms])

        subtitle = '{agents} changed {username}\'s {acls} permissions on ' + \
            '{packages} ({branches}) to {statuses}.'

        tmpl = self.produce_template(constituents, **config)
        tmpl['subtitle'] = subtitle.format(
            agents=agents,
            username=username,
            acls=acls,
            packages=packages,
            branches=branches,
            statuses=statuses,
        )

        tmpl['secondary_icon'] = gravatar_url(username)
        base = 'https://admin.fedoraproject.org/pkgdb/packager/%s/'
        tmpl['link'] = base % username
        return tmpl
