import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import csv
import re
import Dictionnaire
import KNN
import Bayes

elements_tests = [["blabla1", 1], ["blabla2", 2], ["blabla3", 3], ["blabla4", 4]]

liste_apprentissage = []
liste_test = []
algorithmes = [
    {"name": "Dictionnaire", "description": "Algorithme Dictionnaire"},
    {"name": "KNN", "description": "Algorithme KNN"},
    {"name": "Bayes", "description": "Algorithme Bayes"}
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

    print(liste_test)

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
    # #5, Replace all links with void chain
    commentaire_nettoye = re.sub(r'https?://\S+|www\.\S+', '', commentaire_nettoye)
    return commentaire_nettoye

def on_selection(event):
    algo_name = selection_algo.get()
    for algo in algorithmes:
        if algo["name"] == algo_name:
            description_algo.config(text=algo["description"])

def afficher_tweets_importes():
    for item in liste_test:
        listbox.insert(tk.END, f"{item[0]} -> {item[5]}")
    # text_area.delete(1.0, tk.END)
    # for ligne in liste_test:
    #     commentaire = ligne[5]
    #     commentaire_nettoye = nettoyage(commentaire)
    #     text_area.insert(tk.END, commentaire_nettoye + "\n")

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

# def update_evaluation(*args):
#     new_value = combo_var.get()
#     liste_test[0] = new_value
#     for ligne in liste_test:
#         classification = classification_var.get()
#         algorithme = selection_algo.get()
#         # Insérez votre logique d'analyse ici et affichez le résultat dans le Text widget
#         pass

def edit_item():
    selected_index = listbox.curselection()
    if selected_index:
        new_value = combobox.get()
        if new_value:
            new_value = int(new_value)
            index = selected_index[0]
            liste_test[index][0] = new_value
            listbox.delete(index)
            listbox.insert(index, f"{new_value} -> {liste_test[index][5]}")
            print(liste_test)

main_window = tk.Tk()
main_window.title("Interface Graphique")
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
bouton_import_test = tk.Button(main_window, text="Importer fichier de test", command=lambda: convert_csv_to_list(liste_test))
bouton_import_test.pack(padx=20, pady=20)


# Zone de texte
# text_area = tk.Text(main_window, wrap=tk.WORD, width=40, height=10)
# text_area.pack(padx=20, pady=20)

# classification_var = tk.StringVar()
# classification_var.set("-1")

# classification_combo = ttk.Combobox(main_window, textvariable=classification_var, values=["-1", "0", "2", "4"])
# classification_combo.pack(padx=10, pady=10)

# Bouton d'analyser des tweets
bouton_analyser_tweets = tk.Button(main_window, text="Analyser les tweets", command=analyser_tweets, state="disabled")
bouton_analyser_tweets.pack()

espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Zone de résultat
resultat = tk.Label(main_window, text="Résultat : RIEN POUR L'INSTANT")
resultat.pack(padx=20, pady=20)

selection_algo.bind("<<ComboboxSelected>>", on_selection)


# Créez une Listbox pour afficher les deux éléments de chaque sous-liste
listbox = tk.Listbox(main_window, width=100)
listbox.pack()


# Créez une liste déroulante (combobox) pour les choix possibles de notes
choices = [-1, 0, 2, 4]
combobox = ttk.Combobox(main_window, values=choices)
combobox.pack()

# Par défaut, sélectionnez le premier élément de la liste déroulante
combobox.set(choices[0])

# Créez un bouton pour éditer des éléments
edit_button = tk.Button(main_window, text="Éditer", command=edit_item)
edit_button.pack()

# Créez un espace visuel entre les boutons
espace_entre_boutons = tk.Label(main_window, text="", height=1)
espace_entre_boutons.pack()

# Bouton "Sauvegarder" pour sauvegarder les textes nettoyés
bouton_sauvegarder = tk.Button(main_window, text="Sauvegarder", state="disabled", command=sauvegarder_textes_nettoyes)
bouton_sauvegarder.pack()

main_window.mainloop()
