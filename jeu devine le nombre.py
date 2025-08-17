
import random
import time


def affiche(phrase):
   mots = phrase.split(' ')
   for mot in mots:
     print (mot,end=' ',flush = True)
     time.sleep (0.3)
   print ()

def devine():
   mist = random.randint(0,100)
   num = int(input("Entrez un nombre entre 0 et 100: "))
   time.sleep(1)
   i = 1
   while i <= 9:
     if num == mist :
       i = 11
       affiche (f"Bravo vous avez trouvez               le nombre {mist}.")                                                                      time.sleep(1)
     elif num != mist:
       if num > mist:                                                                                                          affiche ("Trop grand !")
         time.sleep(1)                                                                                                         num = int(input("Essayer un autre nombre: "))
         time.sleep(1)
       elif num < mist:
         affiche ("Trop petit !")
         time.sleep(1)
         num = int(input("Essayer un autre nombre: "))
         time.sleep(1)
       i += 1
       if  i == 10:
         affiche("Vous avez atteint 10 essais")
         time.sleep(1)
         affiche("Game Over")
   suite = input("Voulez vous rejouer [oui/non]?")
   if suite == "oui":
     time.sleep(1)
     affiche ("Nouvelle partie")
     time.sleep(1)
     devine ()
   elif suite == "non":
       affiche("Merci d'avoir participer n'hésitez pas à rejouer")

affiche("Salutation jeune joueur,ce jeu consiste à deviner un nombre entre 0 et 100 de manière aléatoire")
time.sleep(1)
affiche("Pour ce faire vous avez droit à 10 essais pour trouver ce nombre")
time.sleep(1)
affiche("Sur ce bonne chance")
time.sleep(1)
devine ()