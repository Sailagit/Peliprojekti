def näytä_huoneen_kissat(pelaaja1):
    print("\nHuoneessa", pelaaja1.sijainti.nimi, "on")

    if len(pelaaja1.sijainti.kissat_huoneessa) == 0:
        print("Huoneessa ei ole kissoja")
    else:
        for kissa in pelaaja1.sijainti.kissat_huoneessa:
            print("-", kissa.nimi)

def lisää_kissa(pelaaja1):
    näytä_huoneen_kissat(pelaaja1)

    nimi = input("Minkä kissan haluat siirtää kuljetuskärryyn? ").capitalize()

    for kissa in pelaaja1.sijainti.kissat_huoneessa:
        if kissa.nimi == nimi:
            pelaaja1.kerää_kissa(kissa)
            return

    print("Tämän nimistä kissaa ei löytynyt huoneesta.")

def näytä_kissat_kuljetuskärryssä(pelaaja1):
    print("\nKuljetuskärryssä on:")

    if len(pelaaja1.kissat_kyydissä) == 0:
        print("Kuljetuskärryssä ei ole yhtään kissaa.")
    else:
        for kissa in pelaaja1.kissat_kyydissä:
            print("-", kissa.nimi,)

def siirrä_kissa(pelaaja1):
    näytä_kissat_kuljetuskärryssä(pelaaja1)

    nimi = input("Minkä kissan haluat siirtää huoneeseen? ").capitalize()

    for kissa in pelaaja1.kissat_kyydissä:
        if kissa.nimi == nimi:
            pelaaja1.siirrä_kissa(kissa)
            return
    print("Tämän nimistä kissaa ei löytynyt kuljetuskärrystä.")

def liiku(pelaaja1, aula, huone1, huone2, huone3, huone4):
    print("\nMihin huoneeseen haluat siirtyä?")
    print("1 - Huone1")
    print("2 - Huone2")
    print("3 - Huone3")
    print("4 - Huone4")

    valinta = input("Valitse huone: ")

    if valinta == "1":
        pelaaja1.liiku(huone1)

    elif valinta == "2":
        pelaaja1.liiku(huone2)

    elif valinta == "3":
        pelaaja1.liiku(huone3)

    elif valinta == "4":
        pelaaja1.liiku(huone4)

    else:
        print("Virheellinen valinta.")

def täytä_kuppi(pelaaja1):
    for esine in pelaaja1.sijainti.esineet:
        if esine.nimi == "Ruokakuppi":
            esine.täytä()
            return

def tyhjennä_hiekkalaatikko(pelaaja1):
    for esine in pelaaja1.sijainti.esineet:
        if esine.nimi == "Hiekkalaatikko":
            esine.tyhjennä()
            return

def lue_ohjeet():
    with open("ohjeet.txt", "r", encoding="utf-8") as tiedosto:
        ohjeet = tiedosto.read()
        print(ohjeet)

def lue_intro():
    with open("intro.txt", "r", encoding="utf-8") as tiedosto:
        intro = tiedosto.read()
    return intro

def lue_päävalikko():
    with open("päävalikko.txt", "r", encoding="utf-8") as tiedosto:
        päävalikko = tiedosto.read()
        print(päävalikko)

def sijainti(pelaaja1):
    print("Olet tällä hetkellä huoneessa:", pelaaja1.sijainti.nimi)
