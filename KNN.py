class KNN:
    def __init__(self):
        pass

    def analyser_tweets(self):
        pass

    # t1 = "bla bla blabla" t2 = "blu bla blabla"
    def distance(self, t1, t2):
        t1_list = t1.split()
        t2_list = t2.split()

        t1_len = len(t1_list)
        t2_len = len(t2_list)

        nombre_total_de_mots = t1_len + t2_len
        nombre_de_mots_en_commun = 0

        historique = []

        for mot in t1_list:
            if (mot in t2_list) and (mot not in historique):
                nombre_de_mots_en_commun += 1
                print(mot)
            historique.append(mot)
            
        return ( (nombre_total_de_mots - nombre_de_mots_en_commun) / nombre_total_de_mots )

    



if __name__ == "__main__":
    knn = KNN()
    knn.distance("bla bla blabla", "blu bla blabla")

