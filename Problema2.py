t=0
gr=0
nsuma=0
g=0
suma=0
nr=0
while t<12:
    g=eval(input("Temp medie= "))
    if g>=0:
        suma=suma+g
        nr+=1
    elif g<0:
        nsuma=g+nsuma
        gr+=1
 
    t=t+1
a=suma/nr
b=nsuma/gr
print(round(a,2))
print(round(b,2))