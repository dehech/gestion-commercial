# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:56:26 2023

@author: DELL
"""

import tkinter as tk

def vendre_produit():
    # Logique pour la vente d'un produit
    print("Produit vendu !")

def ajouter_produit():
    # Logique pour ajouter un produit au stock
    print("Produit ajouté au stock !")
    
# Fonctions pour les options du menu
def option_fichier():
    print("Option Fichier")

def option_ajouter():
    ajouter_produit()

def option_vendre():
    vendre_produit()

def main_interface():
# Création de la fenêtre principale
    root = tk.Tk()
    root.title("Gestion de Stock et Vente")

# Barre de menu
    menu_bar = tk.Menu(root)


# Menu Fichier
    menu_fichier = tk.Menu(menu_bar, tearoff=0)
    menu_fichier.add_command(label="Quitter", command=root.quit)
    menu_bar.add_cascade(label="Fichier", menu=menu_fichier)

# Menu Opérations
    menu_operations = tk.Menu(menu_bar, tearoff=0)
    menu_operations.add_command(label="Ajouter un produit", command=option_ajouter)
    menu_operations.add_command(label="Vendre un produit", command=option_vendre)
    menu_bar.add_cascade(label="Opérations", menu=menu_operations)

# Configurer la barre de menu
    root.config(menu=menu_bar)
    
# Créer un label pour afficher le message
    label_message = tk.Label(root, text="Bienvenue dans votre application de gestion de stock")
    label_message.pack()


# Bouton pour vendre un produit
    btn_vendre = tk.Button(root, text="Vendre un produit", command=vendre_produit)
    btn_vendre.pack()

# Bouton pour ajouter un produit au stock
    btn_ajouter = tk.Button(root, text="Ajouter un produit", command=ajouter_produit)
    btn_ajouter.pack()
    
# Boucle principale pour démarrer l'interface graphique
    root.mainloop()
