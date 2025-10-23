def on_palindromi(sana):
    listakirjaimista = [] # luodaan tyhjä lista kirjaimille
    for merkki in sana: # Käydään merkit läpi yksi kerrallaan
        if merkki.isalpha(): # Jos merkki on kirjain,
            listakirjaimista.append(merkki.upper()) # lisätään se listaan isoina kirjaimina

    if listakirjaimista == list(reversed(listakirjaimista)): # Verrataan listaa käännettyyn listaan
        return True # Jos ne ovat samat, sana on palindromi
    else:
        return False # Muuten sana ei ole palindromi


ehdokkaat = [
    'A man, a plan, a canal: Panama.', # On palindromi
    'Iso rikas sika sökösakissa kirosi.', # On palindromi
    '"Aa, viinaa sitruksilla", kallis kurtisaani ivaa.', # On palindromi
    'Joku satunnainen lause', # Ei ole palindromi
    'A1a2A3a4b5B6a7A8A9a0', # On palindromi
]

for e in ehdokkaat:
    tulos = 'EI OLE'
    if on_palindromi(e):
        tulos = 'ON'
    print(f'"{e}": {tulos} palindromi')