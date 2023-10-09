
from src.algorithms.KNN import KNN

class Test_KNN():

    def setup_method(self):
        self.KNN = KNN()

    def test_distance(self):
        assert KNN.distance("bla bleu bli", "blo bleu") == 0.8
    
    def jaccard_distance(self):
        assert KNN.jaccard_distance("bla bleu bli", "blo bleu") == 0.8