entier=int( input("saisir le nombre de jour :"))
if 0<= entier <= 6 :
    if entier==0 :
        print ("le jour est dimanche")
    elif entier==1 :
        print("le jour est lundi")
    elif entier==2 :
        print("le jour est mardi")
    elif entier ==3 :
        print("le jour est mercredi")
    elif entier == 4 :
        print("le jeur esr jeudi")
    elif entier ==5 :
        print("le jour est vendredi")
    else :
        print ("le jour est samedi")
else:
    print("ERROR")