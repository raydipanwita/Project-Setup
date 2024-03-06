class GrammarStats:
    def __init__(self):
        pass

    def check(self, text):
        if self.text[0].isupper and text[-1] in {"!" , ".", "?"}:
            return True
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass

    