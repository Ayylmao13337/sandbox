#Oppgave 1)
print ('Oppgave 1')
import math

def pi(d=2):
    if d == 0:
        d = 2
    elif d < 0:
        return(f"input kan ikke være et negativt tall")
    
    if d > 16:
        print("Antall desimaler kan ikke være høyere enn 16.")
        return round(math.pi, 16)
    
    return round(math.pi, d)

print(pi(-2))

print()

#Oppgave 2)
print ('Oppgave 2')
def celsius_to_fahrenheit(temp):
    f = (temp*(9/5)+32)
    return (f'Det er {temp} celsius og i farnheight er det {f}')

print(celsius_to_fahrenheit(20))