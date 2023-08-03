import pandas as pd 

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

Suppression()