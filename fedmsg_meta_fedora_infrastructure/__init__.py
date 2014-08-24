#-*- coding: utf-8 -*-

import fedora.client
import fedmsg.meta.base


class BaseProcessor(fedmsg.meta.base.BaseProcessor):
    topic_prefix_re = 'org\\.fedoraproject\\.(dev|stg|prod)'
    FAS = fedora.client.AccountSystem()

    def emails(self, msg, **config):
        usernames = self.usernames(msg, **config)
        emails = [name + "@fedoraproject.org" for name in usernames]
        return dict(zip(emails, usernames))

    def avatars(self, msg, **config):
        usernames = self.usernames(msg, **config)
        kwargs = dict(lookup_email=False)
        lookup = lambda x: self.FAS.avatar_url(x, **kwargs)
        urls = map(lookup, usernames)
        return dict(zip(usernames, urls))
