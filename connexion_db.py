import mysql.connector


def connect_to_db():
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