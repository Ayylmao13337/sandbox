def valuttakonvert(Penger):
    dollar = Penger / 11.62
    euro = Penger / 10.2
    print(f"{Penger} norske kroner tilsvarer {round(euro, 2)} € og {round(dollar, 2)} $")

valuttakonvert(250)
