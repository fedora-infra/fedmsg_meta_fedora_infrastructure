import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class ByUserAndPackageTesting(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'bodhi.update.request.testing' in msg['topic']

    def matches(self, a, b, **config):
        """ The messages must match with both user and package """
        if a['msg']['agent'] != b['msg']['agent']:
            return False
        package_a = self.processor._u2p(a['msg']['update']['title'])[0]
        package_b = self.processor._u2p(b['msg']['update']['title'])[0]
        if package_a != package_b:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['agent']
        package = self.processor._u2p(msg['update']['title'])[0]
        branches = self.list_to_series([
            constituent['msg']['update']['release']['name']
            for constituent in constituents])

        tmpl = self.produce_template(constituents, subject, **config)
        subtitle = '{agent} submitted {N} {package} ' + \
            'testing updates for {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, package=package, N=N, branches=branches)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = avatar_url(msg['agent'])
        base = 'https://bodhi.fedoraproject.org/updates/%s'
        tmpl['link'] = base % package
        return tmpl


class ByUserAndPackageStable(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'bodhi.update.request.stable' in msg['topic']

    def matches(self, a, b, **config):
        """ The messages must match with both user and package """
        if a['msg']['agent'] != b['msg']['agent']:
            return False
        package_a = self.processor._u2p(a['msg']['update']['title'])[0]
        package_b = self.processor._u2p(b['msg']['update']['title'])[0]
        if package_a != package_b:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['agent']
        package = self.processor._u2p(msg['update']['title'])[0]
        branches = self.list_to_series([
            constituent['msg']['update']['release']['name']
            for constituent in constituents])

        tmpl = self.produce_template(constituents, subject, **config)
        subtitle = '{agent} requested {N} {package} ' + \
            'stable updates for {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, package=package, N=N, branches=branches)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = avatar_url(msg['agent'])
        base = 'https://bodhi.fedoraproject.org/updates/%s'
        tmpl['link'] = base % package
        return tmpl


class ByPackage(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return any([
            'bodhi.update.request.testing' in msg['topic'],
            'bodhi.update.request.stable' in msg['topic'],
        ])

    def matches(self, a, b, **config):
        """ The message must match by package """
        package_a = self.processor._u2p(a['msg']['update']['title'])[0]
        package_b = self.processor._u2p(b['msg']['update']['title'])[0]
        if package_a != package_b:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        package = self.processor._u2p(msg['update']['title'])[0]
        branches = self.list_to_series([
            constituent['msg']['update']['release']['name']
            for constituent in constituents])

        tmpl = self.produce_template(constituents, subject, **config)
        agents = self.list_to_series(list(tmpl['usernames']))
        subtitle = '{agents} submitted {N} {package} ' + \
            'updates for {branches}'
        tmpl['subtitle'] = subtitle.format(
            agents=agents, package=package, N=N, branches=branches)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = tmpl['icon']
        base = 'https://bodhi.fedoraproject.org/updates/%s'
        tmpl['link'] = base % package
        return tmpl


class ByUser(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return any([
            'bodhi.update.request.testing' in msg['topic'],
            'bodhi.update.request.stable' in msg['topic'],
        ])

    def matches(self, a, b, **config):
        """ The message must match by username """
        if a['msg']['agent'] != b['msg']['agent']:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']
        agent = msg['agent']
        branches = self.list_to_series([
            constituent['msg']['update']['release']['name']
            for constituent in constituents])

        tmpl = self.produce_template(constituents, subject, **config)
        packages = self.list_to_series(list(tmpl['packages']))
        subtitle = '{agent} submitted {packages} ' + \
            'updates for {branches}'
        tmpl['subtitle'] = subtitle.format(
            agent=agent, packages=packages, N=N, branches=branches)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = avatar_url(msg['agent'])
        base = 'https://bodhi.fedoraproject.org/users/%s'
        tmpl['link'] = base % agent
        return tmpl
