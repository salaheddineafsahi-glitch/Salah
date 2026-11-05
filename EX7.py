<<<<<<< HEAD
A=input("taper les lettres miniscules :")
S=""
for i in  A :
    S= S + i.upper()
print ("les lettres en majuscules est:" ,S)
=======
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
>>>>>>> df32e25d54a1725d0e4e1c40a2b0d54fc538d8e7
