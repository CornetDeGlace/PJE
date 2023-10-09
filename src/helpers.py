import csv 
from tkinter import filedialog
import tkinter as tk
import re 
from src.algorithms import Dictionnary, KNN, Bayes


algorithmes = [
    {"name": "Dictionnaire", "description": "Algorithme Dictionnaire"},
    {"name": "KNN", "description": "Algorithme KNN"},
    {"name": "Bayes", "description": "Algorithme Bayes"}
]

#Cette fonction sauvegarde les tweets nettoyés
def sauvegarder_textes_nettoyes():
    # Récupérer les textes nettoyés de la liste d'apprentissage
    textes_nettoyes = [nettoyage(ligne[5]) for ligne in liste_apprentissage]
    # Écrire les textes nettoyés dans un fichier texte
    with open("textes_nettoyes.txt", "w", encoding="utf-8") as fichier:
        for texte in textes_nettoyes:
            fichier.write(texte + "\n")


#Cette fonction nettoie les tweets
def nettoyage(commentaire):
    commentaire_nettoye = re.sub(r'(@[a-zA-Z0-9]+)', '@', commentaire)
    commentaire_nettoye = re.sub(r'([!?".:;,])', r' \1 ', commentaire_nettoye)
    commentaire_nettoye = re.sub(r'(\$ ?\d+\.\d+)', '$XX', commentaire_nettoye)
    commentaire_nettoye = re.sub(r'([0-9]{1,2}\%)', 'XX%', commentaire_nettoye)
    commentaire_nettoye = re.sub(r'https?://\S+|www\.\S+', '', commentaire_nettoye)
    commentaire_nettoye = commentaire_nettoye.replace(',', '')
    return commentaire_nettoye

#Cette fonction décrit l'algorihtme utilisé
def on_selection(event, selection_algo, description_algo):
    algo_name = selection_algo.get()
    for algo in algorithmes:
        if algo["name"] == algo_name:
            description_algo.config(text=algo["description"])

#Cette fonction affiche les tweets importés sur le GUI
def afficher_tweets_importes(liste_test_file, listbox):
    for item in liste_test_file:
        listbox.insert(tk.END, f"{item[0]} -> {item[5]}")


def analyser_tweets(selection_algo, liste_test_file):
    # Récupérer le nom de l'algorithme sélectionné
    algo_name = selection_algo.get()
    
    # Afficher le nom de l'algorithme dans le terminal
    # print(f"Algorithme sélectionné : {algo_name}")
    
    if algo_name == "Dictionnaire":
        # Appeler la fonction de l'algorithme de Dictionnaire
        dictionnaire = Dictionnary.Dictionnaire()
        liste_test_file_dictionnaire = [tweet[:5] + [nettoyage(tweet[5])] + tweet[5:5] for tweet in liste_test_file]
        liste_test_analyse = dictionnaire.analyser_tweets(liste_test_file_dictionnaire)

        # print("résultat : ")
        # print(liste_test_analyse)
        # print("fin résultat")

    elif algo_name == "KNN":
        # Appeler la fonction de l'algorithme de KNN
        knn = KNN.KNN()
        knn.analyser_tweets()
        
    elif algo_name == "Bayes":
        # Appeler la fonction de l'algorithme de Bayes
        bayes = Bayes.Bayes()
        bayes.analyser_tweets()
        
    else:
        # Gérer une sélection invalide (facultatif)
        # print("Algorithme non pris en charge")
        pass

def edit_item(liste_test_file, listbox, combobox):
    selected_index = listbox.curselection()
    if selected_index:
        new_value = combobox.get()
        if new_value:
            new_value = int(new_value)
            index = selected_index[0]
            liste_test_file[index][0] = new_value
            listbox.delete(index)
            listbox.insert(index, f"{new_value} -> {liste_test_file[index][5]}")
            # print(liste_test_file)
    
    print(liste_test_file)