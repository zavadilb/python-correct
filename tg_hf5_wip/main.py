import random


class Env:
    # Ennek a valtozonak az erteket ird at arra a feladatra, amelyiken eppen dolgozol.
    # Pl. ha a masodik feladatot szeretned futtatni, vagy ellenorizni,
    # MELYIK_FELADATON_DOLGOZOK = 2
    # szerepeljen itt.
    MELYIK_FELADATON_DOLGOZOK = 1

def nulladik():
    print("Szia!")

# Ezt az eljárást már én megírtam és a többi feladatban kell felhasználnod.
def tömegBekér():
    bemenet = input("Írj be néhány számot szóközökkel elválasztva: ")
    darabolt = bemenet.split(' ')
    tömegek = []
    for darab in darabolt:
        if darab:
            tömegek.append(int(darab))
    return tömegek

# 1. Feladat
# A feladat elején lévő kész kódrészlet bekér a felhasználótól szóközökkel elválasztva néhány számot.
# A lista elemei azoknak a járműveknek a tömegét adják meg, amiket ma egy komphajó átvitt a folyón.
# Nehéznek számítanak a 9300 kilónál nehezebb járművek. Ebben a feladatban
# írd ki azt, hogy "Igen", ha volt a hajón olyan jármű, ami nehéznek számít. Egyébként írd ki azt, hogy "Nem"!
# Minta1:
# BEMENET: "10 20 30" KIMENET: "Nem"
# Minta2:
# BEMENET: "100, 200, 9800" KIMENET: "Igen"
def elso():
    # Ide ird az elso feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    # milyen hasznos, hogy ugyanazt a kódrészletet minden feladatnál ezzel az 1 sorral meg tudjuk hívni!
    tömegek = tömegBekér()
    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

# 2. Feladat
# Írd ki, hány nehéz jármű volt! Figyelj a mintának megfelelő kiírásra!
# Minta:
# BEMENET: "9344 714 324234" KIMENET: "2 ilyen jármű volt."
def masodik():
    # Ide ird a masodik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    tömegek = tömegBekér()
    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

# 3. Feladat
# Számold meg, hogy mennyi az össztömege a járműveknek! Mennyi az össztömege a nehéz (9300 kg-nál nehezebb) járműveknek?
# Figyelj a mintának megfelelő kiírásra!
# Minta1:
# BEMENET: "110 2000 300 3032" KIMENET: "Össztömeg: 5442kg, nehéz: 0kg"
# BEMENET: "9301 2131 9500 123 382" KIMENET: "Össztömeg: 21437kg, nehéz: 18801kg"
def harmadik():
    # Ide ird a harmadik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    tömegek = tömegBekér()
    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

if __name__ == '__main__':
    if Env.MELYIK_FELADATON_DOLGOZOK == 0:
        nulladik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 1: elso()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 2: masodik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 3: harmadik()
