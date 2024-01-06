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
    szo = input("Irj be egy mondatot: ")
    i = len(szo) - 1
    forditott = ""
    while i >= 0:
        forditott += szo[i]
        i -= 1

    # forditott = szo[::-1] # :)
    # forditott = ''.join(reversed(szo))
    print(f"{szo} fordítottja: {forditott}")

    pass


# 2. Feladat
# Kérj be a felhasználótól egy mondatot, majd egy szót! Ha a mondatban benne van a szó, minden előfordulását cseréld ki
# a "tej" szóra! Ha nincs benne a mondatban, akkor írd ki, hogy a mondat már helyes!
# Figyelj a mintának megfelelő kiírásra!
# Pl. BEMENET: "A kóla nagyon finom." ÉS "kóla" -> KIMENET: "A tej nagyon finom."
# Pl. BEMENET: "A fanta nagyon finom." ÉS "kóla" -> KIMENET:"A mondat már helyes."
def masodik():
    mondat = input("Irj be egy mondatot: ")
    szo = input("Irj be egy szot: ")

    if szo in mondat:
        print(mondat.replace(szo, 'tej'))
    else:
        print("A mondat már helyes.")
    pass

# 3. Feladat
# Kérj be a felhasználótól egy mondatot! Ezután írd ki a mondatban lévő szavakat kötőjelekkel elválasztva és azt, hogy
# hány szóból áll a mondat! Figyelj a mintának megfelelő kiírásra!
# Pl. BEMENET: "A tej nagyon finom" KIMENET: "A mondat 4 szóból áll: A-tej-nagyon-finom"
def harmadik():
    mondat = input("Írj be egy mondatot: ").split(' ')
    print(f"A mondat {len(mondat)} szóból áll: {'-'.join(mondat)}")

    pass

if __name__ == '__main__':
    if Env.MELYIK_FELADATON_DOLGOZOK == 0:
        nulladik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 1: elso()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 2: masodik()
    elif Env.MELYIK_FELADATON_DOLGOZOK == 3: harmadik()
