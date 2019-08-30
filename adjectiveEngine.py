import re

class AdjectiveEngine():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pattern = r"\b\w+(ий|ый|ых|ые|ой|ей|ому|ему|ий|ья|ье)\b"
        self.regex = re.compile(self.pattern)

    """
        @param string - any string
        @return list of detected adjectives
        Goal: get any string to obtain detected adjectives
    """
    def process(self, string):
        adjectives = list()
        start_pos = 0
        while(self.regex.search(string, start_pos) != None):
            print(self.regex.search(string, start_pos))
            adjective = self.regex.search(string).string
            start_pos = start_pos + len(adjective)
            print(adjective)
            print("regex match: " + str(self.regex.search(string, start_pos)))
            adjectives.append(adjective)
        return adjectives

    def __str__(self):
        return "Adjective engine: " + str(self.__hash__())
