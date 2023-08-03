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

    class Colors:
        RESET = '\033[0m'
        GREEN = '\033[32m'

    print(f"{Colors.BLUE}Client ", nom,"votre numéro de compte est", numero_compte)




def Depot():
    #Charger le fichier Excel
    nom_fichier = "base_de_donnees.xlsx"

    try:
        df = pd.read_excel(nom_fichier)

    except FileNotFoundError:
        #Si le fichier n'existe pas, créer un DataFrame vide
        df = pd.DataFrame()

    numero_compte = int(input("Entrez votre numéro de compte : "))

    class Colors:
        GREEN = '\033[32m'
        RED = '\033[31m'

    #Vérifie si le numéro de compte existe

    if numero_compte in df['numero_compte'].values:

        montant = float(input("Entrez le montant à déposer : "))

        #Mise à jour du solde 

        df.loc[df['numero_compte'] == numero_compte, 'solde'] += montant

        #Enregistrer les informations dans le fichier excel

        df.to_excel(nom_fichier, index=False)

        print(f"{Colors.GREEN}Le montant a été déposé avec succès. Votre nouveau solde est ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

    else:
        print(f"{Colors.RED}Compte introuvable")



def Retrait():

    class Colors:
        RESET = '\033[0m'
        GREEN = '\033[32m'
        RED = '\033[31m'
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

        if montant < df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0] :

        #Mise à jour du solde 

            df.loc[df['numero_compte'] == numero_compte, 'solde'] -= montant

                    #Enregistrer les informations dans le fichier excel

            df.to_excel(nom_fichier, index=False)

            print(f"{Colors.GREEN}Retrait éffectuer avec succès. Votre nouveau solde est ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

        else :
            print(f"{Colors.RED}Solde insuffisant !") 



    else:
        print(f"{Colors.RED}Compte introuvable")



def Transfert():

    class Colors:
        RESET = '\033[0m'
        GREEN = '\033[32m'
        RED = '\033[31m'

    nom_fichier = "base_de_donnees.xlsx"

    try:
        df = pd.read_excel(nom_fichier)

    except FileNotFoundError:
        #Si le fichier n'existe pas, créer un DataFrame vide
        df = pd.DataFrame()

    numero_compte = int(input("Entrez votre numéro de compte : "))


    if numero_compte in df['numero_compte'].values:

        numero_compte_ben = int(input("Entrez le numéro de compte du bénéficiaire : "))

        if numero_compte_ben in df['numero_compte'].values:

          montant_trans = float(input("Entrez le montant à transférer : "))  

          #Mise à jour des soldes 

          df.loc[df['numero_compte'] == numero_compte_ben, 'solde'] += montant_trans

          df.loc[df['numero_compte'] == numero_compte, 'solde'] -= montant_trans

          # Enregistrement des informations dans le fichier excel

          df.to_excel(nom_fichier, index=False)

          print(f"{Colors.GREEN}Le transfert a été éffectuer avec succès. Votre nouveau solde est ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

        else:
            print(f"{Colors.RED}Le numéro de compte n'existe pas ")

    else:
        print(f"{Colors.RED}Le numéro de compte n'existe pas ")


def Consult_solde():

    class Colors:
        RED = '\033[31m'

    nom_fichier = "base_de_donnees.xlsx"

    try:
        df = pd.read_excel(nom_fichier)

    except FileNotFoundError:
        #Si le fichier n'existe pas, créer un DataFrame vide
        df = pd.DataFrame()

    numero_compte = int(input("Entrez votre numéro de compte : "))

    if numero_compte in df['numero_compte'].values:

        print("Solde : ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

    else:
        print(f"{Colors.RED}Numéro de compte inexistant")


def Suppression():

    nom_fichier = "base_de_donnees.xlsx"

    df = pd.read_excel(nom_fichier)

    numero_compte = int(input("Entrez le numéro de compte du compte à supprimer : "))

    if numero_compte in df['numero_compte'].values:

        class Colors:
            RESET = '\033[0m'
            RED = '\033[31m'

        choix = input(f"{Colors.RED}Voulez vous vraiment supprimer votre compte ? o -> Oui / n -> Non :{Colors.RESET} ")

        if choix == "o" :

            #Suppression de la ligne avec le numéro de compte
            df = df[df['numero_compte'] != numero_compte]

            # Mise à jour du fichier excel 
            df.to_excel(nom_fichier, index=False)

            print("Compte supprimé avec succès ")

        elif choix == "n" :
            print("Compte toujours actif")
            

        else:
            print("Choix invalide")

    else:
        print("Numéro de compte inexistant")
















while True :

    class Colors:
        RESET = '\033[0m'
        YELLOW = '\033[33m'

    print(f"\n {Colors.YELLOW}---|  BIENVENU A IIPEA BANK  |---{Colors.RESET}")
    print("--------------------------------------------|")
    print("Quelle opération souhaitez vous éffectuer ?")
    print("--------------------------------------------|")
    print("-> 1 pour la création d'un compte")
    print("--------------------------------------------|")
    print("-> 2 pour déposer de l'argent")
    print("--------------------------------------------|")
    print("-> 3 pour retirer de l'argent")
    print("--------------------------------------------|")
    print("-> 4 pour transférer de l'argent")
    print("--------------------------------------------|")
    print("-> 5 pour consulter votre solde")
    print("--------------------------------------------|")
    print("-> 6 pour la ferméture de votre compte ")
    print("--------------------------------------------|")
    print("-> 0 pour arreter le programme")
    print("--------------------------------------------|")


    choix = input("Entrez votre choix : ")

    if choix == "1":
        Creation_compte()

    elif choix == "2":
        Depot()

    elif choix == "3":
        Retrait()

    elif choix == "4":
        Transfert()

    elif choix == "5":
        Consult_solde()

    elif choix == "6":
        Suppression()

    elif choix == "0":
        class Colors:
            RESET = '\033[0m'
            RED = '\033[31m'

        print("\n--------------------------------------------|")
        choixxx = input(f"{Colors.RED}Voulez-vous vraiment arrêter le programme ? o/n : {Colors.RESET}")
        if choixxx == "o":
            print("\n--------------------------------------------|")
            print("Merci à bientot (*_*) ")
            print("--------------------------------------------|")
            break
        elif choixxx == "n":
            print("")
        else:
            print("Choix invalide ")


    else:
        print("\n--------------------------------------------|")
        print("Opération invalide (-_-) ")
        print("--------------------------------------------|")






