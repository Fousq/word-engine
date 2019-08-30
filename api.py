import vk_api

MAX_COMMENTS = 100

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
    def get_comments(self, group_id: int, post_id: int):
        response = self.api.wall.getComments(owner_id=group_id, post_id=post_id, count=MAX_COMMENTS)
        print("items: " + str(response['items']))
        print("items type: " + str(type(response['items'])))
        print(response)
        comments = list()
        for item in response['items']:
            comments.append(item['text'])
        return comments
