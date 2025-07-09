import pygame
import os

# Pygame inicializálása
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Ablak beállítása
hossz = 900
magasag = 500
Ablak = pygame.display.set_mode((hossz, magasag))
pygame.display.set_caption("Fantasy Kalandjáték")

# Képek betöltése
try:
    helyszin_kezdohely = pygame.transform.scale(
        pygame.image.load(os.path.join("Jatek", "kezdohely.jpg")),
        (hossz, magasag)
    )
    sotet_ut_kep = pygame.transform.scale(
        pygame.image.load(os.path.join("Jatek", "sotet_ut.jpeg")),
        (hossz, magasag)
    )
    farkas_kep = pygame.transform.scale(
        pygame.image.load(os.path.join("Jatek", "farkas.jpeg")),
        (hossz, magasag)
    )
    var_kapu_kep = pygame.transform.scale(
        pygame.image.load(os.path.join("Jatek", "var_kapu.jpeg")),
        (hossz, magasag)
    )
except pygame.error:
    print("Hiba a kép betöltésekor! Ellenőrizd a fájl elérhető és helyes formátumú.")
    helyszin_kezdohely = pygame.Surface((hossz, magasag))
    helyszin_kezdohely.fill((50, 50, 50))
    sotet_ut_kep = pygame.Surface((hossz, magasag))
    sotet_ut_kep.fill((30, 30, 30))
    farkas_kep = pygame.Surface((hossz, magasag))
    farkas_kep.fill((10, 10, 10))
    var_kapu_kep = pygame.Surface((hossz, magasag))
    var_kapu_kep.fill((20, 20, 20))

# Hátizsák tartalma (szótárként kezelve)
hatizsak = {"Arany": 5, "Kenyér": 1, "Balta": 1}

# Szöveg részekre bontása
szovegek = [
    "Egy ködös hajnalon magadhoz térsz egy hatalmas, zöldellő réten.",
    "A harmat még csillog a fűszálakon, a madarak csivitelnek.",
    "De valami nincs rendben – nem emlékszel, hogyan kerültél ide.",
    "Ahogy körbenézel, egy impozáns vár magasodik előtted.",
    "Míg távolabb, az erdő szélén egy magányos kunyhó sziluettje rajzolódik ki.",
    "Egy furcsa érzés kerít hatalmába: mintha választanod kellene.",
    "Ha hazamész a kunyhódba, az út hosszú lesz,",
    " és mire odaérsz, már este borul a vidékre.",
    "Ki tudja, mi vár rád a sötétben?[1-es gomb]",
    "Ha a várba mész, egy nyüzsgő vásárba érkezel,",
    " ahol árusok kínálják portékájukat.",
    "A kapun való belépésnek ára van – egy arany.[2-es gomb]",
    "A választás a tiéd. [1/2] Bármerre indulsz, a sorsod egy rejtély felé sodor."
]

farkasos_szovegek = [
    "Az úton egy hatalmas farkas támad rád.",
    "A szemeid előtt felvillan az életed, miközben a fenevad közeledik.",
    "Mit teszel? Harcolsz a baltáddal? [H gomb]",
    "Vagy futásnak eredsz, hogy megmentsd az életed? [F gomb]"
]

# Arany levonása
def arany_levonasa(hatizsak, osszeg):
    if hatizsak.get("Arany", 0) >= osszeg:
        hatizsak["Arany"] -= osszeg
        print(f"{osszeg} arany levonva. Maradék arany: {hatizsak['Arany']}")
        return True
    else:
        print("Nincs elég arany!")
        return False

# Szöveg megjelenítése árnyékkal
def kiir_szoveget(szovegek, font, ablak, szin=(255, 255, 255), arnyek_szin=(0, 0, 0), hatter=None):
    y_koordinata = magasag - 100
    for szoveg in szovegek:
        if hatter:
            ablak.blit(hatter, (0, 0))
        arnyek_szoveg = font.render(szoveg, True, arnyek_szin)
        ablak.blit(arnyek_szoveg, (27, y_koordinata + 2))
        renderelt_szoveg = font.render(szoveg, True, szin)
        ablak.blit(renderelt_szoveg, (25, y_koordinata))
        hatizsak_arnyek = font.render("Hátizsák: " + ", ".join([f"{kulcs} ({ertek})" for kulcs, ertek in hatizsak.items()]), True, arnyek_szin)
        ablak.blit(hatizsak_arnyek, (hossz - hatizsak_arnyek.get_width() - 12, 12))
        hatizsak_szoveg = font.render("Hátizsák: " + ", ".join([f"{kulcs} ({ertek})" for kulcs, ertek in hatizsak.items()]), True, szin)
        ablak.blit(hatizsak_szoveg, (hossz - hatizsak_szoveg.get_width() - 10, 10))
        pygame.display.update()
        pygame.time.delay(4500)

# Kapuőr párbeszéd
def var_kapu_parbeszed(font, ablak):
    parbeszed = [
        "Kapu őr: Üdvözletem, a várba szeretne jönni?",
        "Én: Igen.",
        "Kapu őr: Annak viszont ára van.",
        "Én: És mégis mennyi?",
        "Kapu őr: 1 arany.",
        "Mesélő/Gondolatom: Kifizetem az egy aranyat [1-es gomb],",
        "vagy inkább vissza megyek a házamba. [2-es gomb]"
    ]

    ablak.blit(var_kapu_kep, (0, 0))  # Háttérkép kirajzolása
    x_kezdo = 25  # Fix kezdő x-koordináta
    y_kezdo = magasag - 100  # Fix kezdő y-koordináta (első sor)
    y_tavolsag = 30  # Második sor relatív távolsága az elsőtől

    for i in range(0, len(parbeszed), 2):  # Két szöveg megjelenítése egyszerre
        ablak.fill((0, 0, 0))  # Tisztítjuk az ablakot
        ablak.blit(var_kapu_kep, (0, 0))  # Háttérkép visszarakása

        # Hátizsák megjelenítése
        hatizsak_arnyek = font.render(
            "Hátizsák: " + ", ".join([f"{kulcs} ({ertek})" for kulcs, ertek in hatizsak.items()]), True, (0, 0, 0))
        ablak.blit(hatizsak_arnyek, (hossz - hatizsak_arnyek.get_width() - 12, 12))
        hatizsak_szoveg = font.render(
            "Hátizsák: " + ", ".join([f"{kulcs} ({ertek})" for kulcs, ertek in hatizsak.items()]), True,
            (255, 255, 255))
        ablak.blit(hatizsak_szoveg, (hossz - hatizsak_szoveg.get_width() - 10, 10))

        # Első sor megjelenítése
        if i < len(parbeszed):
            szoveg = parbeszed[i]
            arnyek_szoveg = font.render(szoveg, True, (0, 0, 0))
            ablak.blit(arnyek_szoveg, (x_kezdo + 2, y_kezdo + 2))  # Árnyék
            renderelt_szoveg = font.render(szoveg, True, (255, 255, 255))
            ablak.blit(renderelt_szoveg, (x_kezdo, y_kezdo))  # Szöveg

        # Második sor megjelenítése
        if i + 1 < len(parbeszed):
            szoveg = parbeszed[i + 1]
            arnyek_szoveg = font.render(szoveg, True, (0, 0, 0))
            ablak.blit(arnyek_szoveg, (x_kezdo + 2, y_kezdo + y_tavolsag + 2))  # Árnyék
            renderelt_szoveg = font.render(szoveg, True, (255, 255, 255))
            ablak.blit(renderelt_szoveg, (x_kezdo, y_kezdo + y_tavolsag))  # Szöveg

        pygame.display.update()
        pygame.time.delay(3000)  # 3 másodperc várakozás a következő blokknál
# Kunyhó esemény
def kunyho_ut(font, ablak):
    kiir_szoveget(farkasos_szovegek, font, ablak, hatter=sotet_ut_kep)

# Játék vége
def jatek_vege(ablak):
    ablak.fill((0, 0, 0))
    font = pygame.font.SysFont('Comic Sans MS', 50)
    vege_szoveg = font.render("JÁTÉK VÉGE", True, (255, 0, 0))
    ablak.blit(vege_szoveg, ((hossz - vege_szoveg.get_width()) // 2, (magasag - vege_szoveg.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(5000)

# Futás kimenetele
def futas_kimenetel(ablak):
    ablak.blit(farkas_kep, (0, 0))
    font = pygame.font.SysFont('Comic Sans MS', 25)
    szoveg = "A farkas gyorsabban futott és hátba támadott."
    renderelt_szoveg = font.render(szoveg, True, (255, 255, 255))
    ablak.blit(renderelt_szoveg, (50, magasag - 100))
    pygame.display.update()
    pygame.time.delay(3000)
    jatek_vege(ablak)

# Főciklus
def jatek():
    futas = True
    valasztott_e = False
    font = pygame.font.SysFont('Comic Sans MS', 22)
    kiir_szoveget(szovegek, font, Ablak, szin=(255, 255, 255), arnyek_szin=(0, 0, 0), hatter=helyszin_kezdohely)

    while futas:
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                futas = False
            elif esemeny.type == pygame.KEYDOWN:
                if esemeny.key == pygame.K_1:  # A kunyhót választja
                    print("A játékos a kunyhót választotta.")
                    kunyho_ut(font, Ablak)
                elif esemeny.key == pygame.K_2:  # A várat választja
                    print("A játékos a várat választotta.")
                    var_kapu_parbeszed(font, Ablak)
                    fizetni_vagy_vissza = True
                    while fizetni_vagy_vissza:
                        for esemeny_vissza in pygame.event.get():
                            if esemeny_vissza.type == pygame.KEYDOWN:
                                if esemeny_vissza.key == pygame.K_1:  # Fizet
                                    if arany_levonasa(hatizsak, 1):
                                        print("A játékos kifizette az egy aranyat.")
                                        fizetni_vagy_vissza = False
                                    else:
                                        print("A játékosnak nincs elég aranya!")
                                        fizetni_vagy_vissza = False
                                elif esemeny_vissza.key == pygame.K_2:  # Visszafordul
                                    print("A játékos visszafordult a házába.")
                                    fizetni_vagy_vissza = False
                elif esemeny.key == pygame.K_f:  # Futás
                    print("A játékos fut.")
                    futas_kimenetel(Ablak)
                elif esemeny.key == pygame.K_h:  # Harc
                    print("A játékos harcol.")
                    # Ide lehet harci mechanikát tenni
# Főprogram
def main():
    jatek()
main()
pygame.quit()