pizzat = {
    1: {'nimi': 'Bolognese',
        'taytteet': ['jauheliha'],
        'hinta': 7.50},
    2: {'nimi': 'Frutti di Mare',
        'taytteet': ['ananas', 'katkarapu', 'tonnikala'],
        'hinta': 8.50},
    3: {'nimi': 'Americano',
        'taytteet': ['ananas', 'aurajuusto', 'kinkku'],
        'hinta': 9.00},
    4: {'nimi': 'Opera Special',
        'taytteet': ['kinkku', 'salami', 'tonnikala'],
        'hinta': 9.50},
    5: {'nimi': 'Mexicana',
        'taytteet': ['ananas', 'pepperoni', 'chili',
                     'tacokastike'],
        'hinta': 10.00},
    6: {'nimi': 'Julia',
        'taytteet': ['ananas', 'aurajuusto', 'katkarapu',
                     'kinkku'],
        'hinta': 10.50},
    7: {'nimi': 'Empire Special',
        'taytteet': ['katkarapu', 'kinkku', 'mustapippuri',
                     'salami', 'sipuli', 'tuplajuusto',
                     'valkosipuli'],
                     'hinta': 11.00},
    8: {'nimi': 'Kummisetä',
        'taytteet': ['herkkusieni', 'katkarapu', 'kinkku',
                     'valkosipuli'],
        'hinta': 11.00},
    9: {'nimi': 'Chicken Hawaii',
        'taytteet': ['ananas', 'aurajuusto', 'kana'],
        'hinta': 11.00},
    11: {'nimi': 'Romeo',
         'taytteet': ['ananas', 'aurajuusto', 'katkarapu',
                      'salami'],
         'hinta': 11.00},
    12: {'nimi': 'Vegetariana',
         'taytteet': ['herkkusieni', 'oliivi', 'paprika',
                      'sipuli', 'tomaatti'],
         'hinta': 10.00},
    13: {'nimi': 'Dillinger',
         'taytteet': ['jauheliha', 'kinkku', 'salami',
                      'sipuli'],
         'hinta': 10.00},
    14: {'nimi': 'Papa''s Special',
         'taytteet': ['aurajuusto', 'mustapippuri', 'oliivi',
                      'paprika', 'salami', 'sipuli'],
         'hinta': 11.00},
    15: {'nimi': 'Quattro Stagioni',
         'taytteet': ['herkkusieni', 'katkarapu', 'kinkku',
                      'paprika'],
         'hinta': 10.00},
    16: {'nimi': 'Cambretti',
         'taytteet': ['tuplajuusto', 'katkarapu',
                      'valkosipuli'],
         'hinta': 11.00},
    17: {'nimi': 'Pepperoni',
         'taytteet': ['paprika', 'pepperoni', 'tonnikala'],
         'hinta': 10.00},
    19: {'nimi': 'Spicy Hot Crispy',
         'taytteet': ['mausteinen naudanliha', 'sipuli',
                      'tomaatti', 'chili'],
         'hinta': 10.00},
    21: {'nimi': 'Finlandia',
         'taytteet': ['kana', 'katkarapu', 'kinkku',
                      'salami', 'tonnikala'],
         'hinta': 11.00},
    23: {'nimi': 'Driver''s Special',
         'taytteet': ['pekoni', 'pepperoni', 'kinkku',
                      'salami', 'aurajuusto'],
         'hinta': 11.00},
    26: {'nimi': 'Fantasia',
         'taytteet': [None, None, None, None],
         'hinta': 14.00}
}

yhteishinta = 0

print("Tervetuloa pizzatilaukseen!")
print("Anna pizzan numero (0 lopettaa): ")
while True:
    valinta = int(input())
    if valinta == 0:
        print(f"Kiitos tilauksesta! Kokonaishintanne on {round(yhteishinta, 2)} euroa.")
        break
    elif valinta in pizzat:
        pizza = pizzat[valinta] # Haetaan valitun pizzan tiedot sanakirjasta
        print(f"Valitsit pizzan: {pizza['nimi']}")
        kappalemaara = int(input("Anna kappalemäärä: "))
        while kappalemaara < 1 or kappalemaara > 50: # Tarkistetaan käyttäjän syöte
            print("Kappalemäärän tulee olla vähintään 1 ja enintään 50. Yritä uudelleen.")
            kappalemaara = int(input("Anna kappalemäärä: "))
        print(f"Hinta: {pizza['hinta']} euroa")
        yhteishinta += pizza['hinta'] * kappalemaara # Päivitetään yhteishinta
        print("Anna pizzan numero (0 lopettaa): ")
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        print("Anna pizzan numero (0 lopettaa): ")
