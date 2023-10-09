
from src.algorithms.Dictionnary import Dictionnary

class Test_Dictionnary():

    def setup_method(self):
        self.dictionnary = Dictionnary()

    def test_distance(self):
        assert Dictionnary.distance("bla bleu bli", "blo bleu") == 0.4

print("cool")