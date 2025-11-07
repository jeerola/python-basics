pisteet = 0 # Alustetaan pistelaskuri

# Luetaan tiedoston rivit ja poistetaan tyhjät
with open('/Users/jaakko/Documents/GitHub/python-basics/8/kysymykset.txt', 'r', encoding='utf-8') as f:
    rivit = [r.strip() for r in f if r.strip() != ""]

i = 0 # Indeksi rivien läpikäyntiin
kysymys_numero = 1 # Kysymysnumero

while i < len(rivit): # Käydään rivit läpi kysymys kerrallaan
    print(f"\n{kysymys_numero}. {rivit[i]}")
    i += 1 # Siirrytään seuraavalle riville

    # Tulostetaan vastausvaihtoehdot ja tallennetaan ne listaan
    vaihtoehdot = [] # Alustetaan lista sallituista vastausvaihtoehdoista
    kirjain = ord('a') # ASCII-arvo kirjaimelle 'a'
    while i < len(rivit) and len(rivit[i]) > 1:
        merkki = chr(kirjain) # Muutetaan ASCII-arvo kirjaimeksi
        print(f" {merkki}) {rivit[i]}")
        vaihtoehdot.append(merkki) # Lisätään kirjain sallittuihin vaihtoehtoihin
        kirjain += 1 # Seuraava kirjain
        i += 1 # Seuraava rivi

    oikea = rivit[i].lower()

    # Kysytään vastaus ja toistetaan jos vastaus on virheellinen
    while True:
        vastaus = input("Vastaus: ").lower()

        if vastaus == "":
            print("Tyhjää vastausta ei hyväksytä.\n")
        elif vastaus not in vaihtoehdot: # Tarkistetaan onko vastaus lisätty listaan vaihtoehdoista
            print(f"Vastaus {vastaus} ei ole sallittu.\n")
        else:
            break  # Hyväksytään vastaus, poistutaan silmukasta

    if vastaus == oikea:
        print("Oikein!\n")
        pisteet += 1
    else:
        print(f"Väärin! Oikea vastaus on {oikea}.\n")

    kysymys_numero += 1 # Kasvatetaan kysymysnumeroa
    i += 1 # Siirrytään seuraavalle riville (seuraava kysymys)

print(f"Sait [{pisteet}/{kysymys_numero - 1}] pistettä.")
