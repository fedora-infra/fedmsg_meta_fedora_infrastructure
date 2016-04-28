import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class ByURL(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return '.meetbot.' in msg['topic']

    def get_title(self, ms):
        for msg in ms:
            title = msg['msg'].get('meeting_topic')
            if title:
                return title
        return None

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand
        usernames = self.list_to_series(
            sum([list(m['msg']['attendees'].keys()) for m in ms], [])
        )
        channel = ms[0]['msg']['channel']
        title = self.get_title(ms)

        if title:
            subtitle = self._('{usernames} participated in {title} in {channel}')
        else:
            subtitle = self._('{usernames} participated in a meeting in {channel}')

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            usernames=usernames,
            title=title,
            channel=channel,
        )
        tmpl['subjective'] = tmpl['subtitle']

        default = tmpl['icon']

        # These are the only two keys that vary amongst our concrete children.
        tmpl['secondary_icon'] = self.get_secondary_icon(constituents, default)
        tmpl['link'] = self.get_link(constituents)

        return tmpl

    def matches(self, a, b, **config):
        """ The events must be all about the same meetbot """
        a, b = a['msg'], b['msg']
        if a['url'] != b['url']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        username = constituents[0]['msg']['owner']
        return avatar_url(username)

    def get_link(self, constituents):
        return constituents[0]['msg']['url']
