# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:12:59 2023

@author: DELL
"""
import untitled0
import tkinter as tk
def ouvrir_interface_principale():
    # Fermer la fenêtre de connexion
    root.destroy()
    # Appeler la fonction pour créer et afficher l'autre interface à partir de l'autre module
    untitled0.main_interface()

def verifier_identifiants():
    nom_utilisateur = entry_nom_utilisateur.get()
    mot_de_passe = entry_mot_de_passe.get()
    
    # Votre logique de vérification des identifiants
    if nom_utilisateur == "firas" and mot_de_passe == "123":
        print("Connexion réussie !")
        # Ajoutez ici la logique pour continuer vers l'application principale
        ouvrir_interface_principale()
    else:
        print("Identifiants incorrects.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface de Connexion")

# Labels et champs d'entrée pour le nom d'utilisateur et le mot de passe
label_nom_utilisateur = tk.Label(root, text="Nom d'utilisateur:")
label_nom_utilisateur.pack()
entry_nom_utilisateur = tk.Entry(root)
entry_nom_utilisateur.pack()

label_mot_de_passe = tk.Label(root, text="Mot de passe:")
label_mot_de_passe.pack()
entry_mot_de_passe = tk.Entry(root, show="*")  # Pour cacher le mot de passe
entry_mot_de_passe.pack()

# Bouton de connexion
btn_connexion = tk.Button(root, text="Se connecter", command=verifier_identifiants)
btn_connexion.pack()

# Boucle principale pour démarrer l'interface graphique
root.mainloop()
