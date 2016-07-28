import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class AbstractCoprConglomerator(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return '.copr.' in msg['topic']

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        agents = set([m['msg']['user'] for m in ms if m['msg']['user']])
        coprs = set([m['msg']['copr'] for m in ms])
        count = len([1 for m in ms
                      if m['topic'].endswith('copr.build.start')])

        if count > 0:
            subtitle = '{agents} kicked off {count} {rebuild_predicate} ' + \
                'of the {coprs} {copr_predicate}'
        else:
            # If count is zero, then there are zero start messages in the
            # constituents list, so change tack and render "finishes" instead
            # of "starts".
            count = len(ms)
            subtitle = 'The {coprs} {copr_predicate} finished ' + \
                '{count} {rebuild_predicate} by {agents}'

        rebuild_predicate = 'rebuilds' if count > 1 else 'rebuild'
        copr_predicate = 'coprs' if len(coprs) > 1 else 'copr'

        agents = self.list_to_series(agents)
        coprs = self.list_to_series(coprs)

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            agents=agents, count=count, coprs=coprs,
            copr_predicate=copr_predicate, rebuild_predicate=rebuild_predicate)
        tmpl['subjective'] = tmpl['subtitle']

        default = tmpl['icon']

        tmpl['secondary_icon'] = self.get_secondary_icon(constituents, default)
        tmpl['link'] = self.get_link(constituents)

        return tmpl


class ByCopr(AbstractCoprConglomerator):
    def matches(self, a, b, **config):
        a, b = a['msg'], b['msg']
        if a['copr'] != b['copr']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        agents = set([m['msg']['user'] for m in constituents])
        if len(agents) == 1:
            user = constituents[0]['msg']['user']
            return avatar_url(user)
        else:
            return 'https://apps.fedoraproject.org/img/icons/copr.png'

    def get_link(self, constituents):
        owner = constituents[0]['msg']['owner']
        copr = constituents[0]['msg']['copr']
        return 'https://copr.fedoraproject.org/coprs/%s/%s/' % (owner, copr)


class ByUser(AbstractCoprConglomerator):
    def matches(self, a, b, **config):
        a, b = a['msg'], b['msg']
        if a['user'] != b['user']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        user = constituents[0]['msg']['user']
        return avatar_url(user)

    def get_link(self, constituents):
        user = constituents[0]['msg']['user']
        return 'https://copr.fedoraproject.org/coprs/' + user
