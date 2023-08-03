import pandas as pd

def Consult_solde():

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
        print("Numéro de compte inexistant")

Consult_solde()