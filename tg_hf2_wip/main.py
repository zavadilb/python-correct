class Env:
    # Ennek a valtozonak az erteket ird at arra a feladatra, amelyiken eppen dolgozol.
    # Pl. ha a masodik feladatot szeretned futtatni, vagy ellenorizni,
    # MELYIK_FELADATON_DOLGOZOK = 2
    # szerepeljen itt.
    MELYIK_FELADATON_DOLGOZOK = 1


def nulladik():
    print("Szia!")


# 1. Feladat
# Kérj be egy mondatot a felhasználótól és írd ki a fordítottját! Figyelj a mintának megfelelő kiírásra!
# Pl. Ha a bemenet "Szép tehenek" akkor a kimenet legyen "Szép tehenek fordítottja: kenehet pézS"!
def elso():
    # Ide ird az elso feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 2. Feladat
# Kérj be a felhasználótól egy mondatot, majd egy szót! Ha a mondatban benne van a szó, minden előfordulását cseréld ki
# a "tej" szóra! Ha nincs benne a mondatban, akkor írd ki, hogy a mondat már helyes!
# Figyelj a mintának megfelelő kiírásra!
# Pl. BEMENET: "A kóla nagyon finom." ÉS "kóla" -> KIMENET: "A tej nagyon finom."
# Pl. BEMENET: "A fanta nagyon finom." ÉS "kóla" -> KIMENET:"A mondat már helyes."
def masodik():
    # Ide ird a masodik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 3. Feladat
# Kérj be a felhasználótól egy mondatot! Ezután írd ki a mondatban lévő szavakat kötőjelekkel elválasztva és azt, hogy
# hány szóból áll a mondat! Figyelj a mintának megfelelő kiírásra!
# Pl. BEMENET: "A tej nagyon finom" KIMENET: "A mondat 4 szóból áll: A-tej-nagyon-finom"
def harmadik():
    # Ide ird a harmadik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

if __name__ == '__main__':
    if Env.MELYIK_FELADATON_DOLGOZOK == 0:
        nulladik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 1: elso()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 2: masodik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 3: harmadik()
