import time

def afficher_phrase(phrase):
    mots = phrase.split(' ')
    for mot in mots:
        print(mot, end=' ', flush=True)
        time.sleep(0.2)
    print()

afficher_phrase("Salut, je suis Axsenk votre bot préféré ")
time.sleep(1)
afficher_phrase("Il est important de connaître son Indice de Masse Coorporelle pour veiller à sa santé")
time.sleep(1)
afficher_phrase("Je suis disposé à vous aidez avec cela. Pour ce faire j'aurai besoin de vos informations personnelles")
time.sleep(1.5)
Masse = float(input("Entrez votre masse en Kg: "))
time.sleep(1)
Taille = float(input("Entrez votre taille m: "))

if Masse <= 0 or Taille <= 0:
    afficher_phrase("Donnée non valides veuillez réitérer votre saisie en veillant à la validité des données éditées")


elif Masse > 0 and Taille > 0:
    BMI = Masse / (Taille * Taille)
    Categorie = "masse"
    if BMI < 18.5:
        Categorie = "Vous êtes en sous-poids nourisser vous bien"
    elif BMI >= 18.5 and BMI <= 24.9:
        Categorie = "Votre IMC est normal vous êtes en bonne santé"
    elif BMI >= 25 and BMI <= 29.9:
        Categorie = "Sur-poids commencer à surveiller votre alimentation vous franchissez la ligne rouge"
    else:
        Categorie = "Vous êtes obèse veuiller suivre un régime accompagner d'un rigoureux programme sportif"
    time.sleep(1)
    afficher_phrase(f"Indice de masse coorporelle: {BMI:.2f}")
    time.sleep(1)
    afficher_phrase(Categorie)
    time.sleep(1)
    suite=input("Voulez vous connaître la tranche de masse convenable pour vous? [s/n] ")
    if suite == "s":
        mi=int(18.5*(Taille2))
        ma=int(24.9*(Taille2))
        time.sleep(1)
        afficher_phrase(f"Votre masse est optimale entre {mi}Kg et {ma}Kg.")
        time.sleep(1.5)
    afficher_phrase("Merci de votre attention!")
