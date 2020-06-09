import logging
from superset.security import SupersetSecurityManager


class CustomSsoSecurityManager(SupersetSecurityManager):

    def oauth_user_info(self, provider, response=None):
        logging.debug("Oauth2 provider: {0}.".format(provider))

        if provider == 'boss':
            me = self.appbuilder.sm.oauth_remotes[provider].get('/boss/openapi/user/info?permission=SupersetLogin')
            result = me.data
            return {'first_name': result['nick'], 'username': result['userId'], 'email': result['userId']}

    ...
