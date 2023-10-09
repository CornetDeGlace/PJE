from src.algorithms.Algorithm import Algorithm

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
        liste_test_analyse = []
        for tweet in liste_test_file:
            liste_test_analyse.append([self.analyze_tweet(tweet)] + tweet[1:])
        return liste_test_analyse
    
    def analyze_tweet_content(self, tweet_content):
            count = self.count_positive_negative_words(tweet_content)
            if count > 0:
                label = "4"
            elif count < 0:
                label = "0"
            else:
                label = "2"
            return label 
    
    def count_positive_negative_words(self, words):
        count = 0
        for word in words.split():
                if word in self.positive_list:
                    count += 1
                elif word in self.negative_list:
                    count -= 1
        return count
    
