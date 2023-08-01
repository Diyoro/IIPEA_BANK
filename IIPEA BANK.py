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




def Depot():
    #Charger le fichier Excel
    nom_fichier = "base_de_donnees.xlsx"

    try:
        df = pd.read_excel(nom_fichier)

    except FileNotFoundError:
        #Si le fichier n'existe pas, créer un DataFrame vide
        df = pd.DataFrame()

    numero_compte = int(input("Entrez votre numéro de compte : "))

    #Vérifie si le numéro de compte existe

    if numero_compte in df['numero_compte'].values:

        montant = float(input("Entrez le montant à déposer : "))

        #Mise à jour du solde 

        df.loc[df['numero_compte'] == numero_compte, 'solde'] += montant

        #Enregistrer les informations dans le fichier excel

        df.to_excel(nom_fichier, index=False)

        print("Le montant a été déposé avec succès. Votre nouveau solde est ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

    else:
        print("Compte introuvable")



def Retrait():
    #Charger le fichier Excel
    nom_fichier = "base_de_donnees.xlsx"

    try:
        df = pd.read_excel(nom_fichier)

    except FileNotFoundError:
        #Si le fichier n'existe pas, créer un DataFrame vide
        df = pd.DataFrame()

    numero_compte = int(input("Entrez votre numéro de compte : "))

    #Vérifie si le numéro de compte existe

    if numero_compte in df['numero_compte'].values:

        montant = float(input("Entrez le montant à retirer : "))

        #Mise à jour du solde 

        df.loc[df['numero_compte'] == numero_compte, 'solde'] -= montant

        #Enregistrer les informations dans le fichier excel

        df.to_excel(nom_fichier, index=False)

        print("Retrait éffectuer avec succès. Votre nouveau solde est ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

    else:
        print("Compte introuvable")






















while True :

    print("\n ---|  BIENVENU A IIPEA BANK  |---")
    print("--------------------------------------------")
    print("Quelle opération souhaitez vous éffectuer ?")
    print("--------------------------------------------")
    print("-> 1 pour la création d'un compte")
    print("--------------------------------------------")
    print("-> 2 pour déposer de l'argent")
    print("--------------------------------------------")
    print("-> 3 pour retirer de l'argent")
    print("--------------------------------------------")
    print("-> 4 pour transférer de l'argent")
    print("--------------------------------------------")
    print("-> 5 pour consulter votre solde")
    print("--------------------------------------------")
    print("-> 6 pour la ferméture de votre compte ")
    print("--------------------------------------------")
    print("-> 0 pour arreter le programme")
    print("--------------------------------------------")


    choix = input("Entrez votre choix : ")

    if choix == "1":
        Creation_compte()

    elif choix == "2":
        Depot()

    elif choix == "3":
        Retrait()

    elif choix == "4":
        pass

    elif choix == "5":
        pass

    elif choix == "6":
        pass

    elif choix == "0":
        print("\n--------------------------------------------")
        print("Merci à bientot (*-*) ")
        print("--------------------------------------------")
        break

    else:
        print("\n--------------------------------------------")
        print("Opération invalide")
        print("--------------------------------------------")






