
class AdjectiveEngine():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    """
        @param string - any string
        @return list of detected adjectives
        Goal: get any string to obtain detected adjectives
    """
    def process(self, string):
        adjectives = list()
        return adjectives

    def __str__(self):
        return "Adjective engine: " + str(self.__hash__())
