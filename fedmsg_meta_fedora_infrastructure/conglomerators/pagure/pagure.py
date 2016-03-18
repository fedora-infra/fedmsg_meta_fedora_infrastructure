import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url




class AbstractPagureTicketConglomerator(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return '.{entity_name}.'.format(entity_name=self.entity_name) in msg['topic']

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        count = len(ms)
        agents = set([m['msg']['agent'] for m in ms])
        idx = ms[0]['msg'][self.entity_key]['id']
        repo = self.get_repo(ms[0])
        subtitle = '{agents} interacted with {entity_name} #{idx} of project "{repo}" {count} times'

        agents = self.list_to_series(agents)

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            agents=agents,
            entity_name=self.entity_name,
            repo=repo,
            idx=idx,
            count=count,
        )
        tmpl['subjective'] = tmpl['subtitle']

        tmpl['secondary_icon'] = avatar_url(ms[0]['msg']['agent'])
        link_template = 'https://pagure.io/{repo}/{entity_name}/{idx}'
        tmpl['link'] = link_template.format(
            repo=repo,
            entity_name=self.entity_name,
            idx=idx,
        )

        return tmpl


class ByPR(AbstractPagureTicketConglomerator):
    entity_key = 'pullrequest'
    entity_name = 'pull-request'

    def matches(self, a, b, **config):
        a, b = a['msg'][self.entity_key], b['msg'][self.entity_key]
        return (
            a['id'] == b['id']
            and a['project']['name'] == b['project']['name']
        )

    def get_repo(self, msg):
        return msg['msg']['pullrequest']['project']['name']


class ByIssue(AbstractPagureTicketConglomerator):
    entity_key = 'issue'
    entity_name = 'issue'

    def matches(self, a, b, **config):
        a, b = a['msg'], b['msg']
        return (
            a[self.entity_key]['id'] == b[self.entity_key]['id']
            and a['project']['name'] == b['project']['name']
        )

    def get_repo(self, msg):
        return msg['msg']['project']['name']
