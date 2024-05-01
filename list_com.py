# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:14:46 2024

@author: DELL
"""

import tkinter as tk
from datetime import datetime
import os

def consulter_comandes(database):

    def lister_commandes():
        cursor.execute("SELECT id_cmd, chemin FROM commande")
        commandes = cursor.fetchall()
        return commandes


    def ouvrir_commandes():
        selected_com = listbox.curselection()
        if selected_com:
            selected_com_index = int(selected_com[0])
            selected_com_info = commandes[selected_com_index]
            selected_com_path = selected_com_info[1]
            os.system(f"start {selected_com_path}")  

    
    def supprimer_commande():
        selected_com = listbox.curselection()
        if selected_com:
            selected_com_index = int(selected_com[0])
            selected_com_info = commandes[selected_com_index]
            selected_com_id = selected_com_info[0]
            selected_com_path = selected_com_info[1]
            date_today = datetime.now().strftime("%Y-%m-%d")
            
         
            cursor.execute("INSERT INTO archive_cmd (id_supp_cmd, date_supp, chemin) VALUES (%s, %s, %s)",
                           (selected_com_id, date_today, selected_com_path))
            
           
            cursor.execute("DELETE FROM commande WHERE id_cmd = %s", (selected_com_id,))
            
            db.commit()
            refresh_listbox()

  
    def refresh_listbox():
        listbox.delete(0, tk.END)
        commandes = lister_commandes()
        for com in commandes:
            listbox.insert(tk.END, com[0])

   
    db = database
    cursor = db.cursor()


    root = tk.Tk()
    root.title("Consulter les commandes")
    root.geometry("500x500")

    label = tk.Label(root, text="Liste des commandes disponibles:")
    label.pack()

   
    commandes = lister_commandes()
    listbox = tk.Listbox(root)
    listbox.config(height=20)
    listbox.config(width=-100)
    for com in commandes:
        listbox.insert(tk.END, com[0]) 
    listbox.pack()


    btn_ouvrir = tk.Button(root, text="Ouvrir la commande sélectionnée", command=ouvrir_commandes)
    btn_ouvrir.pack()

    
    btn_supprimer = tk.Button(root, text="Supprimer la commande sélectionnée", command=supprimer_commande)
    btn_supprimer.pack()

    root.mainloop()
