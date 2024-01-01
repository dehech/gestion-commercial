# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:40:44 2023

@author: ASUS
"""

#gestion_stock.py
import tkinter as tk
import mysql.connector

def deconnexion(root):
    root.destroy()  # Fermer la fenêtre de connexion
    import sign_in

def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="projet_python"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Erreur de connexion à la base de données : {err}")
        return None

def vendre_produit():
    # Logique pour la vente d'un produit
    print("Produit vendu !")

def ajouter_produit(database):
    def add_product():
     nom_produit = entry_nom_produit.get()
     description = entry_description.get()
     quantite = entry_quantite.get()
     prix_achat = entry_prix_achat.get()
     prix_vente = entry_prix_vente.get()

     try:
         cursor = database.cursor()
         cursor.execute("SELECT MAX(id_produit) + 1 FROM produit")
         next_id = cursor.fetchone()[0]  # Récupérer le résultat de la requête
         query = "INSERT INTO produit (id_produit, nom_produit, description, quantite, prix_achat, prix_vente) VALUES (%s, %s, %s, %s, %s, %s)"
         cursor.execute(query, (next_id, nom_produit, description, quantite, prix_achat, prix_vente))
         database.commit()
         print("Produit ajouté avec succès.")
     except mysql.connector.Error as err:
         print(f"Erreur lors de l'ajout du produit : {err}")

    root = tk.Tk()
    root.title("Ajout de Produit")

    label_nom = tk.Label(root, text="Nom du produit:")
    label_nom.pack()

    entry_nom_produit = tk.Entry(root)
    entry_nom_produit.pack()

    label_description = tk.Label(root, text="Description:")
    label_description.pack()

    entry_description = tk.Entry(root)
    entry_description.pack()

    label_quantite = tk.Label(root, text="Quantité:")
    label_quantite.pack()

    entry_quantite = tk.Entry(root)
    entry_quantite.pack()

    label_prix_achat = tk.Label(root, text="Prix d'achat:")
    label_prix_achat.pack()

    entry_prix_achat = tk.Entry(root)
    entry_prix_achat.pack()

    label_prix_vente = tk.Label(root, text="Prix de vente:")
    label_prix_vente.pack()

    entry_prix_vente = tk.Entry(root)
    entry_prix_vente.pack()

    btn_ajouter = tk.Button(root, text="Ajouter", command=add_product)
    btn_ajouter.pack()

    root.mainloop()
    
def lister_produits(database):
    try:
        cursor = database.cursor()
        cursor.execute("SELECT CONCAT('id: ', id_produit, ', nom: ', nom_produit, ', desc: ', description, ', Qte: ', quantite, ', prix_achat: ', prix_achat, ', prix_vente: ', prix_vente) AS infos_produit FROM produit;")
        result = cursor.fetchall()
        # Création de la fenêtre Tkinter
        root = tk.Tk()
        root.title("Liste des Produits")
       
        # Zone de texte pour afficher les produits
        text_area = tk.Text(root, height=10, width=80)
        text_area.pack()
       
        # Affichage de tous les produits dans la zone de texte
        for row in result:
           text_area.insert(tk.END, row[0] + "\n")  # Ajoute chaque produit dans une nouvelle ligne
       
        root.mainloop()
    except mysql.connector.Error as err:
       print(f"Erreur lors de la récupération des produits : {err}")


def chercher_produit(database):
    def rechercher():
        produit_recherche = entry_produit.get()
        try:
            cursor = database.cursor()
            query = f"SELECT CONCAT('id: ', id_produit, ', nom: ', nom_produit, ', desc: ', description, ', Qte: ', quantite, ', prix_achat: ', prix_achat, ', prix_vente: ', prix_vente) AS infos_produit FROM produit WHERE nom_produit LIKE '%{produit_recherche}%'"
            cursor.execute(query)
            result = cursor.fetchall()

            text_area.delete(1.0, tk.END)  # Efface le contenu précédent de la zone de texte

            # Affichage des résultats dans la zone de texte
            for row in result:
                text_area.insert(tk.END, row[0] + "\n")  # Ajoute chaque produit dans une nouvelle ligne
        except mysql.connector.Error as err:
            print(f"Erreur lors de la recherche de produit : {err}")

    root = tk.Tk()
    root.title("Recherche de Produit")

    label = tk.Label(root, text="Nom du Produit à rechercher:")
    label.pack()

    entry_produit = tk.Entry(root)
    entry_produit.pack()

    search_button = tk.Button(root, text="Rechercher", command=rechercher)
    search_button.pack()

    text_area = tk.Text(root, height=10, width=80)
    text_area.pack()

    root.mainloop()
    
def supprimer_produit(database):
    def delete_product():
        product_name = entry_nom_produit.get()
        try:
            cursor = database.cursor()
            query = "DELETE FROM produit WHERE nom_produit = %s"
            cursor.execute(query, (product_name,))
            database.commit()
            print("Produit supprimé avec succès.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la suppression du produit : {err}")

    root = tk.Tk()
    root.title("Suppression de Produit")

    label_nom = tk.Label(root, text="Nom du produit à supprimer:")
    label_nom.pack()

    entry_nom_produit = tk.Entry(root)
    entry_nom_produit.pack()

    btn_supprimer = tk.Button(root, text="Supprimer", command=delete_product)
    btn_supprimer.pack()

    root.mainloop()
    
def get_products(database):
    try:
        cursor = database.cursor()
        cursor.execute("SELECT id_produit, nom_produit, quantite FROM produit")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération des produits : {err}")
        return []

def update_quantity(database, product_id, new_quantity):
    try:
        cursor = database.cursor()
        query = "UPDATE produit SET quantite = %s WHERE id_produit = %s;"
        cursor.execute(query, (new_quantity, product_id))
        database.commit()
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour de la quantité : {err}")

def inventaire(database):
    def update():
        for product_id, entry in entries.items():
            product_id = row[0]
            new_quantity = entry.get()
            update_quantity(database, product_id, int(new_quantity))
    
    root = tk.Tk()
    root.title("Inventaire")

    products = get_products(database)

    rows = []
    entries = {}

    for i, product in enumerate(products):
        id_produit, nom_produit, quantite = product
        row = []

        label_id = tk.Label(root, text=f"ID: {id_produit}")
        label_id.grid(row=i, column=0)
        row.append(label_id)

        label_nom = tk.Label(root, text=f"Nom: {nom_produit}")
        label_nom.grid(row=i, column=1)
        row.append(label_nom)

        label_quantite = tk.Label(root, text="Quantité:")
        label_quantite.grid(row=i, column=2)
        row.append(label_quantite)

        entry_quantite = tk.Entry(root)
        entry_quantite.insert(tk.END, quantite)
        entry_quantite.grid(row=i, column=3)
        row.append(entry_quantite)

        rows.append(row)
        entries[id_produit] = entry_quantite

    update_button = tk.Button(root, text="Mettre à jour", command=update)
    update_button.grid(row=len(products), columnspan=4)

    root.mainloop()

def modifier_produit(database):
    def rechercher_produit():
        nom_produit = entry_nom_produit.get()
        try:
            cursor = database.cursor()
            query = "SELECT * FROM produit WHERE nom_produit = %s"
            cursor.execute(query, (nom_produit,))
            result = cursor.fetchone()

            if result:
                # Produit trouvé, afficher une page pour les modifications
                root_modif = tk.Tk()
                root_modif.title("Modifier Produit")

                # Créer des champs pour chaque attribut du produit
                labels = ["Nom du Produit:", "Description:", "Quantité:", "Prix Achat:", "Prix Vente:"]
                entries = []
                for i, label_text in enumerate(labels):
                    label = tk.Label(root_modif, text=label_text)
                    label.grid(row=i, column=0)
                    entry = tk.Entry(root_modif)
                    entry.insert(tk.END, result[i+1])  # Insérer la valeur de l'attribut correspondant
                    entry.grid(row=i, column=1)
                    entries.append(entry)

                def modifier():
                    new_values = [entry.get() for entry in entries]
                    update_product(database, result[0], new_values)

                btn_modifier = tk.Button(root_modif, text="Modifier", command=modifier)
                btn_modifier.grid(row=len(labels), columnspan=2)

                root_modif.mainloop()
            else:
                print("Produit non trouvé.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la recherche du produit : {err}")

    def update_product(database, product_id, new_values):
        try:
            cursor = database.cursor()
            query = "UPDATE produit SET nom_produit = %s, description = %s, quantite = %s, prix_achat = %s, prix_vente = %s WHERE id_produit = %s"
            cursor.execute(query, (*new_values, product_id))
            database.commit()
            print("Produit mis à jour avec succès !")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la mise à jour du produit : {err}")

    root = tk.Tk()
    root.title("Modifier Produit")

    label_nom_produit = tk.Label(root, text="Nom du Produit à Modifier:")
    label_nom_produit.pack()

    entry_nom_produit = tk.Entry(root)
    entry_nom_produit.pack()

    btn_rechercher = tk.Button(root, text="Rechercher", command=rechercher_produit)
    btn_rechercher.pack()

    root.mainloop()


def main_interface():
    root = tk.Tk()
    root.title("StockMaster - Gestion de Stock")
    app_name_label = tk.Label(root, text="StockMaster - Gestion de Stock", bg="#7D4FFE", fg="white", font=("Arial", 14))
    app_name_label.pack(side="top", fill="x")
    root.geometry('800x600')
    root.configure(bg='#7D4FFE')

    btn_vendre = tk.Button(root, text="Vendre un produit", command=vendre_produit)
    btn_vendre.pack(pady=10)

    btn_ajouter = tk.Button(root, text="Ajouter un produit", command=lambda:ajouter_produit(database))
    btn_ajouter.pack(pady=10)

    btn_lister = tk.Button(root, text="Lister tous les produits", command=lambda:lister_produits(database))
    btn_lister.pack(pady=10)

    btn_chercher = tk.Button(root, text="Chercher un produit", command= lambda:chercher_produit(database))
    btn_chercher.pack(pady=10)

    btn_inventaire = tk.Button(root, text="Inventaire", command=lambda:inventaire(database))
    btn_inventaire.pack(pady=10)
    
    btn_supprimer = tk.Button(root, text="supprimer produit", command=lambda:supprimer_produit(database))
    btn_supprimer.pack(pady=10)
    
    btn_modifier = tk.Button(root, text="modifier produit", command=lambda:modifier_produit(database))
    btn_modifier.pack(pady=10)
    
    btn_deconnexion = tk.Button(root, text="Déconnexion", command=lambda:deconnexion(root))
    btn_deconnexion.pack(anchor="nw", side="right", pady=5)  # Positionnement en haut à droite

    root.resizable(True, True)
    database = connect_to_database()
    root.mainloop()

# Lancer l'interface principale
main_interface()