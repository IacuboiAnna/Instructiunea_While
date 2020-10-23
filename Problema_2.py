#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
#Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
#Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  
#Date de ieşire  medie_poz=13.66  medie_neg=-3.33.
t=0
nr_p=0
nr_n=0
suma_p=0
suma_n=0
nr_luna=1
while nr_luna<=12 :
    t=int(input("Dati temperatura:"))
    if t>=0:
        suma_p+=t
        nr_p+=1
    if t<0:
        suma_n+=t
        nr_n+=1
    nr_luna+=1

medie_poz=suma_p/nr_p
medie_neg=suma_n/nr_n
print(round(medie_poz,2))
print(round(medie_neg,2))