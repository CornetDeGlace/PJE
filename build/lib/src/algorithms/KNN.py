<<<<<<< HEAD
from Algorithm import Algorithm
from collections import OrderedDict

class KNN(Algorithm):
=======
from src.algorithms.Algorithm import Algorithm
from collections import OrderedDict

class KNN(Algorithm):

    # t1 = "bla bla blabla" t2 = "blu bla blabla"
    # private
    def distance(t1, t2):
        t1_list = t1.split()
        t2_list = t2.split()
        total_words_number = len(t1_list) + len(t2_list)
        common_words_number = 0
        history = set()
        for word in t1_list:
            if (word in t2_list) and (word not in history):
                common_words_number += 1
            history.add(word)    
        return ((total_words_number - common_words_number) / total_words_number)
    
    def jaccard_distance(t1, t2):
        t1_set = set(t1)
        t2_set = set(t2)
        intersection = len(list(t1_set.intersection(t2)))
        union = (len(t1_set) + len(t2_set)) - intersection
        return 1 - float(intersection) / union
    

>>>>>>> Dictionnaire
    def __init__(self):
        pass
    
    # sans réutilisation des tests déjà labélisés
    # sans pondération de la distance
    # TODO : fonction de pondération 
<<<<<<< HEAD
    def analyser_tweets(self, test_list, learning_list, neighbours_number):
=======
    # method neighbour => prend en paramètre un neighbor, et renvoie sa classe multipliée par une pondération (par défaut 1). On peut imaginer multiplier par sa distance par exemple.
    def analyser_tweets(self, test_list, learning_list, neighbours_number, ponderation_fonction = lambda neighbour, distance: neighbour[0]):
>>>>>>> Dictionnaire
        res = test_list.copy()
        neighbours = OrderedDict() # polarité : distance
        for tweet in test_list:
            for labeled_data in learning_list:
                distance = self.distance(tweet[5], labeled_data[5])
                if neighbours and len(neighbours.keys()) >= neighbours_number:
                    worst_neighbour = neighbours.keys()[-1]
                    if distance < neighbours[worst_neighbour]:
                        neighbours.pop(worst_neighbour)
                        neighbours[labeled_data[0]] = distance
                else :
                    neighbours[labeled_data[0]] = distance
<<<<<<< HEAD
            tweet[0] = max(neighbours.keys(), lambda neighbour: neighbour[0])
        return res

    # t1 = "bla bla blabla" t2 = "blu bla blabla"
    # private
    def distance(self, t1, t2):
        t1_list = t1.split()
        t2_list = t2.split()
        total_words_number = len(t1_list) + len(t2_list)
        common_words_number = 0
        history = set()
        for word in t1_list:
            if (word in t2_list) and (word not in history):
                common_words_number += 1
            history.add(word)    
        return ((total_words_number - common_words_number) / total_words_number)

    

if __name__ == "__main__":
    knn = KNN()
    print(knn.distance("bla bla test", "bla culk"))
    print(knn.distance("bkuvlab grub", "blab grib"))
=======
            tweet[0] = max(neighbours.keys(), lambda neighbour: ponderation_fonction(neighbour, distance))
        return res

    

if __name__ == "__main__":
    print(KNN.distance("bla bla test", "bla culk"), KNN.jaccard_distance("bla bla test", "bla culk"))
    print(KNN.distance("bkuvlab grub", "blab grib"), KNN.jaccard_distance("bkuvlab grub", "blab grib"))
>>>>>>> Dictionnaire


