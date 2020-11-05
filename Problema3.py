a=0
b=0
x=0
s=0
while a==0 or b!=0:
    x=eval(input("Dati cifra:"))
    a=x%2
    b=x%3
    if a==0:
        s=s+x
print(s)