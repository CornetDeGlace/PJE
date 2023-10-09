from Algorithm import Algorithm

class Dictionnary(Algorithm):

    def read_words_from_file(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                mots = contenu.split(',')
                mots_propres = [mot.strip().lower() for mot in mots if mot.strip()]
                return mots_propres
        except FileNotFoundError:
            print(f"Le fichier '{file_name}' n'a pas été trouvé.")
            return []
        
    def __init__(self):
        self.negative_list = Dictionnary.read_words_from_file("data/negative.txt")
        self.positive_list = Dictionnary.read_words_from_file("data/positive.txt")

    def analyser_tweets(self, liste_test_file):
        count = 0
        liste_test_analyse = []
        for tweet in liste_test_file:
            for mot in tweet[5].split():
                if mot in self.positive_list:
                    count += 1
                elif mot in self.negative_list:
                    count -= 1
            if count > 0:
                label = "4"
            elif count < 0:
                label = "0"
            else:
                label = "2"
            liste_test_analyse.append([label] + tweet[1:])
            count = 0
        return liste_test_analyse
    
    def analyser_tweets(self, liste_test_file):
        count = 0
        liste_test_analyse = []
        for tweet in liste_test_file:
            i = 0
            tmp = 0
            words = tweet[5].split()
            for i in range (len(words)):
                if words[i:i+tmp] in self.positive_list:
                    count += 1
                elif words[i:i+tmp] in self.negative_list:
                    count -= 1
                else:
                    pass
            if count > 0:
                label = "4"
            elif count < 0:
                label = "0"
            else:
                label = "2"
            liste_test_analyse.append([label] + tweet[1:])
            count = 0
        return liste_test_analyse
