def tarkista_pelin_lopetus(pelaaja1, huoneet):
    for huone in huoneet:
        for kissa in huone.kissat_huoneessa:
            if kissa.luonne == "Epäsosiaalinen":
                if len(huone.kissat_huoneessa) != 1:
                    print("\nKissoja ei järjestelty oikein, mistä seurasi tappelu ja eläinlääkäri reissu.")
                    return False
    if len(pelaaja1.kissat_kyydissä) != 0:
        print("Kissoja jäi kuljetuskärryyn työvuoron päättyessä.")
        return False
    for huone in huoneet:
        for esine in huone.esineet:
            if esine.nimi == "Ruokakuppi":
                if esine.täyttö_aste == 0:
                    print("\nKissat nälkiintyivät, koska et täyttänyt ruokakuppeja.")
                    return False
    for huone in huoneet:
        for esine in huone.esineet:
            if esine.nimi == "Hiekkalaatikko":
                if esine.täyttö_aste == 1:
                    print("\nPissaa ja kakkaa on lattialla, koska et tyhjentänyt hiekkalaatikoita")
                    return False
    return True