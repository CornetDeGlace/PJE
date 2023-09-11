import tkinter as tk
from tkinter import filedialog
import csv
from tkinter import ttk

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
    print(nettoyage(liste_test))

def analyse():
    pass

def nettoyage(csv_list):
    commentaires = []
    for line in csv_list:
        commentaires.append(line[5])
    return commentaires

def on_selection(event):
    algo_name = selection_algo.get()
    for algo in algorithmes:
        if algo["name"] == algo_name:
            description_algo.config(text=algo["description"])
            


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

bouton_analyser = tk.Button(main_window, text="Analyser avec IA", command=analyse, state="disabled")
bouton_analyser.pack()

bouton_analyser = tk.Button(main_window, text="Afficher le résultat", command=analyse, state="disabled")
bouton_analyser.pack()

resultat = tk.Label(main_window, text="Résultat : RIEN POUR L'INSTANT")
resultat.pack(padx=20, pady=20)

bouton_analyser = tk.Button(main_window, text="Sauvegarder")
bouton_analyser.pack(padx=20, pady=20)  

selection_algo.bind("<<ComboboxSelected>>", on_selection)

main_window.mainloop()