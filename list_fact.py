# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:26:37 2024

@author: DELL
"""

import tkinter as tk
import mysql.connector

from datetime import datetime
import os

def consulter_fac(database):

    def lister_factures():
        cursor.execute("SELECT id_facture, chemin FROM facture")
        factures = cursor.fetchall()
        return factures

   
    def ouvrir_facture():
        selected_facture = listbox.curselection()
        if selected_facture:
            selected_facture_index = int(selected_facture[0])
            selected_facture_info = factures[selected_facture_index]
            selected_facture_path = selected_facture_info[1]
            os.system(f"start {selected_facture_path}")  


    def supprimer_facture():
        selected_facture = listbox.curselection()
        if selected_facture:
            selected_facture_index = int(selected_facture[0])
            selected_facture_info = factures[selected_facture_index]
            selected_facture_id = selected_facture_info[0]
            selected_facture_path = selected_facture_info[1]
            date_today = datetime.now().strftime("%Y-%m-%d")
            
         
            cursor.execute("INSERT INTO archive_fact (id_supp_fac, date_supp, chemin) VALUES (%s, %s, %s)",
                           (selected_facture_id, date_today, selected_facture_path))
            
        
            cursor.execute("DELETE FROM facture WHERE id_facture = %s", (selected_facture_id,))
            
            db.commit()
            refresh_listbox()


    def refresh_listbox():
        listbox.delete(0, tk.END)
        factures = lister_factures()
        for facture in factures:
            listbox.insert(tk.END, facture[0])

  
    db = database
    cursor = db.cursor()

   
    root = tk.Tk()
    root.title("Consulter les factures")
    root.geometry("500x500")

    label = tk.Label(root, text="Liste des factures disponibles:")
    label.pack()

   
    factures = lister_factures()
    listbox = tk.Listbox(root)
    listbox.config(height=20)
    listbox.config(width=-100)
    for facture in factures:
        listbox.insert(tk.END, facture[0])  
    listbox.pack()

 
    btn_ouvrir = tk.Button(root, text="Ouvrir la facture sélectionnée", command=ouvrir_facture)
    btn_ouvrir.pack()


    btn_supprimer = tk.Button(root, text="Supprimer la facture sélectionnée", command=supprimer_facture)
    btn_supprimer.pack()

    root.mainloop()
