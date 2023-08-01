import pandas as pd
import random
import openpyxl

def Creation_compte():


    nom_fichier = "base_de_donnees.xlsx"

    try:
        df_exist = pd.read_excel(nom_fichier)
    except FileExistsError :
        df_exist = pd.DataFrame()

    # Création de liste pour stocker les informations 
    personnes_liste = []

    nom = input("Entrez votre nom : ")

    prenom = input("Entrez votre prenom : ")

    date_naissance = input("Entrez votre date de naissance (Format JJ/MM/AAAA) : ")

    telephone = input("Entrez votre numéro de téléphone : ")

    # Calcul de l'âge 

    jour, mois, annee = map(int, date_naissance.split('/'))
    aujourdhui = pd.Timestamp.now()
    date_naissance = pd.Timestamp(annee, mois, jour)
    age = (aujourdhui - date_naissance).days // 365

    numero_compte = random.randint(10000, 99999)

    # Création de DataFrame 

    personne = {
        'numero_compte' : numero_compte,
        'nom' : nom,
        'prenom' : prenom,
        'age' : age,
        'telephone' : telephone,
        'solde' : 0,
    }

    personnes_liste.append(personne)
    df_new = pd.DataFrame(personnes_liste)

    df_final = pd.concat([df_exist, df_new], ignore_index=True)

    # Enregistrement dans le fichier excel
    nom_fichier = "base_de_donnees.xlsx"
    df_final.to_excel(nom_fichier, index=False)

    print("Client ", nom,"votre numéro de compte est", numero_compte)


Creation_compte()