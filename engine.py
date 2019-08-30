from adjectiveEngine import AdjectiveEngine

class Engine():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lexalEngines = dict()
        self.lexalEngines["adjectives"] = AdjectiveEngine()

    """
        @param string - any string
        @return dict of words with lexical value
        Goal: process any string to get lexical value of every word
    """
    def process(self, string):
        words = dict()
        print(self.lexalEngines)
        for lexalEngine in self.lexalEngines:
            print("engine: " + lexalEngine)
            print("engine class: " + str(self.lexalEngines[lexalEngine]))
            words[lexalEngine] = self.lexalEngines.get(lexalEngine).process(string)
        return words