import vk_api

"""
    Outter api class for working with Vk api
    req: login and password of user to work with vk api
"""
class API():
    def __init__(self, login, password):
        self.login = login
        self.password = password
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()

        self.api = vk_session.get_api()

    """
        @return return list of comments
        Goal: get avaliable comments of the post
    """
    def get_comments(self):
        pass
