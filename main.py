import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if (len(args) < 4 or not ('-login' in args and '-password' in args)):
        print("Usage main.py -login [login] -password [password]")
    