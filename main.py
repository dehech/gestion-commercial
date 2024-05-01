# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:40:44 2023

@author: ASUS
"""

#gestion_stock.py

import tkinter as tk
from connexion_db import connect_to_db
from manipulation_prod import ajouter_produit, lister_produits, supprimer_produit, chercher_produit, inventaire, modifier_produit
from client import ajouter_client, chercher_client, lister_client, supprimer_client, modifier_client
from gestion_vente import vendre_produit_db
from commande import vendre_produit
#from teste import vendre_produit
from list_fact import consulter_fac
from list_com import consulter_comandes
from archive_fact import list_archive_fact
from archive_cmd import list_archive_commande

def deconnexion(root):
    root.destroy()  
    import sign_in

def main_interface():
    root = tk.Tk()
    root.title("StockMaster - Gestion de Stock")
    app_name_label = tk.Label(root, text="StockMaster - Gestion de Stock", bg="#7D4FFE", fg="white", font=("Arial", 14))
    app_name_label.pack(side="top", fill="x")
    root.geometry('800x600')
    root.configure(bg='#7D4FFE')
    
    # Cadre pour la vente
    frame_vente = tk.LabelFrame(root, text="Vente", bg='#7D4FFE', fg='white', font=("Arial", 12))
    frame_vente.pack(side="left", padx=20, pady=20)
    
    btn_vendre = tk.Button(frame_vente, text="Vendre un produit", command=lambda:vendre_produit_db(database))
    btn_vendre.pack(fill=tk.X, padx=10, pady=5)
    
    btn_commande = tk.Button(frame_vente, text="passer une commande", command=lambda:vendre_produit(database))
    btn_commande.pack(fill=tk.X, padx=10, pady=5)
    
    btn_fact = tk.Button(frame_vente, text="consulter facture", command=lambda:consulter_fac(database))
    btn_fact.pack(fill=tk.X, padx=10, pady=5)
    
    btn_comm = tk.Button(frame_vente, text="consulter commande", command=lambda:consulter_comandes(database))
    btn_comm.pack(fill=tk.X, padx=10, pady=5)
    
    btn_arch_com = tk.Button(frame_vente, text="consulter l'archive des commandes", command=lambda:list_archive_commande())
    btn_arch_com.pack(fill=tk.X, padx=10, pady=5)
    
    btn_arch_fact = tk.Button(frame_vente, text="consulter l'archive des factures", command=lambda:list_archive_fact())
    btn_arch_fact.pack(fill=tk.X, padx=10, pady=5)
    
    # Cadre pour produit
    frame_produits = tk.LabelFrame(root, text="Produits", bg='#7D4FFE', fg='white', font=("Arial", 12))
    frame_produits.pack(side="left", padx=20, pady=20)
    
    btn_ajouter = tk.Button(frame_produits, text="Ajouter un produit", command=lambda:ajouter_produit(database))
    btn_ajouter.pack(fill=tk.X, padx=10, pady=5)

    btn_lister = tk.Button(frame_produits, text="Lister tous les produits", command=lambda:lister_produits(database))
    btn_lister.pack(fill=tk.X, padx=10, pady=5)

    btn_chercher = tk.Button(frame_produits, text="Chercher un produit", command= lambda:chercher_produit(database))
    btn_chercher.pack(fill=tk.X, padx=10, pady=5)

    btn_inventaire = tk.Button(frame_produits, text="Inventaire", command=lambda:inventaire(database))
    btn_inventaire.pack(fill=tk.X, padx=10, pady=5)
    
    btn_supprimer = tk.Button(frame_produits, text="Supprimer produit", command=lambda:supprimer_produit(database))
    btn_supprimer.pack(fill=tk.X, padx=10, pady=5)
    
    btn_modifier = tk.Button(frame_produits, text="Modifier produit", command=lambda:modifier_produit(database))
    btn_modifier.pack(fill=tk.X, padx=10, pady=5)
    
    # Cadre pour client 
    frame_clients = tk.LabelFrame(root, text="Clients", bg='#7D4FFE', fg='white', font=("Arial", 12))
    frame_clients.pack(side="left", padx=20, pady=20)
    
    btn_ajouter_client = tk.Button(frame_clients, text="Ajouter client", command=lambda:ajouter_client(database))
    btn_ajouter_client.pack(fill=tk.X, padx=10, pady=5)
    
    btn_chercher_client = tk.Button(frame_clients, text="Chercher client", command=lambda:chercher_client(database))
    btn_chercher_client.pack(fill=tk.X, padx=10, pady=5)
    
    btn_lister_client = tk.Button(frame_clients, text="Lister tous les clients", command=lambda:lister_client(database))
    btn_lister_client.pack(fill=tk.X, padx=10, pady=5)
    
    btn_supp_client = tk.Button(frame_clients, text="Supprimer un client", command=lambda:supprimer_client(database))
    btn_supp_client.pack(fill=tk.X, padx=10, pady=5)
    
    btn_modif_client = tk.Button(frame_clients, text="Modifier un client", command=lambda:modifier_client(database))
    btn_modif_client.pack(fill=tk.X, padx=10, pady=5)
    
    btn_deconnexion = tk.Button(root, text="Déconnexion", bg="#A7001E", fg="white", command=lambda:deconnexion(root))
    btn_deconnexion.pack(anchor="nw", side="right", pady=5)  # Positionnement en haut à droite

    root.resizable(True, True)
#    database = connect_to_database()
    database = connect_to_db()
    
    footer = tk.Label(root, text="© Copyright 2024", relief=tk.GROOVE, bg="#7D4FFE", fg="white", font=("Arial", 12) )
    footer.pack(side=tk.BOTTOM, fill=tk.X)
    root.mainloop()


main_interface()