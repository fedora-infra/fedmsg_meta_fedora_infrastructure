import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url

class AbstractTaggerConglomerator(fedmsg.meta.base.BaseConglomerator):

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        user = ms[0]['msg']['user']['username']
        tags = set([m['msg']['vote']['tag']['tag'] for m in ms])
        pkgs = set([m['msg']['vote']['tag']['package'] for m in ms])

        tags = self.list_to_series(tags)
        pkgs = self.list_to_series(pkgs)


        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = self.subtitle.format(user=user, tags=tags, pkgs=pkgs)
        tmpl['subjective'] = tmpl['subtitle']

        default = tmpl['icon']

        tmpl['secondary_icon'] = self.get_secondary_icon(constituents, default)
        tmpl['link'] = 'http://infrastructure.fedoraproject.org' + \
            '/infra/ansible.git/'

        return tmpl

    def matches(self, a, b, **config):
        """ The changes must all be **to** the same pkgdb user """
        a, b = a['msg'], b['msg']
        if a['user']['username'] != b['user']['username']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        userid = constituents[0]['msg']['user']['username']
        return avatar_url(userid)

    def get_link(self, constituents):
        return ''


class UpdateByUser(AbstractTaggerConglomerator):
    subtitle = '{user} voted on the tags: {tags} to the packages: {pkgs}'

    def can_handle(self, msg, **config):
        return 'fedoratagger.tag.update' in msg['topic']


class CreateByUser(AbstractTaggerConglomerator):
    subtitle = '{user} created new tags: {tags} on the packages: {pkgs}'

    def can_handle(self, msg, **config):
        return 'fedoratagger.tag.create' in msg['topic']
