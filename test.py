import engine

if __name__ == "__main__":
    engine = engine.Engine()
    words = engine.process("интересный, умный")
    print(words)