# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:58:38 2023

@author: DELL
"""
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from connexion_db import connect_to_db

    
    
def ouvrir_interface_principale():
    root.destroy()  
    import main

def verifier_identifiants():
    nom_utilisateur = username_entry.get()
    mot_de_passe = password_entry.get()
    
    try:
        
        mydb= connect_to_db()        
        mycursor = mydb.cursor()
        
        query = "SELECT * FROM access WHERE nom_user = %s AND mot_de_passe = %s"
        mycursor.execute(query, (nom_utilisateur, mot_de_passe))
        result = mycursor.fetchone()
        
        if result:
            print("Connexion réussie !")
            ouvrir_interface_principale()
        else:
            print("Identifiants incorrects.")
            
        mycursor.close()
        mydb.close()
        
    except mysql.connector.Error as err:
        print(f"Erreur de connexion à la base de données : {err}")

def load_image():
    global background_image
    image = Image.open("gestion-stock-commerce.png")
    background_image = ImageTk.PhotoImage(image)
    
    image_width = image.width
    image_height = image.height
    
    
    window_width = min(800, image_width + 100)
    window_height = min(600, image_height + 100)
    
    canvas.config(width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
    
    root.geometry(f"{window_width}x{window_height}")


root = tk.Tk()
root.title("StockMaster - Gestion de Stock")
app_name_label = tk.Label(root, text="StockMaster - Gestion de Stock", bg="#7D4FFE", fg="white", font=("Arial", 14))
app_name_label.pack(side="top", fill="x")

canvas = tk.Canvas(root)
canvas.pack()


login_frame = tk.Frame(root, bg='#7D4FFE', padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

username_label = tk.Label(login_frame, text="Nom d'utilisateur:", bg='#7D4FFE', fg="white")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Mot de passe:", bg='#7D4FFE', fg="white")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Se connecter", bg="#24D26D", fg="white",  command=verifier_identifiants)
login_button.grid(row=2, columnspan=2)
load_image()
footer = tk.Label(root, text="© Copyright 2024", relief=tk.GROOVE)
footer.pack(side=tk.BOTTOM, fill=tk.X)


root.mainloop()



