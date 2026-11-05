
C=int(input("saisir la valeur d'entier N :"))
while C<=0 :
  print("donner un nombre positive")
  C=int(input("saisir la valeur d'entier N"))
S=0 
for i  in range (1,1+C) :
  S=S+1/i 
  print("la somme est:", S)

a=float(input("saisir la longueur de rectangle:" ))
b=float(input("saisie la largeur de rectangle:"))
if a==b :
    print("c'est un carrè")
else :
    print("c'est un rectangle non carrè")

