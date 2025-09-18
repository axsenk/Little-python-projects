#Definition d'une fonction parite 
def parite ():
    #Definition et entrer de variable
    number = input ("Veuillez entrer un nombre entier pour en connaître la parité:" )
    while True:
        try:
               number =  int(number)
               break
        except ValueError :
                print ("Assurer vous d'entrer une valeur correcte.")
                parite()
                break
    if number < 0 :
         print ("Entrer un nombre entier.")
    elif number % 2 == 0:
                   print (f"Le nombre {number} est pair.")
    elif  number % 2 != 0:
                       print (f"Le nombre {number} est impair.")
                 
        
               
     #Possibilité d'entrer un autre nombre
    choix = input("Voulez vous essayer à nouveau? [oui/non] ")
    if choix.lower() == "oui" :
        parite ()
    else :
        print ("Bonne continuation!!!")



#Exécution de la fonction predefinie
parite ()