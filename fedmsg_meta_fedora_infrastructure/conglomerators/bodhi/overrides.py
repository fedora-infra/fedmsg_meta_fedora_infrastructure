import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class ByUserTag(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return any([
            'bodhi.buildroot_override.tag' in msg['topic'],
        ])

    def matches(self, a, b, **config):
        """ The message must match by username """
        submitter_a = a['msg']['override']['submitter']['name']
        submitter_b = b['msg']['override']['submitter']['name']
        if submitter_a != submitter_b:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['override']['submitter']['name']
        branches = self.list_to_series([
            constituent['msg']['override']['nvr'].split('.')[-1]
            for constituent in constituents])

        tmpl = self.produce_template(constituents, subject, **config)
        packages = self.list_to_series(list(tmpl['packages']))
        subtitle = '{agent} submitted {N} overrides for {packages} ' + \
            'on {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, packages=packages, N=N, branches=branches)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = avatar_url(agent)
        base = 'https://bodhi.fedoraproject.org/overrides/?user=%s'
        tmpl['link'] = base % agent
        return tmpl


class ByUserUnTag(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return any([
            'bodhi.buildroot_override.untag' in msg['topic'],
        ])

    def matches(self, a, b, **config):
        """ The message must match by username """
        submitter_a = a['msg']['override']['submitter']['name']
        submitter_b = b['msg']['override']['submitter']['name']
        if submitter_a != submitter_b:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['override']['submitter']['name']
        branches = self.list_to_series([
            constituent['msg']['override']['nvr'].split('.')[-1]
            for constituent in constituents])

        tmpl = self.produce_template(constituents, subject, **config)
        packages = self.list_to_series(list(tmpl['packages']))
        subtitle = '{agent} expired {N} overrides for {packages} ' + \
            'on {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, packages=packages, N=N, branches=branches)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = avatar_url(agent)
        base = 'https://bodhi.fedoraproject.org/overrides/?user=%s'
        tmpl['link'] = base % agent
        return tmpl
