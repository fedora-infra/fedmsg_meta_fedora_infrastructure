import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class AbstractPkgdbACLsConglomerator(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'pkgdb.acl.update' in msg['topic']

    def possessive(self, name):
        """ Given a name, return the possessive form. """
        return self._("{name}'s").format(name=name)

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand
        agents = self.list_to_series([m['msg']['agent'] for m in ms])
        usernames = self.list_to_series([
            self.possessive(m['msg']['username']) for m in ms
        ])
        acls = self.list_to_series([m['msg']['acl'] for m in ms])
        packages = self.list_to_series([m['msg']['package_name'] for m in ms])
        statuses = self.list_to_series([m['msg']['status'] for m in ms])
        branches = self.list_to_series([
            m['msg']['package_listing']['collection']['branchname']
            for m in ms])

        subtitle = '{agents} changed {usernames} {acls} permissions on ' + \
            '{packages} ({branches}) to {statuses}.'

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            agents=agents,
            usernames=usernames,
            acls=acls,
            packages=packages,
            branches=branches,
            statuses=statuses,
        )
        tmpl['subjective'] = tmpl['subtitle']

        default = tmpl['icon']

        # These are the only two keys that vary amongst our concrete children.
        tmpl['secondary_icon'] = self.get_secondary_icon(constituents, default)
        tmpl['link'] = self.get_link(constituents)

        return tmpl


class BySubject(AbstractPkgdbACLsConglomerator):
    def matches(self, a, b, **config):
        """ The changes must all be **to** the same pkgdb user """
        a, b = a['msg'], b['msg']
        if a['username'] != b['username']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        username = constituents[0]['msg']['username']
        return avatar_url(username)

    def get_link(self, constituents):
        username = constituents[0]['msg']['username']
        base = 'https://admin.fedoraproject.org/pkgdb/packager/%s/'
        return base % username


class ByAgent(AbstractPkgdbACLsConglomerator):
    def matches(self, a, b, **config):
        """ The changes must all be **by** the same pkgdb user """
        a, b = a['msg'], b['msg']
        if a['agent'] != b['agent']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        username = constituents[0]['msg']['agent']
        return avatar_url(username)

    def get_link(self, constituents):
        username = constituents[0]['msg']['agent']
        base = 'https://admin.fedoraproject.org/pkgdb/packager/%s/'
        return base % username


class ByPackage(AbstractPkgdbACLsConglomerator):
    def matches(self, a, b, **config):
        """ The changes must all be **on** the same package """
        a, b = a['msg'], b['msg']
        if a['package_name'] != b['package_name']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        return default

    def get_link(self, constituents):
        package = constituents[0]['msg']['package_name']
        base = 'https://admin.fedoraproject.org/pkgdb/package/%s/'
        return base % package
