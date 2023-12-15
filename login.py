# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#login.py
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
root ['bg']= 'sky blue'
root.geometry ('400x400')
print('hello')




# Labels et champs d'entrée pour le nom d'utilisateur et le mot de passe
label_nom_utilisateur = tk.Label(root, text="Nom d'utilisateur:")
label_nom_utilisateur.place(x=40, y=40)
entry_nom_utilisateur = tk.Entry(root)
entry_nom_utilisateur.place(x=40, y=60) 

label_mot_de_passe = tk.Label(root, text="Mot de passe:")
label_mot_de_passe.place(x=40 , y=80)
entry_mot_de_passe = tk.Entry(root, show="*")  # Pour cacher le mot de passe
entry_mot_de_passe.place(x=40 , y=100)

# Bouton de connexion
btn_connexion = tk.Button(root, text="Se connecter", command=verifier_identifiants)
btn_connexion.place(x=40 , y=120)

# Boucle principale pour démarrer l'interface graphique
root.mainloop()