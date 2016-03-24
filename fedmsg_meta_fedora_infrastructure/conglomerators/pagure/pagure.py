import fedmsg.meta.base
from fedmsg_meta_fedora_infrastructure.fasshim import avatar_url, email2fas


class AbstractPagureTicketConglomerator(fedmsg.meta.base.BaseConglomerator):

    def can_handle(self, msg, **config):
        target = 'pagure.{entity_name}.'.format(entity_name=self.entity_name)
        return target in msg['topic']

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


class ByNewStyleCommit(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return '.pagure.git.receive' in msg['topic'] and 'commit' not  in msg['msg']

    def matches(self, a, b, **config):
        a, b = a['msg'], b['msg']
        return a['repo']['name'] == b['repo']['name']

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        count = sum([m['msg']['total_commits'] for m in ms])
        agents = set([m['msg']['agent'] for m in ms])
        branches = [m['msg']['branch'].replace('refs/heads/', '') for m in ms]
        repo = ms[0]['msg']['repo']['name']
        subtitle = '{agents} pushed {count} commits to {repo} ({branches})'
        agents = self.list_to_series(agents)
        branches = self.list_to_series(branches)

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            agents=agents,
            repo=repo,
            count=count,
            branches=branches,
        )
        tmpl['subjective'] = tmpl['subtitle']

        tmpl['secondary_icon'] = avatar_url(ms[0]['msg']['agent'])
        link_template = 'https://pagure.io/{repo}/commits'
        tmpl['link'] = link_template.format(repo=repo)

        return tmpl


class ByOldStyleCommit(fedmsg.meta.base.BaseConglomerator):
    def can_handle(self, msg, **config):
        return '.pagure.git.receive' in msg['topic'] and 'commit' in msg['msg']

    def matches(self, a, b, **config):
        a, b = a['msg'], b['msg']
        return a['commit']['path'] == b['commit']['path']

    def merge(self, constituents, subject, **config):
        ms = constituents  # shorthand

        count = len(ms)
        agents = set([
            email2fas(m['msg']['commit']['email'], **config) for m in ms
        ])
        repo = ms[0]['msg']['commit']['repo']['name']
        subtitle = '{agents} pushed {count} commits to the {repo} project'
        agents = self.list_to_series(agents)

        tmpl = self.produce_template(constituents, subject, **config)
        tmpl['subtitle'] = subtitle.format(
            agents=agents,
            repo=repo,
            count=count,
        )
        tmpl['subjective'] = tmpl['subtitle']

        tmpl['secondary_icon'] = avatar_url(list(agents)[0])
        link_template = 'https://pagure.io/{repo}/commits'
        tmpl['link'] = link_template.format(repo=repo)

        return tmpl
