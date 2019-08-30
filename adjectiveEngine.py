import re

class AdjectiveEngine():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pattern = r"\b\w+(ий|ый|ых|ые|ой|ей|ому|ему|ий|ья|ье)\b"
        self.regex = re.compile(self.pattern, re.MULTILINE)

    """
        @param string - any string
        @return list of detected adjectives
        Goal: get any string to obtain detected adjectives
    """
    def process(self, string: str):
        adjectives = list()
        start_pos = 0
        while(self.regex.search(string, start_pos) != None):
            print(self.regex.search(string, start_pos))
            print(self.regex.search(string).group(0))
            adjective = self.regex.search(string, start_pos).group(0)
            start_pos = start_pos + len(adjective) + string.find(adjective, start_pos)
            print(adjective)
            print(string[start_pos:])
            print("regex match: " + str(self.regex.search(string, start_pos)))
            adjectives.append(adjective)
        return adjectives if adjectives else None

    def __str__(self):
        return "Adjective engine: " + str(self.__hash__())
