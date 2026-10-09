class Huone:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kissat_huoneessa = []
        self.esineet = []

class Aula(Huone):
    def __init__(self, nimi):
        super().__init__(nimi)