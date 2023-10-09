
from src.algorithms.Dictionnary import Dictionnary

class Test_Dictionnary():

    def setup_method(self):
        self.dictionnary = Dictionnary()
        self.dictionnary.positive_list = ["good", "amazing"]
        self.dictionnary.negative_list = ["bad", "wrong"]

    def test_count_words(self):
        phrase = "Don't get me wrong this was good and amazing"
        assert self.dictionnary.count_positive_negative_words(phrase) == 1

    def test_positive_phrase(self):
        phrase = "Don't get me wrong this was good and amazing"
        assert self.dictionnary.analyze_tweet_content(phrase) == "4"

    def test_neutral_phrase(self):
        phrase = "Don't get me wrong this was good"
        assert self.dictionnary.analyze_tweet_content(phrase) == "2"

    def test_negative_phrase(self):
        phrase = "Don't get me wrong"
        assert self.dictionnary.analyze_tweet_content(phrase) == "0"