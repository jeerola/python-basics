tyylipisteet = [] # Lista tuomareiden pisteille

hypynPituus = float(input("Hypyn pituus: "))
for i in range(5):
    pisteet = float(input(f"Tuomarin {i + 1} pisteet: "))
    tyylipisteet.append(pisteet) # Lisätään pisteet listaan

yhteispisteet = sum(tyylipisteet) + 0.9 * hypynPituus # Lasketaan yhteispisteet
print(f"Hypyn pituus: {hypynPituus} metriä")
print(f"Tyylipisteet: {tyylipisteet}")
print(f"Yhteispisteet: {round(yhteispisteet, 2)}") # Pyöristetään pisteet kahden desimaalin tarkkuudella