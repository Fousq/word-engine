import sys
import json

from parser import Parser
from engine import Engine
from api import API

OUTPUT_FILE_NAME = 'result.json'

if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) < 4 or not ('-login' in args and '-password' in args)):
        print("Usage main.py -login [login] -password [password]")
    _parser = Parser()
    parsed_args = None
    api = None
    uri_flag = False
    owner_id_flag = False
    post_id_flag = False
    if (len(args) is 8 and not ('-uri' in args)):
        parsed_args = _parser.parse_args(args)
        api = API(parsed_args['login'], parsed_args['password'])
        owner_id_flag = True
        post_id_flag = True
    elif (len(args) is 6 and '-uri' in args):
        parsed_args = _parser.parse_args(args)
        api = API(parsed_args['login'], parsed_args['password'])
        uri_flag = True
    elif (len(args) is 4):
        parsed_args = _parser.parse_args(args)
        api = API(parsed_args['login'], parsed_args['password'])
    
    if (not (owner_id_flag and post_id_flag)):
        uri = None
        if (uri_flag):
            uri = parsed_args['uri']
        else:
            uri = input("Enter the uri of the post: ")
        parsed_uri = _parser.parse_uri(uri)
        parsed_args['owner_id'] = parsed_uri['owner_id']
        parsed_args['post_id'] = parsed_uri['post_id']

    word_engine = Engine()
    comments = api.get_comments(parsed_args['owner_id'], parsed_args['post_id'])
    items = list()
    for comment in comments:
        items.append(word_engine.process(comment))

    f = open(OUTPUT_FILE_NAME, "w", encoding='utf8')
    f.write(json.dumps(items, ensure_ascii=False))