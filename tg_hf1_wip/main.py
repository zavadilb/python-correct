class Env:
    # Ennek a valtozonak az erteket ird at arra a feladatra, amelyiken eppen dolgozol.
    # Pl. ha a masodik feladatot szeretned futtatni, vagy ellenorizni,
    # MELYIK_FELADATON_DOLGOZOK = 2
    # szerepeljen itt.
    MELYIK_FELADATON_DOLGOZOK = 0

# Ez egy proba feladat, mar megoldottam en. Ezen kiprobalhatod a futtatas es ellenorzes kozotti kulonbseget.
# 0. Feladat: Ird ki a kimenetre a kovekezo szoveget: "Szia!"
def nulladik():
    print("Szia!")


# 1. feladat: Kerj be ket szamot a felhasznalotol egymas utan, majd ird ki a szorzatukat! Figyelj a helyes kiirasra!
#             Ha a ket szam 2 es 4, a kimenet legyen "2 es 4 szorzata: 8" (ekezetek nelkul!)
def elso():
    # Ide ird az elso feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 2. feladat: Kerj be egy nevet a felhasznalotol! Ezutan udvozold ot! Figyelj a helyes kiirasra!
#             Ha a felhasznalo neve Tomi, a kimenet legyen "Szia, Tomi!"
def masodik():
    # Ide ird a masodik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 3. feladat: Kerj be egy szamot a felhasznalotol! Figyelj a helyes kiirasra!
#            Ha a szam erteke legfeljebb 50, ird ki, hogy 'kicsi'!
#            Ha a szam erteke 51-100 kozott van (zart intervallum), ird ki, hogy 'kozepes'!
#            Ha a szam erteke 100-nal nagyobb, de legfeljebb 10-zel, ird ki, hogy 'nagy'!
#            Egyebkent a program irja ki, hogy 'nagyon nagy'!
# A feladat megoldasa soran 1 db 'if'-et, akarhany db 'elif'-et es 1 db 'else'-t hasznalhatsz!
def harmadik():
    # Ide ird a harmadik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 4. feladat: Kerj be 3 szamot a felhasznalol. Ezek kulonbozo tantargyakbol szerzett ev vegi jegyek lesznek. Miutan
#             beirta a 3 szamot, ird ki mi lesz az atlaga ezeknek a szamoknak! Ha a szam kevesebb, mint 2, irj egy ":("
#             karaktert a szam es egy szokoz utan. Egyebkent irj egy ":)" karaktert hasonlo modon.
#             Pl. ha az atlag 1.3, a kimenet: "1.3 :("
#             Pl. ha az atlag 4.5, a kimenet: "4.5 :)"
def negyedik():
    # Ide ird a negyedik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass




# Ne torold ki vagy ird at, ez kell az ellenorzeshez.
if __name__ == '__main__':
    if Env.MELYIK_FELADATON_DOLGOZOK == 0: nulladik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 1: elso()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 2: masodik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 3: harmadik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 4: negyedik()
