# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 22:08:32 2024

@author: DELL
"""

import tkinter as tk
from connexion_db import connect_to_db
import os

def list_archive_fact():
    
    connection = connect_to_db()
    cursor = connection.cursor()
    
    
    cursor.execute("SELECT id_supp_fac, date_supp, chemin FROM archive_fact")
    archives = cursor.fetchall()

    def afficher_facture():
       
        selected_item = archive_listbox.curselection()
        selected_facture = archive_listbox.get(selected_item)
        selected_fact_path = archive[2] 
        
        os.system(f"start {selected_fact_path}")
     

    root = tk.Tk()
    root.title("Liste des Archives de Factures")

    archive_listbox = tk.Listbox(root, width=50, height=20)
    archive_listbox.pack(padx=10, pady=10)

    for archive in archives:
        archive_listbox.insert(tk.END, archive)

    view_button = tk.Button(root, text="Afficher la Facture Sélectionnée", command=afficher_facture)
    view_button.pack(padx=10, pady=5)

    root.mainloop()



