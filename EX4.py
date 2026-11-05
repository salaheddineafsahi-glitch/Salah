A=int(input("entrer  un entier :"))
S=0
for i in range(1,A-1) :
    if A%i==0 :
      S=S+i
if S==A :
   print("le nombre est parfait")
else :
   print("le nombre n'est pas parfait")