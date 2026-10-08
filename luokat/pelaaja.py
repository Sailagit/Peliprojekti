from luokat.huoneet import Huone 

class Pelaaja(Huone):
    def __init__(self, käyttäjä, sijainti):
        self.käyttäjä = käyttäjä
        self.kissat_kyydissä = []
        self.sijainti = sijainti
    
    def liiku(self, huone):
        self.sijainti = huone
        print("\nSiirryit huoneeseen: ", huone.nimi)

    def kerää_kissa(self, kissa):
        if kissa in self.sijainti.kissat_huoneessa:
            self.kissat_kyydissä.append(kissa)
            self.sijainti.kissat_huoneessa.remove(kissa)
            print(kissa.nimi, "siirretty kuljetuskärryyn!")
        else:
            print("Tämä kissa ei ole tässä huoneessa")

    def siirrä_kissa(self, kissa):
        if len(self.sijainti.kissat_huoneessa) >= 4:
            print("Huoneessa on maximi määrä kissoja")
        elif kissa in self.kissat_kyydissä:
            self.kissat_kyydissä.remove(kissa)
            self.sijainti.kissat_huoneessa.append(kissa)
            print(kissa.nimi, "on siirretty huoneeseen.")
        else:
            print("Tämä kissa ei ole kuljetuskärryssä.")