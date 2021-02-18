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


    # class CustomSsoSecurityManager(SupersetSecurityManager):
    #
    #     def oauth_user_info(self, provider, response=None):
    #         logging.debug("Oauth2 provider: {0}.".format(provider))
    #         if provider == 'egaSSO':
    #             # As example, this line request a GET to base_url + '/' + userDetails with Bearer  Authentication,
    #             # and expects that authorization server checks the token, and response with user details
    #             me = self.appbuilder.sm.oauth_remotes[provider].get('userDetails').data
    #             logging.debug("user_data: {0}".format(me))
    #             return {'name': me['name'], 'email': me['email'], 'id': me['user_name'],
    #                     'username': me['user_name'], 'first_name': '', 'last_name': ''}
