import engine
import api
import parser

import sys

def engine_test():
    word_engine = engine.Engine()
    words = word_engine.process("интересный, умный")
    print(words)

def api_test():
    API = api.API("+77021165878", "1234fifa")
    print(API)
    comments = API.get_comments(-37763998, 2455537)
    print(comments)

def parser_test():
    _parser = parser.Parser()
    parsed_args = _parser.parse_uri("https://vk.com/anime__lol?w=wall-143107500_30403")
    print(parsed_args)

if __name__ == "__main__":
    #engine_test()
    #api_test()
    parser_test()