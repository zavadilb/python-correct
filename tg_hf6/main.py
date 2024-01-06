class Env:
    # Ennek a valtozonak az erteket ird at arra a feladatra, amelyiken eppen dolgozol.
    # Pl. ha a masodik feladatot szeretned futtatni, vagy ellenorizni,
    # MELYIK_FELADATON_DOLGOZOK = 2
    # szerepeljen itt.
    MELYIK_FELADATON_DOLGOZOK = 2

def nulladik():
    print("Szia!")

# 1. Feladat
# Írj egy programot, ami bekér a felhasználótól két szót, ":" karakterrel elválasztva. Ezt megismétli 3-szor.
# Ezeket a szavakat tedd be egy szótárba a mintának megfelelően! A végén íd ki a a szótárat!
# A szótár kiírásához csak a print(szótár) utasítást használd, nem kell bonyolultabban formázni.
# Minta:
# BEMENET:
# "kicsi:small"
# "alma:apple"
# "körte:pear"
# KIMENET:
# {'kicsi': 'small', 'alma': 'apple', 'körte': 'pear'}
def elso():
    # Ide ird az elso feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass
# 2. Feladat
# Írj programot, mely bekér egymás után vesszővel elválasztva számokat, majd belerakja őket egy szótárba.
# A szótárban egy bejegyzés értéke mindig az, hogy hányadik szónál járunk, az kulcsa pedig a beírt szó.
# A szótár kiírásához csak a print(szótár) utasítást használd, nem kell bonyolultabban formázni.
# Minta:
# BEMENET: "alma,körte,citrom,narancs"
# KIMENET: "{'alma': 1, 'körte': 2, 'citrom': 3, 'narancs': 4}
def masodik():
    # Ide ird a masodik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

def harmadik():
    # most nincs harmadik feladat :)
    pass

if __name__ == '__main__':
    if Env.MELYIK_FELADATON_DOLGOZOK == 0:
        nulladik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 1: elso()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 2: masodik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 3: harmadik()
