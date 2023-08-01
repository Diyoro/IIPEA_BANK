import pandas as pd

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


Retrait()