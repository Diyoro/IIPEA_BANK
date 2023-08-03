import pandas as pd

def Consult_solde():
    nom_fichier = "base_de_donnees.xlsx"

    try:
        df = pd.read_excel(nom_fichier)

    except FileNotFoundError:
        # Si le fichier n'existe pas, créer un DataFrame vide
        df = pd.DataFrame()

    numero_compte = int(input("Entrez votre numéro de compte : "))

    if numero_compte in df['numero_compte'].values:
        # Trouver le nom_client correspondant au numéro de compte
        nom_client = df.loc[df['numero_compte'] == numero_compte, 'nom_client'].iloc[0]
        # Trouver le solde correspondant au numéro de compte
        solde = df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0]
        print(f"Nom du client : {nom_client}")
        print(f"Solde : {solde}")
    else:
        print("Numéro de compte inexistant")

Consult_solde()
