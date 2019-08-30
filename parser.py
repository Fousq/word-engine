import argparse

class Parser():
    def __init__(self):
        self.arg_parser = argparse.ArgumentParser()
        self.arg_parser.add_argument('-login', required=True)
        self.arg_parser.add_argument('-password', required=True)
        self.arg_parser.add_argument('-owner_id', required=False)
        self.arg_parser.add_argument('-post_id', required=False)
        self.arg_parser.add_argument('-uri', required=False)

    """
        @param args - list of arguments
        @return dict of values of parsed arguments.
        Goal: parse args to work easly with api 
    """
    def parse_args(self, args):
        parsed_args = self.arg_parser.parse_args(args)
        print(parsed_args)
        print(type(parsed_args))
        return vars(parsed_args)
    
    """
        @param uri - string of uri
        @return dict of values of parsed uri
        Goal: parse uri to work with api
        Example of uri: https://vk.com/example?w=wall-owner_id_post_id
    """
    def parse_uri(self, uri: str):
        OWNER_ID_INDEX = 0
        POST_ID_INDEX = 1
        SPLITTER = '_'
        values = dict()
        token = '?w=wall'
        start_index = uri.find(token) + len(token)
        args = uri[start_index:].split(SPLITTER)
        values['owner_id'] = int(args[OWNER_ID_INDEX])
        values['post_id'] = int(args[POST_ID_INDEX])
        return values
