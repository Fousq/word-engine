import engine
import api

def engine_test():
    word_engine = engine.Engine()
    words = word_engine.process("интересный, умный")
    print(words)

def api_test():
    API = api.API("+77021165878", "1234fifa")
    print(API)
    comments = API.get_comments(-37763998, 2455537)
    print(comments)

if __name__ == "__main__":
    engine_test()
    api_test()