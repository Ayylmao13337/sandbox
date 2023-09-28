5
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

print(pi())

print()

#Oppgave 2)
print ('Oppgave 2')
def celsius_to_fahrenheit(temp):
   f = (temp*9/5)+32
   return (f'Det er {temp} celsius og fahrenheit er {f}')

print(celsius_to_fahrenheit(10))

print()

#Oppgave 3a)
print ('Oppgave 3a')
saldo = 500
rentesats = 0.01

def innskudd(beløp):
    global saldo
    saldo += beløp

def uttak(beløp):
    global saldo
    saldo -= beløp if beløp <= saldo else print("Ikke nok penger på konto.")

def beregn_rente():
    global rentesats
    return saldo * (0.02 if saldo > 1000000 else 0.01)

def årlig_renteoppgjør():
    global saldo
    rente = beregn_rente()
    saldo += rente
    return rente

innskudd(1000000)
uttak(10)
print("Saldo:", saldo)
rente = årlig_renteoppgjør()
print("Årlig renteoppgjør:", rente)
print("Ny saldo etter renteoppgjør:", saldo)


print()

#Oppgave 3b)
print ('Oppgave 3b')
saldo = 500
rentesats = 0.01

def innskudd(beløp):
    global saldo
    saldo += beløp

def uttak(beløp):
    global saldo
    saldo -= beløp if beløp <= saldo else print("Ikke nok penger på konto.")

def beregn_rente():
    global rentesats
    return saldo * (0.02 if saldo > 1000000 else 0.01)

def årlig_renteoppgjør():
    global saldo
    rente = beregn_rente()
    saldo += rente
    return rente

def velg():
    i = 0
    while i < 1:
        print("1. Vis saldo")
        print("2. Innskudd")
        print("3. Uttak")
        print("4. Renteoppgjør")
        print("5. Avslutt")

        valg = input("Skriv inn valg (1/2/3/4/5): ")
        
        while i <= 1:
            if valg == '1':
                print("Saldo:", saldo)
                print()
                break 
            elif valg == '2':
                beløp = float(input("Skriv inn beløp for innskudd: "))
                innskudd(beløp)
                print("Innskudd på", beløp, "kroner er gjennomført.")
                print()
                break
            elif valg == '3':
                beløp = float(input("Skriv inn beløp for uttak: "))
                uttak(beløp)
                print()
                break
            elif valg == '4':
                rente = årlig_renteoppgjør()
                print("Årlig renteoppgjør på", rente, "kroner er gjennomført.")
                print()
                break
            elif valg == '5':
                i += 1
                print()
                break
            else:
                print("Ugyldig valg. Prøv igjen.")
                (print)
                break
            
            
        
velg()

print()

#Oppgave 3c)
print ('Oppgave 3c')
saldo = 500
rentesats = 0.01
saldoendringer = []

def innskudd(beløp):
    global saldo
    saldo += beløp
    saldoendringer.append(saldo)

def uttak(beløp):
    global saldo
    saldo -= beløp if beløp <= saldo else print("Ikke nok penger på konto.")
    saldoendringer.append(saldo)

def beregn_rente():
    global rentesats
    return saldo * (0.02 if saldo > 1000000 else 0.01)

def årlig_renteoppgjør():
    global saldo
    rente = beregn_rente()
    saldo += rente
    saldoendringer.append(saldo)
    return rente

def vis_siste_endringer():
    if len(saldoendringer) >= 3:
        print("Siste tre saldoendringer:")
        for i in range(-1, -4, -1):
            print(saldoendringer[i])
    else:
        print("Ikke nok saldoendringer tilgjengelig.")

def velg():
    i = 0
    while i < 1:
        print("1. Vis saldo")
        print("2. Innskudd")
        print("3. Uttak")
        print("4. Renteoppgjør")
        print("5. Vis siste tre saldoendringer")
        print("6. Avslutt")

        valg = input("Skriv inn valg (1/2/3/4/5/6): ")
    
        while i < 1:
            if valg == '1':
                print("Saldo:", saldo)
                print()
                break
            elif valg == '2':
                beløp = float(input("Skriv inn beløp for innskudd: "))
                innskudd(beløp)
                print()
                break
            elif valg == '3':
                uttak(float(input("Skriv inn beløp for uttak: ")))
                print()
                break
            elif valg == '4':
                rente = årlig_renteoppgjør()
                print("Årlig renteoppgjør på", rente, "kroner er gjennomført.")
                print()
                break
            elif valg == '5':
                vis_siste_endringer()
                print()
                break
            elif valg == '6':
                print("Avslutt") 
                i += 1
                break
            else:
                return("Ikke gyldig.")
    
    
velg()
print()

#Oppgave 4)
print ('Oppgave 4')
import random

def tre_tilfeldige_sifre():
    siffer1 = random.randint(1, 9)
    siffer2 = random.randint(1, 9)
    siffer3 = random.randint(1, 9)

    min_siffer = min(siffer1, siffer2, siffer3)
    max_siffer = max(siffer1, siffer2, siffer3)

    tallet = int(f"{min_siffer}{siffer1 + siffer2 + siffer3 - min_siffer - max_siffer}{max_siffer}")

    return print(f"Generert tall er: {tallet}")

tre_tilfeldige_sifre()



