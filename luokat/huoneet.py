class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kissat_huoneessa = []
        self.esineet = []

class Aula(Huone):
    def __init__(self, nimi):
        super().__init__(nimi)


# Huoneiden määrä on x ja niissä on x määrä kissoja
# Yksi huone voisi olla tyhjä?
# Pelaajalle annettu lista mitkä kissat voivat olla yhdessä
# Lopussa for looppi tarkistaa esintyykö tietyt alkiot samassa listassa?
# Huoneessa pitää olla raja monta kissaa siihen voi lisätä, jos mahdollista toteuttaa