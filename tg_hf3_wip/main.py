class Env:
    # Ennek a valtozonak az erteket ird at arra a feladatra, amelyiken eppen dolgozol.
    # Pl. ha a masodik feladatot szeretned futtatni, vagy ellenorizni,
    # MELYIK_FELADATON_DOLGOZOK = 2
    # szerepeljen itt.
    MELYIK_FELADATON_DOLGOZOK = 3

def nulladik():
    print("Szia!")

# 1. Feladat
# Írj egy programot, ami bekér a felhasználótól egy mondatot, majd a mintának megfelelően kiírja, hány
# szám van a mondatban és mi az összegük! Feltételezheted, hogy csak egyjegyű számok vannak a mondatban.
# Minta1:
# BEMENET: "Ebben a mondatban van 3, 4 illetve 8."
# KIMENET: "A mondatban 3 szám volt, amelyek összege 15."
# Minta2:
# BEMENET: "Az erdőben 9 róka és 4 nyúl lakik"
# KIMENET: "A mondatban 2 szám volt, amelyek összege 13."
#
# Tipp: Ha egy karaktert szám típusúvá szeretnél konvertálni, használd az int(karakter) utasítást!
def elso():
    # Ide ird az elso feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass


# 2. Feladat
# Írj egy programot, amely bekér egy szót, majd kiírja annak az első, középső és utolsó karakterét.
# Amennyiben a szónak nincs középső karaktere, írja ki a program csak az első és utolsó karaktert!
# Minta1:
# BEMENET: "James"
# KIMENET: "Jms"
# Minta2:
# BEMENET: "negy"
# KIMENET: "ny"
# Tipp (a kódrészlet bemutatja, hogyan lehet "levágni" a tizedesvessző utáni részét egy számnak):
# a = 2.5
# b = int(a)
# print(b) # kimenet: 2
def masodik():
    # Ide ird a masodik feladat megoldasat!
    # <---- Ettol a karaktertol balra ne legyen kod, tehat itt, vagy ettol jobbra kezdj minden sort!

    #Torold ki ezt a sort es a helyere irhatod a megoldast!

    # Feladat vege, ezzel ne foglalkozz!
    pass

# 3. Feladat
# Kérj be két szót a felhasználótól! Az első szó közepére szúrd be a második szót,
# majd írd ki az eredményt! (Ha az első szó páratlan számú karakterből áll, akkor a
# középső karakter elé szúrd be a második szót!)
# Minta1:
# BEMENET: "teve", "kutya"
# KIMENET: "tekutyave"
# Minta2:
# BEMENET: "tehén", "teve"
# KIMENET: "tetevehén"
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
