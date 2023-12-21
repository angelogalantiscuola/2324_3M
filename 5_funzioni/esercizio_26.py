from math import sqrt
def entrata() -> list[int]:
    a=int(input('Inserisci un numero:'))
    b=int(input('Inserisci un numero:'))
    c=int(input('Inserisci un numero:'))
    return [a,b,c]
def elaborazione(a:int,b:int,c:int)->list[float] | None:
    x1=0
    x2=0
    delta=b*b-4*a*c
    if delta<0:
        print("Delta è negativa,l'equazione è impossibile")
        x1=None
        x2=None
        return x1,x2
    elif delta==0:
        x1=-b/(2*a)
        x2=x1
        return x1,x2
    elif delta>0:
        x1=-b+sqrt(delta)/2*a
        x2=-b-sqrt(delta)/2*a
        return [x1,x2]
def uscita(x1:float|None,x2:float|None)-> None:
    if x1 is not None:
        if x1==x2:
            print(x1)
        else:
            print(x1)
            print(x2)

a,b,c=entrata()
x1,x2=elaborazione(a,b,c)
uscita(x1,x2)
