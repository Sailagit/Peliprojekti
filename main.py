from funktiot import toiminnot
from funktiot import lopetus
from luokat.kissat import Kissa
from luokat.esineet import Esine
from luokat.huoneet import Huone, Aula
from luokat.pelaaja import Pelaaja

kissa1 = Kissa("Mei", "Sosiaalinen")
kissa2 = Kissa("Ahri", "Epäsosiaalinen")
kissa3 = Kissa("Musti", "Sosiaalinen")
kissa4 = Kissa("Sulo", "Epäsosiaalinen")
kissa5 = Kissa("Viivi", "Sosiaalinen")
kissa6 = Kissa("Rölli", "Sosiaalinen")
kissa7 = Kissa("Simba", "Sosiaalinen")
kissa8 = Kissa("Romeo", "Sosiaalinen")
kissa9 = Kissa("Misu", "Sosiaalinen")
kissa10 = Kissa("Minttu", "Sosiaalinen")
hiekkalaatikko = Esine("Hiekkalaatikko", 1)
ruokakuppi = Esine("Ruokakuppi", 0)
aula = Aula("Aula")
huone1 = Huone("Huone.1")
huone2 = Huone("Huone.2")
huone3 = Huone("Huone.3")
huone4 = Huone("Huone.4")
huone1.kissat_huoneessa.extend([kissa2, kissa10, kissa8, kissa5])
huone2.kissat_huoneessa.extend([kissa4, kissa1, kissa9])
huone3.kissat_huoneessa.extend([kissa7, kissa6, kissa3])
huone1.esineet.extend([hiekkalaatikko, ruokakuppi])
huone2.esineet.extend([hiekkalaatikko, ruokakuppi])
huone3.esineet.extend([hiekkalaatikko, ruokakuppi])
huone4.esineet.extend([hiekkalaatikko, ruokakuppi])
huoneet = [huone1, huone2, huone3, huone4]

käyttäjä = input("Hei! Mikä on nimesi? ")
print("Hauska tavata, " + käyttäjä + "!")
ikä = int(input("Kerrotko vielä ikäsi: "))
if ikä < 12:
    print("Olet alaikäinen, peli sammutetaan")
    exit()
pelaaja1 = Pelaaja(käyttäjä, aula)

print(toiminnot.lue_intro())

komento = ""

while komento != "lopeta":

    komento = input("Valitse toiminto (1 näyttää päävalikon): ")

    if komento == "1":
        toiminnot.lue_päävalikko()

    elif komento == "2":
        toiminnot.lue_ohjeet()
    
    elif komento == "5":
        toiminnot.lisää_kissa(pelaaja1)

    elif komento == "6":
        toiminnot.näytä_kissat_kuljetuskärryssä(pelaaja1)

    elif komento == "4":
        toiminnot.näytä_huoneen_kissat(pelaaja1)

    elif komento == "3":
        toiminnot.liiku(pelaaja1, aula, huone1, huone2, huone3, huone4)

    elif komento == "7":
        toiminnot.siirrä_kissa(pelaaja1)

    elif komento == "8":
        toiminnot.täytä_kuppi(pelaaja1)

    elif komento == "9":
        toiminnot.tyhjennä_hiekkalaatikko(pelaaja1)

    elif komento == "10":
        toiminnot.sijainti(pelaaja1)

    elif komento == "lopeta":
        if lopetus.tarkista_pelin_lopetus(pelaaja1, huoneet):
            print("Onneksi olkoon, suoriuduit työvuorosta onnistuneesti!")
            break
        else:
            print("Työvuoro päättyi epäonnistuneesti. Saat potkut.")
    else:
        print("Virheellinen komento. Yritä uudelleen.")
