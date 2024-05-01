# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:43:16 2024

@author: DELL
"""


import tkinter as tk
from connexion_db import connect_to_db
import os

def list_archive_commande():
   
    connection = connect_to_db()
    cursor = connection.cursor()
    
 
    cursor.execute("SELECT id_supp_cmd, date_supp, chemin FROM archive_cmd")
    archives = cursor.fetchall()

    def afficher_commande():
        
        selected_item = archive_listbox.curselection()
        selected_comand = archive_listbox.get(selected_item)
        selected_cmd_path = archive[2] 
        
        os.system(f"start {selected_cmd_path}")
       

    root = tk.Tk()
    root.title("Liste des Archives de Commandes")

    archive_listbox = tk.Listbox(root, width=50, height=20)
    archive_listbox.pack(padx=10, pady=10)

    for archive in archives:
        archive_listbox.insert(tk.END, archive)

    view_button = tk.Button(root, text="Afficher la Commande Sélectionnée", command=afficher_commande)
    view_button.pack(padx=10, pady=5)

    root.mainloop()



