import tkinter as tk
from tkinter import filedialog
import csv

csv_list = []

def quit():
    main_window.destroy()

def convert_csv_to_list():
    file = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
    if file:
        with open(file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                csv_list.append(line)
    print(csv_list)

main_window = tk.Tk()
main_window.title("Interface Graphique")

# label = tk.Label(main_window, text="rien pour l'instant")
# label.pack(padx=20, pady=20)

bouton_import = tk.Button(main_window, text="Importer un fichier CSV", command=convert_csv_to_list)
bouton_import.pack(padx=20, pady=20)

bouton_fermer = tk.Button(main_window, text="Fermer", command=quit)
bouton_fermer.pack()

main_window.mainloop()
