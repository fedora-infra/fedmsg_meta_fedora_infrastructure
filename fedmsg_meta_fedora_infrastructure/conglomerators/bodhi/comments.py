import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class ByUpdate(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'bodhi.update.comment' in msg['topic']

    def matches(self, a, b, **config):
        """ The comments must all be on the same bodhi update """
        a, b = a['msg'], b['msg']
        if a['comment']['update_title'] != b['comment']['update_title']:
            return False
        return True

    def merge(self, constituents, subject, **config):
        N = len(constituents)
        msg = constituents[0]['msg']

        tmpl = self.produce_template(constituents, subject, **config)
        agents = self.list_to_series(list(tmpl['usernames']))
        update = msg['comment']['update_title']
        subtitle = '{agents} commented on {update}'
        tmpl['subtitle'] = subtitle.format(agents=agents, update=update)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = tmpl['icon']
        base = 'https://bodhi.fedoraproject.org/updates/%s'
        tmpl['link'] = base % update
        return tmpl


class ByUser(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'bodhi.update.comment' in msg['topic']

    def matches(self, a, b, **config):
        """ The comments must all be by the same user """
        if a['msg']['agent'] != b['msg']['agent']:
            return False
        return True

    def merge(self, constituents, subject, **config):
        tmpl = self.produce_template(constituents, subject, **config)
        msg = constituents[0]
        agent = msg['msg']['agent']
        updates = self.list_to_series([
            msg['msg']['comment']['update_title'] for msg in constituents])
        subtitle = '{agent} commented on {updates}'
        tmpl['subtitle'] = subtitle.format(agent=agent, updates=updates)
        tmpl['subjective'] = tmpl['subtitle']
        tmpl['secondary_icon'] = avatar_url(agent)
        base = 'https://bodhi.fedoraproject.org/users/%s'
        tmpl['link'] = base % agent
        return tmpl
