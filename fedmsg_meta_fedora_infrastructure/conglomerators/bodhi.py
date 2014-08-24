import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import gravatar_url


class RequestByUserAndPackageTesting(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'bodhi.update.request.testing' in msg['topic']

    def matches(self, a, b, **config):
        """ The message must match with all three topic, user, and package """
        if a['topic'] != b['topic']:
            return False
        if a['msg']['agent'] != b['msg']['agent']:
            return False
        package_a = self.processor._u2p(a['msg']['update']['title'])[0]
        package_b = self.processor._u2p(b['msg']['update']['title'])[0]
        if package_a != package_b:
            return False
        return True

    def merge(self, constituents, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['agent']
        package = self.processor._u2p(msg['update']['title'])[0]
        branches = self.list_to_series([
            constituent['msg']['update']['release']['name']
            for constituent in constituents])

        tmpl = self.produce_template(constituents, **config)
        subtitle = '{agent} submitted {N} {package} ' + \
            'testing updates for {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, package=package, N=N, branches=branches)
        tmpl['secondary_icon'] = gravatar_url(msg['agent'])
        base = 'https://admin.fedoraproject.org/updates/%s/'
        tmpl['link'] = base % package
        return tmpl


class RequestByUserAndPackageStable(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'bodhi.update.request.stable' in msg['topic']

    def matches(self, a, b, **config):
        """ The message must match with all three topic, user, and package """
        if a['topic'] != b['topic']:
            return False
        if a['msg']['agent'] != b['msg']['agent']:
            return False
        package_a = self.processor._u2p(a['msg']['update']['title'])[0]
        package_b = self.processor._u2p(b['msg']['update']['title'])[0]
        if package_a != package_b:
            return False
        return True

    def merge(self, constituents, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['agent']
        package = self.processor._u2p(msg['update']['title'])[0]
        branches = self.list_to_series([
            constituent['msg']['update']['release']['name']
            for constituent in constituents])

        tmpl = self.produce_template(constituents, **config)
        subtitle = '{agent} requested {N} {package} ' + \
            'stable updates for {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, package=package, N=N, branches=branches)
        tmpl['secondary_icon'] = gravatar_url(msg['agent'])
        base = 'https://admin.fedoraproject.org/updates/%s/'
        tmpl['link'] = base % package
        return tmpl
