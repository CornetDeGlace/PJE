import tkinter as tk
from tkinter import filedialog
import csv
from tkinter import ttk

csv_list = []
algorithmes = [{"name" : "Dictionnaire", "description" : "blabla sur dictionnaire"}, {"name" : "KNN", "description" : "blaba de KNN"}, {"name" : "Bayes", "description" : "blabla sur Bayes"}]

def quit():
    main_window.destroy()

def convert_csv_to_list():
    file = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
    if file:
        with open(file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                csv_list.append(line)
    if csv_list != []:
        bouton_analyser.config(state="normal")
    print(csv_list)

def analyse():
    pass

def on_selection(event):
    algo_name = selection_algo.get()
    for algo in algorithmes:
        if algo["name"] == algo_name:
            description_algo.config(text=algo["description"])

main_window = tk.Tk()
main_window.title("Interface Graphique")

bouton_import = tk.Button(main_window, text="Importer un fichier CSV", command=convert_csv_to_list)
bouton_import.pack(padx=20, pady=20)

description_algo = tk.Label(main_window, text=algorithmes[0]["description"])
description_algo.pack(padx=20, pady=20)

selection_algo = ttk.Combobox(main_window, values=[algo["name"] for algo in algorithmes], state="readonly")
selection_algo.pack(pady=10)
selection_algo.set(algorithmes[0]["name"])

bouton_analyser = tk.Button(main_window, text="Analyser", command=analyse, state="disabled")
bouton_analyser.pack()

resultat = tk.Label(main_window, text="Résultat : RIEN POUR L'INSTANT")
resultat.pack(padx=20, pady=20)

# Lier la fonction à l'événement de changement de sélection de la combobox
selection_algo.bind("<<ComboboxSelected>>", on_selection)


main_window.mainloop()
