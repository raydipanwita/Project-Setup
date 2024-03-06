
from lib.grammer_stats import *
class GrammerStats:
# """
# When the text does not starts with capital 
# and does not have a punctuatation in the end
# """

    def test_check_words_for_nocapital_nopunc():
        grammer = GrammarStats("hello Worlds")
        result = grammer.check()
        assert result == False


# """
# When the text starts with capital 
# but does not have a punctuatation in the end
# """

    def test_check_words_for_capital_but_nopunc():
        grammer = GrammarStats("Hello Worlds")
        result = grammer.check("hello Worlds")
        assert result == False

