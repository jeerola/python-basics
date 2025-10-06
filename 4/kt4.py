tyylipisteet = [] # Lista tuomareiden pisteille
tuomareidenMäärä = 5 # Tuomareiden määrä

hypynPituus = float(input("Hypyn pituus: "))
while tuomareidenMäärä > 0:
    pisteet = float(input(f"Tuomarin {6 - tuomareidenMäärä} pisteet: "))
    tyylipisteet.append(pisteet) # Lisätään pisteet listaan
    tuomareidenMäärä -= 1

yhteispisteet = sum(tyylipisteet) + 0.9 * hypynPituus
print(f"Hypyn pituus: {hypynPituus} metriä")
print(f"Tyylipisteet: {tyylipisteet}")
print(f"Yhteispisteet: {round(yhteispisteet, 2)}") # Muotoillaan pisteet kahden desimaalin tarkkuudella