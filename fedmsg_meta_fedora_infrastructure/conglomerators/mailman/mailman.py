import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url_from_email


class ByMessageId(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return '.mailman.receive' in msg['topic']

    def matches(self, a, b, **config):
        a, b = a['msg']['msg'], b['msg']['msg']
        a_references, b_references = [], []
        if a['references']:
            a_references = [r.strip() for r in a['references'].split('\n')]
        if b['references']:
            b_references = [r.strip() for r in b['references'].split('\n')]

        a_references = set(a_references + [a['message-id']])
        b_references = set(b_references + [b['message-id']])

        # Return True if the messages share some subset of references.
        return a_references & b_references

    def get_secondary_icon(self, constituents, default):
        agents = set([m['msg']['msg']['from'] for m in constituents])

        # Just take the first.
        agent = sorted(agents)[0]

        email = agent.split('<')[-1].split('>')[0]

        return avatar_url_from_email(email)

    def get_link(self, constituents):
        links = set([m['msg']['msg']['archived-at'] for m in constituents])

        # Just take the first.
        link = sorted(links)[0]

        link = link.split('<')[-1].split('>')[0]

        return link

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        subtitle = u'{people} wrote {N} replies to the ' + \
            '"{subject}" thread on the {mlists} {predicate}'

        people = set([
            m['msg']['msg']['from'].split('<')[-1].split('>')[0]
            for m in ms
        ])
        mlists = set([m['msg']['mlist']['list_name'] for m in ms])
        predicate = 'list' if len(mlists) == 1 else 'lists'
        people = self.list_to_series(people)
        mlists = self.list_to_series(mlists)

        # Build a set of subjects and strip off the leading 'Re: RE: re: ...'
        subjects = set()
        for m in ms:
            subject = m['msg']['msg']['subject']
            if 're: ' in subject.lower():
                index = subject.lower().rindex('re: ') + 4
                subject = subject[index:]
            subjects.add(subject)

        # Just take the first....
        subject = sorted(subjects)[0]

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            people=people,
            N=len(ms),
            subject=subject,
            mlists=mlists,
            predicate=predicate,
        )
        tmpl['subjective'] = tmpl['subtitle']

        default = tmpl['icon']

        tmpl['secondary_icon'] = self.get_secondary_icon(constituents, default)
        tmpl['link'] = self.get_link(constituents)

        return tmpl
