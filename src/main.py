import tkinter as tk
from tkinter import ttk
import csv
import re
from src.algorithms import Dictionnary
from algorithms import KNN
from algorithms import Bayes
from helpers import *


liste_apprentissage = []
liste_test_file = []
liste_test_analyse = []

#Cette fonction transforme le fichier csv en liste de chaîne de caractères
def convert_csv_to_list(liste_a_modifier):
    file = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
    if file:
        with open(file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                liste_a_modifier.append(line)
    if liste_a_modifier != []:
        bouton_analyser_tweets.config(state="normal")
        # Activer le bouton "Sauvegarder"
        bouton_sauvegarder.config(state="normal")  
        afficher_tweets_importes(liste_test_file, listbox)

    # print(liste_test_file)
    
    

#Cette fonction sert à quiter l'application 
def quit():
    main_window.destroy()


main_window = tk.Tk()
main_window.title("Twitter Sentiments Analysis App")
main_window.geometry("600x600")

# Liste algorithmes
selection_algo = ttk.Combobox(main_window, values=[algo["name"] for algo in algorithmes], state="readonly")
selection_algo.pack(pady=10)
selection_algo.set(algorithmes[0]["name"])

# Description de l'algorithme choisi
description_algo = tk.Label(main_window, text=algorithmes[0]["description"])
description_algo.pack(padx=20, pady=20)

# Bouton d'import du fichier d'apprentissage
bouton_import_apprentissage = tk.Button(main_window, text="Importer fichier d'apprentissage", command=lambda: convert_csv_to_list(liste_apprentissage))
bouton_import_apprentissage.pack()

# Créez un espace visuel entre les boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Bouton d'import du fichier test
bouton_import_test = tk.Button(main_window, text="Importer fichier de test", command=lambda: convert_csv_to_list(liste_test_file))
bouton_import_test.pack(padx=20, pady=20)

# Bouton d'analyser des tweets
bouton_analyser_tweets = tk.Button(main_window, text="Analyser les tweets", command=lambda: analyser_tweets(selection_algo, liste_test_file), state="disabled")
bouton_analyser_tweets.pack()

# Espace
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Zone de résultat
# resultat = tk.Label(main_window, text="Résultat : RIEN POUR L'INSTANT")
# resultat.pack(padx=20, pady=20)

selection_algo.bind("<<ComboboxSelected>>", command=lambda: on_selection(selection_algo, description_algo))

# Créez une Listbox pour afficher les deux éléments de chaque sous-liste
listbox = tk.Listbox(main_window, width=100)
listbox.pack()

# Créez un espace visuel entre les boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Créez une liste déroulante (combobox) pour les choix possibles de notes
choices = [-1, 0, 2, 4]
combobox = ttk.Combobox(main_window, values=choices)
combobox.pack()

# Créez un espace visuel entre les boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Par défaut, sélectionnez le premier élément de la liste déroulante
combobox.set(choices[0])

# Créez un bouton pour éditer des éléments
edit_button = tk.Button(main_window, text="Éditer", command=lambda: edit_item(liste_test_file, listbox, combobox))
edit_button.pack()

# Créez un espace visuel entre les boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Bouton "Sauvegarder" pour sauvegarder les textes nettoyés
bouton_sauvegarder = tk.Button(main_window, text="Sauvegarder", state="disabled", command=sauvegarder_textes_nettoyes)
bouton_sauvegarder.pack()

main_window.mainloop()
