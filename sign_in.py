# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:58:38 2023

@author: DELL
"""
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
#import untitled0
#def verify_login():
 #   username = username_entry.get()
 #   password = password_entry.get()
    
    # Vérification des informations de login ici
    # Si les informations sont correctes, passer au tableau de bord
    # Sinon afficher un message d'erreur
    
    
def ouvrir_interface_principale():
    root.destroy()  # Fermer la fenêtre de connexion
    # Ajouter ici le code pour ouvrir l'autre interface
    import untitled0
    #untitled0.main_interface()

def verifier_identifiants():
    nom_utilisateur = username_entry.get()
    mot_de_passe = password_entry.get()
    
    try:
        # Connexion à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="projet_python"
        )
        
        mycursor = mydb.cursor()
        
        # Exemple de requête pour vérifier les informations de connexion
        query = "SELECT * FROM access WHERE nom_user = %s AND mot_de_passe = %s"
        mycursor.execute(query, (nom_utilisateur, mot_de_passe))
        result = mycursor.fetchone()
        
        if result:
            print("Connexion réussie !")
            # Ajoutez ici la logique pour continuer vers l'application principale
            ouvrir_interface_principale()
        else:
            print("Identifiants incorrects.")
            # Ajoutez ici la logique pour afficher un message d'erreur dans l'interface
            
        mycursor.close()
        mydb.close()
        
    except mysql.connector.Error as err:
        print(f"Erreur de connexion à la base de données : {err}")

def load_image():
    # Charger l'image avec PIL et conserver une référence globale
    global background_image
    image = Image.open("gestion-stock-commerce.png")
    background_image = ImageTk.PhotoImage(image)
    
    # Obtenir les dimensions de l'image de fond
    image_width = image.width
    image_height = image.height
    
    
    # Si l'image est grande, ajuster les dimensions de la fenêtre
    window_width = min(800, image_width + 100)
    window_height = min(600, image_height + 100)
    
    # Créer un canevas avec les dimensions de l'image
    canvas.config(width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
    
    # Ajuster la taille de la fenêtre
    root.geometry(f"{window_width}x{window_height}")


root = tk.Tk()
root.title("StockMaster - Gestion de Stock")
app_name_label = tk.Label(root, text="StockMaster - Gestion de Stock", bg="#7D4FFE", fg="white", font=("Arial", 14))
app_name_label.pack(side="top", fill="x")

canvas = tk.Canvas(root)
canvas.pack()


login_frame = tk.Frame(root, bg='#7D4FFE', padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

username_label = tk.Label(login_frame, text="Nom d'utilisateur:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Mot de passe:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Se connecter", command=verifier_identifiants)
login_button.grid(row=2, columnspan=2)

# Appeler la fonction pour charger l'image
load_image()


root.mainloop()



