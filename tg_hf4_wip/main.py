class Env:
    # Ennek a valtozonak az erteket ird at arra a feladatra, amelyiken eppen dolgozol.
    # Pl. ha a masodik feladatot szeretned futtatni, vagy ellenorizni,
    # MELYIK_FELADATON_DOLGOZOK = 2
    # szerepeljen itt.
    MELYIK_FELADATON_DOLGOZOK = 1

def nulladik():
    print("Szia!")

# 1. Feladat
# Írj egy programot, ami bekér egy szöveget, és ha a (karakterekben mért) hossza 4-el osztható,
# kiírja a szöveg fordítottját, egyébként magát a szöveget!
# Minta1:
# BEMENET: "Ez a mondat 4-el osztható számú karaktert tartalmaz."
# KIMENET: ".zamlatrat tretkarak úmázs ótahtzso le-4 tadnom a zE"
# Minta2:
# BEMENET: "Abcde"
# KIMENET: "Abcde"
def elso():
    # Ide ird az elso feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 2. Feladat
# Írj egy programot, ami bekér a felhasználótól egy szöveget, majd megnézi, hogy a mondat utolsó szava
# az-e, hogy "azt". Ha igen, írja ki, hogy "Igen", egyébként azt, hogy "Nem".
# Feltételezd, hogy az utolsó szó után vagy '.' karakter van, vagy semmi.
# Minta1:
# BEMENET: "Nem ezt az almát ettem meg, hanem azt."
# KIMENET: "Igaz"
# BEMENET: "Nem ezt az almát ettem meg, hanem azt"
# KIMENET: "Igaz"
# BEMENET: "Nem ezt az almát ettem meg."
# KIMENET: "Hamis"
def masodik():
    # Ide ird a masodik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

# 3. Feladat
# Írj egy programot, ami bekér egy szöveget a felhasználótól és kiírja, milyen hosszú a leghosszabb szó
# benne a mintának megfelelően!.
# Minta1:
# BEMENET: "Ez egy rövid mondat"
# KIMENET: "6"
# BEMENET: "Ebben a mondatban a leghosszabb szó az, hogy leghosszabb"
# KIMENET: "11"
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
