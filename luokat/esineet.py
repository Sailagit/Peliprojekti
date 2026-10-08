class Esine:
    def __init__(self, nimi, täyttö_aste):
        self.nimi = nimi
        self.täyttö_aste = täyttö_aste

    def täytä(self):
        if self.täyttö_aste == 1:
            print(self.nimi, "on jo täynnä.")
        else:
            self.täyttö_aste = 1
            print(self.nimi, "on täytetty kestävästi kalastetulla kalaruualla!")

    def tyhjennä(self):
        if self.täyttö_aste == 0:
            print(self.nimi, "on jo tyhjä.")
        else:
            self.täyttö_aste = 0
            print(self.nimi, "on tyhjennetty.")