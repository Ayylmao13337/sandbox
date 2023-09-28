#A)
def valuttakonvert(Penger):
    dollar = Penger/11.62
    euro = Penger/10.2
    return f"{Penger} norske kroner tilsvarer {round(euro,2)} Euro og {round(dollar,2)} Dollar"

print(valuttakonvert(250))
print()


#B)
euro_sign = "\N{euro sign}"
dollar_sign = "\N{dollar sign}"

def valuttakonvert(Penger):
    dollar = Penger/11.62
    euro = Penger/10.2
    return f"{Penger} norske kroner tilsvarer {round(euro,2)}{euro_sign} og {round(dollar,2)}{dollar_sign}"
    


print(valuttakonvert(250))     