from Algorithm import Algorithm

class Dictionnaire(Algorithm):
    def __init__(self):
        self.negative_list = self.mots_depuis_fichier("data/negative.txt")
        self.positive_list = self.mots_depuis_fichier("data/positive.txt")

    def analyser_tweets(self, liste_test_file):
        compteur_positive = 0
        compteur_negative = 0
        liste_test_analyse = []
        for tweet in liste_test_file:
            for mot in tweet[5].split():
                if mot in self.positive_list:
                    compteur_positive += 1
                elif mot in self.negative_list:
                    compteur_negative += 1
            if compteur_positive > compteur_negative:
                liste_test_analyse.append(["4"] + tweet[1:])
            elif compteur_negative > compteur_positive:
                liste_test_analyse.append(["0"] + tweet[1:])
            else:
                liste_test_analyse.append(["2"] + tweet[1:])
            compteur_positive = 0
            compteur_negative = 0
        print(liste_test_analyse)
        return liste_test_analyse

    def mots_depuis_fichier(self, nom_fichier):
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                mots = contenu.split(',')
                mots_propres = [mot.strip() for mot in mots if mot.strip()]
                return mots_propres
        except FileNotFoundError:
            print(f"Le fichier '{nom_fichier}' n'a pas été trouvé.")
            return []
