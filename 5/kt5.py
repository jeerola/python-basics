def muunnaLampotila(asteet, mista, mihin):
    if mista == 'f' and mihin == 'c': # Fahrenheit --> Celsius
        return (asteet - 32) * 5/9
    elif mista == 'c' and mihin == 'f': # Celsius --> Fahrenheit
        return asteet * 9/5 + 32
    elif mista == 'k' and mihin == 'c': # Kelvin --> Celsius
        return asteet - 273
    elif mista == 'c' and mihin == 'k': # Celsius --> Kelvin
        return asteet + 273
    elif mista == 'k' and mihin == 'f': # Kelvin --> Fahrenheit
        return (asteet - 273) * 9/5 + 32
    elif mista == 'f' and mihin == 'k': # Fahrenheit --> Kelvin
        return (asteet - 32) * 5/9 + 273
    elif mista == mihin:
        return asteet  # Jos sama asteikko, ei muutosta
    else:
        return None # Tuntematon käyttäjäsyöte


mista = input("Mistä asteikosta muunnetaan? (C/F/K) ")
mihin = input("Mihin asteikoon? (C/F/K) ")
asteet = int(input("Asteet: "))

tulos = muunnaLampotila(asteet, mista, mihin)

if tulos is not None:
    print(f'{asteet} astetta {mista} on {tulos} astetta {mihin}.') # Muunnettu tulos
else:
    print("Muunnettaessa tapahtui virhe.") # Virheellinen syöte
