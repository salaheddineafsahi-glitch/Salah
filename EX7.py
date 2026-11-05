A1=input("saisir le nom de premier personne:")
A=float(input("saisir l'age de premier personne:"))
B1=input("saisir le nom de deuxieme personne:")
B=float(input("saisir l'age de deuxieme personne"))
C1=input("saisir le nom de troiseieme personne:")
C=float(input("saisir l'age de troiseime personnes"))
if B<A and C<A :
    print("le personne le plus ageè est :",A1)
elif C<B and A<B :
    print("le personne le plus ageè est:",B1)
else:
    print("le personne le plus ageè est:",C1)