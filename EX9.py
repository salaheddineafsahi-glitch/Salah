A=input("taper une chaine: ")
S=""
for i in A :
    S=i.upper() + S
if S==A.upper() :
    print (f"{A} est un palindrome ")
else : 
    print("nond")