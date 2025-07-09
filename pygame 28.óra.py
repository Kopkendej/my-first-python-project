import pygame
import os
pygame.mixer.init()
pygame.font.init()
hossz = 900
magasag = 500
Jatekos_hossz = 50
Jatekos_magasag = 50
LOVEDEK_SEBESSEG = 7
jatekos_sebbeseg = 1
Ablak = pygame.display.set_mode((hossz,magasag))
FPS = 144
GameOver_betutipus = pygame.font.SysFont('Comic Sans MS', 100)
PIROS_SZIN = (255,0,0)
SARGA_SZIN = (255,255,0)
pygame.display.set_caption("Pew Pew")
#hatterszin = (255,255,255)
hatar_szin = (0,0,0)
SZOVEG_SZIN = (241,43,255)
hatter = pygame.transform.scale(pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "tornyok.webp")), (hossz, magasag))
PIROSPNG = pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "spaceship_yellow.png"))
SárgaPNG = pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "spaceship_red.png"))
piros = pygame.transform.rotate(pygame.transform.scale(PIROSPNG,(Jatekos_hossz, Jatekos_magasag)), -90)
sárga = pygame.transform.rotate(pygame.transform.scale(SárgaPNG,(Jatekos_hossz, Jatekos_magasag)),90)
lezer_hang = pygame.mixer.Sound(os.path.join(r"Lesson_15-17_Assets\Assets", "laser.wav"))
HP_SZAMLALO_BETUTIPUS = pygame.font.SysFont('Comic Sans MS', 40)
HATAR = pygame.Rect(hossz/2,0,5, magasag)
PIROS_TALALAT = pygame.USEREVENT + 1
SARGA_TALALAT = pygame.USEREVENT + 2
def megjelenites(pirosrect,sargarect,piros_lovedek,sarga_lovedek,PIROS_HP,SARGA_HP):
    piros_hp_szoveg = HP_SZAMLALO_BETUTIPUS.render("HP: " + str(PIROS_HP), True, SZOVEG_SZIN)
    sarga_hp_szoveg = HP_SZAMLALO_BETUTIPUS.render("HP: " + str(SARGA_HP), True, SZOVEG_SZIN)
    Ablak.blit(piros_hp_szoveg, (10, 10))
    Ablak.blit(sarga_hp_szoveg, (770,10))
    Ablak.blit(piros,(pirosrect.x, pirosrect.y-25))
    Ablak.blit(sárga, (sargarect.x,sargarect.y-25))
    pygame.display.update()
    Ablak.blit(hatter, (0,0)) #mit jelenitse meg és hova tegye
    pygame.draw.rect(Ablak,hatar_szin,HATAR)
    #Ablak.fill(hatterszin)
    for lezer in piros_lovedek:
        pygame.draw.rect(Ablak,SARGA_SZIN,lezer)
    for lezer in sarga_lovedek:
        pygame.draw.rect(Ablak,PIROS_SZIN,lezer)
def main(): #futtatásos dolgok
    pirosrect = pygame.Rect(0, magasag/2-Jatekos_magasag, Jatekos_hossz, Jatekos_magasag)
    sargarect = pygame.Rect(hossz- Jatekos_hossz, magasag / 2 - Jatekos_magasag, Jatekos_hossz, Jatekos_magasag)
    piros_lovedek = []
    sarga_lovedek = []
    PIROS_HP = 10
    SARGA_HP = 10
    run = True
    clock = pygame.time.Clock()
    while run: #while fut == true
        clock.tick(FPS)
        for esemeny in pygame.event.get():
                if esemeny.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    exit()
                if esemeny.type == pygame.KEYDOWN:
                    if esemeny.key == pygame.K_e:#piros
                        lezer = pygame.Rect(pirosrect.x, pirosrect.y, 10,5)
                        lezer_hang.play()
                        piros_lovedek.append(lezer)
                    if esemeny.key == pygame.K_RCTRL:#sárga
                        lezer_hang.play()
                        lezer = pygame.Rect(sargarect.x,sargarect.y,10,5)
                        sarga_lovedek.append(lezer)
        if esemeny.type == SARGA_TALALAT:
            SARGA_HP -= 1
        if esemeny.type == PIROS_TALALAT:
            PIROS_HP -= 1
        if PIROS_HP == 0:
            gameo_szin = (255, 0, 0)
            gameover("Piros nyert!", gameo_szin)
            break
        if SARGA_HP == 0:
            gameo_szin = (255, 255, 0)
            gameover("Sárga nyert!", gameo_szin)
            break
        lovedek_iranyito(piros_lovedek,sarga_lovedek,pirosrect,sargarect)
        lenyomottGomb = pygame.key.get_pressed()
        piros_irányitas(lenyomottGomb,pirosrect)
        sarga_irányitas(lenyomottGomb, sargarect)
        megjelenites(pirosrect, sargarect,piros_lovedek,sarga_lovedek,PIROS_HP,SARGA_HP)
def piros_irányitas(lenyomottGomb,pirosrect):
    if lenyomottGomb[pygame.K_w] and pirosrect.y > 30:
        pirosrect.y -= 1
    if lenyomottGomb[pygame.K_s] and magasag-pirosrect.height >  pirosrect.y + jatekos_sebbeseg :
        pirosrect.y += 1
    if lenyomottGomb[pygame.K_a] and pirosrect.x > 0:
        pirosrect.x -= 1
    if lenyomottGomb[pygame.K_d] and not pirosrect.colliderect(HATAR):
        pirosrect.x += 1
def sarga_irányitas(lenyomottGomb,sargarect):
    if lenyomottGomb[pygame.K_UP] and sargarect.y > 30:
        sargarect.y -= 1
    if lenyomottGomb[pygame.K_DOWN] and magasag-sargarect.height > sargarect.y + jatekos_sebbeseg:
        sargarect.y += 1
    if lenyomottGomb[pygame.K_LEFT] and not sargarect.colliderect(HATAR):
        sargarect.x -= 1
    if lenyomottGomb[pygame.K_RIGHT] and hossz-sargarect.width > sargarect.x:
        sargarect.x += 1

    def lovedek_iranyito(piros_lovedekek, sarga_lovedekek, pirosrect, sargarecte):
        for piroslezer in piros_lovedekek:
            piroslezer.x += LOVEDEK_SEBESSEG
            if sargarect.colliderect(piroslezer):
                pygame.event.post(pygame.event.Event(SARGA_TALALAT))
                piros_lovedekek.remove(piroslezer)

        for sargalezer in sarga_lovedekek:
            sargalezer.x -= LOVEDEK_SEBESSEG
            if pirosrect.colliderect(sargalezer):
                pygame.event.post(pygame.event.Event(PIROS_TALALAT))
                sarga_lovedekek.remove(sargalezer)
def lovedek_iranyito(piros_lovedekek, sarga_lovedekek, piros, sarga):
    for piroslezer in piros_lovedekek:
        piroslezer.x += LOVEDEK_SEBESSEG
        if sarga.colliderect(piroslezer):
            pygame.event.post(pygame.event.Event(SARGA_TALALAT))
            piros_lovedekek.remove(piroslezer)

    for sargalezer in sarga_lovedekek:
        sargalezer.x -= LOVEDEK_SEBESSEG
        if piros.colliderect(sargalezer):
            pygame.event.post(pygame.event.Event(PIROS_TALALAT))
            sarga_lovedekek.remove(sargalezer)
def gameover(szoveg,gameo_szin):
    gameover_szoveg = GameOver_betutipus.render(szoveg,True, gameo_szin)
    Ablak.blit(gameover_szoveg,(hossz/2 - gameover_szoveg.get_width() / 2,magasag/2 - gameover_szoveg.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000) #késleltetés

main()