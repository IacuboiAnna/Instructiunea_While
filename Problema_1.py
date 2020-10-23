#Se introduc succesiv numere nenule până la introducerea numărului 0. 
#Să se afişeze suma tuturor numerelor introduse. 
#Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
nr=eval(input("Introduceti un numar:"))
nr!=0
suma=0
while nr!=0 :
    suma+=nr
    nr=eval(input("Introduceti un numar:"))

print("Suma este:", suma)