#Elaborați un program care va calcula suma, 
#produsul și media aritmetică a numerelor de la 1 la n, 
#pentru n introdus de la tastatură.
n=eval(input("Introduceti numarul:"))
i=1
suma=0
produs=1
while i<=n:
    suma+=i
    produs*=i
    i+=1

m_a=suma/n
print("Suma numerelor este:", suma)
print("Produsul numerelor este:", produs)
print("Media aritmetica a numerelor este:", m_a)