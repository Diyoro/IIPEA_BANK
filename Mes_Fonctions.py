import pandas as pd

  # Charger le fichier Excel
nom_fichier = "base_de_donnees.xlsx"

try:
     df_exist = pd.read_excel(nom_fichier)

except FileNotFoundError:
        # Si le fichier n'existe pas, créer un DataFrame vide
    df_exist = pd.DataFrame()

def numero_compte_existe(deja_existant, numero_compte):

        return numero_compte in deja_existant['numero_compte'].values

while True:
    numero_compte = int(input("Entrez votre numéro de compte"))

    if numero_compte_existe(df_exist, numero_compte):
        montant = int(input("Entrez le montant à déposer : "))

        solde = solde + montant

        print("Votre nouveau solde est", solde)

    else:
        print("Le numéro de compte n'existe pas ")
