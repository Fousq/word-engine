
class Engine():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    """
        @param string - any string
        @return dict of words with lexical value
        Goal: process any string to get lexical value of every word
    """
    def process(self, string):
        words = dict()
        return words