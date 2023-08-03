import pandas as pd

def Transfert():

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

          print("Le transfert a été éffectuer avec succès. Votre nouveau solde est ", df.loc[df['numero_compte'] == numero_compte, 'solde'].iloc[0])

        else:
            print("Le numéro de compte n'existe pas ")

    else:
        print("Le numéro de compte n'existe pas ")


Transfert()

