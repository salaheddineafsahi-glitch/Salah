A=int(input("saisir la valeur de A :"))
B = int(input("Saisir la valeur de B : "))

if A<=0 or B<=0 :
    print("error")
elif A%B==0 :
    print(A," est divisible par" ,B )
else :
    print(A, "n'est pas divisible par", B)
    