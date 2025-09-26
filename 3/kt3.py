kilometrit = int(input('Autolla ajettava vuotuinen kilometrimäärä: '))
bensaHinta = float(input('Bensiinin litrahinta euroina: '))
dieselHinta = float(input('Dieselöljyn litrahinta euroina: '))
bensaKulutus = float(input('Bensiinimoottorisen auton kulutus (litraa / 100 km): ')) / 100 # Jaetaan kulutus vastaamaan yhden kilometrin kulutusta laskemisen toimimiseksi
dieselKulutus = float(input('Dieselmoottorisen auton kulutus (litraa / 100 km): ')) / 100 # Jaetaan kulutus vastaamaan yhden kilometrin kulutusta laskemisen toimimiseksi

# Käytetään keskiarvollista henkilöauton veromäärää: 5.5 snt per 100 kg per päivä, 1980 kg painava auto
käyttövoimaVero = 0.055 * 19.8 * 365

bensaKulut = (kilometrit * bensaKulutus * bensaHinta)
dieselKulut = (kilometrit * dieselKulutus * dieselHinta + käyttövoimaVero)

if bensaKulut < dieselKulut:
    print(f'Bensalla ajo on halvempaa. Vuotuiset kustannukset ovat: {bensaKulut:.2f}€. Bensiinillä ajaminen on {dieselKulut - bensaKulut:.2f}€ edullisempaa vuodessa.')
elif dieselKulut < bensaKulut:
    print(f'Dieselillä ajo on halvempaa. Vuotuiset kustannukset ovat: {dieselKulut:.2f}€. Dieselillä ajaminen on {bensaKulut - dieselKulut:.2f}€ edullisempaa vuodessa.')
else:
    print(f'Bensalla ja dieselillä ajaminen maksavat yhtä paljon: {bensaKulut:.2f}€ vuodessa.')