import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url


class ByUser(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return 'ansible.playbook' in msg['topic']

    def possessive(self, name):
        """ Given a name, return the possessive form. """
        return self._("{name}'s").format(name=name)

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        agent = ms[0]['msg']['userid']
        playbooks = set([m['msg']['playbook'].split('/')[-1] for m in ms])
        playbooks_text = self.list_to_series(playbooks)

        N = len([m for m in ms if m['topic'].endswith('start')])
        if not N:
            N = len(ms)

        playbooks_predicate = 'playbooks' if len(playbooks) > 1 else 'playbook'
        times_predicate = 'times' if N > 1 else 'time'

        subtitle = '{agent} ran the {playbooks} ' + \
            '{playbooks_predicate} {N} {times_predicate}'

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            agent=agent, playbooks=playbooks_text, N=N,
            playbooks_predicate=playbooks_predicate,
            times_predicate=times_predicate)

        subjective_agent = 'You' if agent == subject else agent
        tmpl['subjective'] = subtitle.format(
            agent=subjective_agent, playbooks=playbooks_text, N=N,
            playbooks_predicate=playbooks_predicate,
            times_predicate=times_predicate)

        default = tmpl['icon']

        tmpl['secondary_icon'] = self.get_secondary_icon(constituents, default)
        tmpl['link'] = 'http://infrastructure.fedoraproject.org' + \
            '/infra/ansible.git/'

        return tmpl

    def matches(self, a, b, **config):
        """ The changes must all be **to** the same pkgdb user """
        a, b = a['msg'], b['msg']
        if a['userid'] != b['userid']:
            return False
        return True

    def get_secondary_icon(self, constituents, default):
        userid = constituents[0]['msg']['userid']
        return avatar_url(userid)

    def get_link(self, constituents):
        return ''
