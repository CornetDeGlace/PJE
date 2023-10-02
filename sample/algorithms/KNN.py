from Algorithm import Algorithm

class KNN:
    def __init__(self):
        pass

    def analyser_tweets(self):
        pass

    # t1 = "bla bla blabla" t2 = "blu bla blabla"
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


