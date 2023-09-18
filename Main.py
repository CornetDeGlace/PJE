import tkinter as tk
from tkinter import filedialog
import csv
from tkinter import ttk
import re
import Dictionnaire
import KNN
import Bayes


listeTest = ['4', '3', 'Mon May 11 03:17:40 UTC 2009', 'kindle2', 'tpryan', '@stellargirl I loooooooovvvvvveee my Kindle2. Not that the DX is cool, but the 2 is fantastic in its own right.']

liste_apprentissage = []
liste_test = []
algorithmes = [{"name" : "Dictionnaire", "description" : "blabla sur dictionnaire"}, {"name" : "KNN", "description" : "blaba de KNN"}, {"name" : "Bayes", "description" : "blabla sur Bayes"}]

def quit():
    main_window.destroy()

def convert_csv_to_list(liste_a_modifier):
    file = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
    if file:
        with open(file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                liste_a_modifier.append(line)
    if liste_a_modifier != []:
        bouton_analyser.config(state="normal")
        afficher_tweets_importes()  # Affiche les tweets importés après importation

def analyse():
    pass

def nettoyage(commentaire):
    # #1, Replace @username with @
    commentaire_nettoye = re.sub(r'(@[a-zA-Z0-9]+)', '@', commentaire)
    # #2, Add white space character before and after ! ? : . " ; ,
    commentaire_nettoye = re.sub(r'([!?":;,])', r' \1 ', commentaire_nettoye)
    # #3, Replace dollar values with variable ( $14.99 => $XX) (idem euros)
    commentaire_nettoye = re.sub(r'(\$ ?\d+\.\d+)', '$XX', commentaire_nettoye)
    # #4, Replace percentage values with variable (25n% => XXn%)
    commentaire_nettoye = re.sub(r'([0-9]{1,2}\%)', 'XX%', commentaire_nettoye)
    # #5, Replace all links with void chain
    commentaire_nettoye = re.sub(r'https?://\S+|www\.\S+', '', commentaire_nettoye)
    return commentaire_nettoye

def on_selection(event):
    algo_name = selection_algo.get()
    for algo in algorithmes:
        if algo["name"] == algo_name:
            description_algo.config(text=algo["description"])

def afficher_tweets_importes():
    text_area.delete(1.0, tk.END)  # Efface le contenu précédent du Text widget
    for ligne in liste_test:
        commentaire = ligne[5]  # Supposons que le commentaire est dans la sixième colonne.
        commentaire_nettoye = nettoyage(commentaire)
        text_area.insert(tk.END, commentaire_nettoye + "\n")  # Ajoute le commentaire nettoyé avec un saut de ligne

def analyser_tweets():
    # Récupérer le nom de l'algorithme sélectionné
    algo_name = selection_algo.get()
    
    # Afficher le nom de l'algorithme dans le terminal
    print(f"Algorithme sélectionné : {algo_name}")
    
    if algo_name == "Dictionnaire":
        # Appeler la fonction de l'algorithme de Dictionnaire
        Dictionnaire.analyser_tweets(liste_test)
    elif algo_name == "KNN":
        # Appeler la fonction de l'algorithme de KNN
        KNN.analyser_tweets(liste_test)
    elif algo_name == "Bayes":
        # Appeler la fonction de l'algorithme de Bayes
        Bayes.analyser_tweets(liste_test)
    else:
        # Gérer une sélection invalide (facultatif)
        print("Algorithme non pris en charge")


def update_evaluation(*args):
    new_value = combo_var.get()
    liste_test[0] = new_value

main_window = tk.Tk()
main_window.title("Interface Graphique")

selection_algo = ttk.Combobox(main_window, values=[algo["name"] for algo in algorithmes], state="readonly")
selection_algo.pack(pady=10)
selection_algo.set(algorithmes[0]["name"])

description_algo = tk.Label(main_window, text=algorithmes[0]["description"])
# description_algo.pack(padx=20, pady=20)

bouton_import = tk.Button(main_window, text="Import fichier d'apprentissage", command=lambda: convert_csv_to_list(liste_apprentissage))
bouton_import.pack()

bouton_import = tk.Button(main_window, text="Import fichier de test", command=lambda: convert_csv_to_list(liste_test))
bouton_import.pack(padx=20, pady=20)

# Créez un widget Text pour afficher les tweets
text_area = tk.Text(main_window, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=20, pady=20)

# Bouton pour analyser les tweets
bouton_analyser_tweets = tk.Button(main_window, text="Analyser les tweets", command=analyser_tweets, state="disabled")
bouton_analyser_tweets.pack()

# Espace entre les deux boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()
label = tk.Label(main_window, text=listeTest[5])
label.pack(padx=10, pady=10)
# Créer une liste déroulante pour modifier le premier élément
combo_var = tk.StringVar()
combo_var.set(listeTest[0])  # Initialiser la liste déroulante avec la première valeur de la liste
combo = ttk.Combobox(main_window, textvariable=combo_var, values=["-1", "0", "1", "2", "4"])
combo.pack(padx=10, pady=10)

# Associer la fonction de mise à jour à la liste déroulante
combo_var.trace_add("write", update_evaluation)

# Bouton pour afficher le résultat
bouton_afficher_resultat = tk.Button(main_window, text="Afficher le résultat", command=afficher_tweets_importes, state="disabled")
bouton_afficher_resultat.pack()

resultat = tk.Label(main_window, text="Résultat : RIEN POUR L'INSTANT")
resultat.pack(padx=20, pady=20)

bouton_analyser = tk.Button(main_window, text="Sauvegarder")
bouton_analyser.pack(padx=20, pady=20)  

selection_algo.bind("<<ComboboxSelected>>", on_selection)

main_window.mainloop()