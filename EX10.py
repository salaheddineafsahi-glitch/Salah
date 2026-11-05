A=(input("saisir la valeur de a :"))
S=0
for i in A :
    X=int(A)
    P=1
    for C in  range(1,X+1) :
        P=P*C
    S=P+S
        
if int(A)==S:
    print("il est égal à la somme des factorielles de ses chiffres")
else :
    print("non")

