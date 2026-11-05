C=int(input("saisir la valeur d'entier N :"))
while C<=0 :
  print("donner un nombre positive")
  C=int(input("saisir la valeur d'entier N"))
S=0 
for i  in range (1,1+C) :
  S=S+1/i 
  print("la somme est:", S)
