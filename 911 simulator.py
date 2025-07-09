import pygame
import os
import time
pygame.mixer.init()

hossz = 900
magasag = 500
Jatekos_hossz = 60
Jatekos_magasag = 60
ertek = 1
pos = 383
hatar_szin = (0,0,0)
Ablak = pygame.display.set_mode((hossz,magasag))
FPS = 144

robanás_hang = pygame.mixer.Sound(os.path.join(r"Lesson_15-17_Assets\Assets", "explosion.wav"))
hatter_uj = pygame.transform.scale(pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "9-11-01.jpg")), (hossz, magasag))
pygame.display.set_caption("Pew Pew")
hatter = pygame.transform.scale(pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "tornyok.webp")), (hossz, magasag))
repulopng = pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "repulo.png"))
robbanaspng = pygame.image.load(os.path.join(r"Lesson_15-17_Assets\Assets", "robbanas.png"))
repulo = pygame.transform.rotate(pygame.transform.scale(repulopng,(Jatekos_hossz, Jatekos_magasag)),90)
HATAR = pygame.Rect(pos,0,ertek, magasag)
SZEL = pygame.Rect(0,0,ertek, magasag)
melyikhatter = hatter
erintete = False
show_robbanas = False
robbanas_time = 0
robbanas_pos = None
def megjelenites(repulorect):
    global erintete,show_robbanas,robbanas_time,robbanas_pos

    if erintete:
        Ablak.blit(hatter_uj, (0, 0))
    else:
        Ablak.blit(hatter, (0, 0))
    pygame.draw.rect(Ablak, hatar_szin, SZEL)

    if not show_robbanas:
        Ablak.blit(repulo, (repulorect.x, repulorect.y))
    elif show_robbanas and robbanas_pos:
        Ablak.blit(robbanaspng,robbanas_pos)
        if time.time() - robbanas_time >= 1:
            show_robbanas = False

    pygame.display.update()

    if repulorect.colliderect(HATAR) and not erintete:
        erintete = True
        show_robbanas = True
        robbanas_pos = (repulorect.x, repulorect.y)
        robbanas_time = time.time()
        robanás_hang.play()
        repulorect.x = -9999
def repcsiiranyitas(lenyomottGomb,repulorect):
    if lenyomottGomb[pygame.K_SPACE]:
        time.sleep(0.001)
        repulorect.x -= 1
def main():
    repulorect = pygame.Rect(hossz- Jatekos_hossz, magasag / 2 - Jatekos_magasag, Jatekos_hossz, Jatekos_magasag)
    run = True
    clock = pygame.time.Clock()
    while run:  # while fut == true
        clock.tick(FPS)
        for esemeny in pygame.event.get():
            if esemeny.type == pygame.QUIT:
                run = False
        lenyomottGomb = pygame.key.get_pressed()
        repcsiiranyitas(lenyomottGomb, repulorect)
        megjelenites(repulorect)
    pygame.quit()
main()
#0911