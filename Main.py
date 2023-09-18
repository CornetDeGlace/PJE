import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv
import re

liste_apprentissage = []
liste_test = []
algorithmes = [
    {"name": "Dictionnaire", "description": "blabla sur dictionnaire"},
    {"name": "KNN", "description": "blabla de KNN"},
    {"name": "Bayes", "description": "blabla sur Bayes"}
]

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
        bouton_analyser_tweets.config(state="normal")
        bouton_sauvegarder.config(state="normal")  # Activer le bouton "Sauvegarder"
        afficher_tweets_importes()

def sauvegarder_textes_nettoyes():
    # Récupérer les textes nettoyés de la liste d'apprentissage
    textes_nettoyes = [nettoyage(ligne[5]) for ligne in liste_apprentissage]
    
    # Écrire les textes nettoyés dans un fichier texte
    with open("textes_nettoyes.txt", "w", encoding="utf-8") as fichier:
        for texte in textes_nettoyes:
            fichier.write(texte + "\n")

def analyse():
    pass

def nettoyage(commentaire):
    commentaire_nettoye = re.sub(r'(@[a-zA-Z0-9]+)', '@', commentaire)
    commentaire_nettoye = re.sub(r'([!?":;,])', r' \1 ', commentaire_nettoye)
    commentaire_nettoye = re.sub(r'(\$ ?\d+\.\d+)', '$XX', commentaire_nettoye)
    commentaire_nettoye = re.sub(r'([0-9]{1,2}\%)', 'XX%', commentaire_nettoye)
    return commentaire_nettoye

def on_selection(event):
    algo_name = selection_algo.get()
    for algo in algorithmes:
        if algo["name"] == algo_name:
            description_algo.config(text=algo["description"])

def afficher_tweets_importes():
    text_area.delete(1.0, tk.END)
    for ligne in liste_test:
        commentaire = ligne[5]
        commentaire_nettoye = nettoyage(commentaire)
        text_area.insert(tk.END, commentaire_nettoye + "\n")

def analyser_tweets():
    for ligne in liste_test:
        classification = classification_var.get()
        algorithme = selection_algo.get()
        # Insérez votre logique d'analyse ici et affichez le résultat dans le Text widget
        pass

main_window = tk.Tk()
main_window.title("Interface Graphique")

selection_algo = ttk.Combobox(main_window, values=[algo["name"] for algo in algorithmes], state="readonly")
selection_algo.pack(pady=10)
selection_algo.set(algorithmes[0]["name"])

description_algo = tk.Label(main_window, text=algorithmes[0]["description"])
description_algo.pack(padx=20, pady=20)

bouton_import_apprentissage = tk.Button(main_window, text="Importer fichier d'apprentissage", command=lambda: convert_csv_to_list(liste_apprentissage))
bouton_import_apprentissage.pack()

# Créez un espace visuel entre les boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Bouton "Sauvegarder" pour sauvegarder les textes nettoyés
bouton_sauvegarder = tk.Button(main_window, text="Sauvegarder", state="disabled", command=sauvegarder_textes_nettoyes)
bouton_sauvegarder.pack()

bouton_import_test = tk.Button(main_window, text="Importer fichier de test", command=lambda: convert_csv_to_list(liste_test))
bouton_import_test.pack(padx=20, pady=20)

text_area = tk.Text(main_window, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=20, pady=20)

classification_var = tk.StringVar()
classification_var.set("-1")

classification_combo = ttk.Combobox(main_window, textvariable=classification_var, values=["-1", "0", "2", "4"])
classification_combo.pack(padx=10, pady=10)

bouton_analyser_tweets = tk.Button(main_window, text="Analyser les tweets", command=analyser_tweets, state="disabled")
bouton_analyser_tweets.pack()

espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

resultat = tk.Label(main_window, text="Résultat : RIEN POUR L'INSTANT")
resultat.pack(padx=20, pady=20)

selection_algo.bind("<<ComboboxSelected>>", on_selection)

main_window.mainloop()
