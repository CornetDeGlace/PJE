class Dictionnaire:
    def __init__(self):
        self.positive_list = []
        self.negative_list = []

    def analyser_tweets(self, liste_test_file):
        liste_test_analyse = []
        for tweet in liste_test_file:
            # Analyser le tweet ici en utilisant votre méthode d'annotation
            # Vous pouvez comparer les mots du tweet avec self.positive_list et self.negative_list
            pass

    def charge_positive(self, positive_file_path):
        try:
            with open(positive_file_path, 'r', encoding='utf-8') as file:
                self.positive_list = file.read().splitlines()
        except FileNotFoundError:
            print(f"Le fichier {positive_file_path} n'a pas été trouvé.")

    def charge_negative(self, negative_file_path):
        try:
            with open(negative_file_path, 'r', encoding='utf-8') as file:
                self.negative_list = file.read().splitlines()
        except FileNotFoundError:
            print(f"Le fichier {negative_file_path} n'a pas été trouvé.")

# Exemple d'utilisation :
dico = Dictionnaire()
dico.charge_positive('positive.txt')
dico.charge_negative('negative.txt')

# Maintenant, vous pouvez utiliser les listes self.positive_list et self.negative_list
# pour analyser les tweets dans la méthode analyser_tweets.
