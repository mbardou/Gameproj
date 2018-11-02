import os
import sys, math, random, pygame
from pygame.locals import *
from pygame import *

pygame.init()

largeur = 1024
hauteur = 768
LargeurPerso = 30
HauteurPerso = 50
fontChat = pygame.font.SysFont("monospace", 15)
# fenetre=pygame.display.set_mode((largeur,hauteur))
fenetre=pygame.display.set_mode((largeur,hauteur), RESIZABLE)
rectFenetre = fenetre.get_rect()
imageChatbox = pygame.image.load("pictures/FenetreChat1.png").convert_alpha()
rectChatbox = imageChatbox.get_rect()
rectChatbox.y = 624
imageFond = pygame.image.load("pictures/eau.png").convert_alpha()
imagePont01 = pygame.image.load("pictures/pont01.png").convert_alpha()
imageMarketplace01 = pygame.image.load("pictures/marketplace.png").convert_alpha()
imageMarketplace02 = pygame.image.load("pictures/marketplace2.png").convert_alpha()
imagePontvertical01 = pygame.image.load("pictures/pontvertical01.png").convert_alpha()
imageHorloge01 = pygame.image.load("pictures/horloge1.png").convert_alpha()
imagePuit01 = pygame.image.load("pictures/puit1.png").convert_alpha()
imageTonneau01 = pygame.image.load("pictures/tonneau1.png").convert_alpha()
imageLampe01 = pygame.image.load("pictures/lampe1.png").convert_alpha()
imageBanc01 = pygame.image.load("pictures/banc1.png").convert_alpha()
imageBoat01 = pygame.image.load("pictures/boat1.png").convert_alpha()
imageBoat02 = pygame.image.load("pictures/boat2.png").convert_alpha()
imageMarket01 = pygame.image.load("pictures/market1.png").convert_alpha()
imageMarket02 = pygame.image.load("pictures/market2.png").convert_alpha()
imageRondin01 = pygame.image.load("pictures/rondin1.png").convert_alpha()
imageWheatbag01 = pygame.image.load("pictures/wheatbag1.png").convert_alpha()
imageBigboat01 = pygame.image.load("pictures/bigboat1.png").convert_alpha()
imageForge01 = pygame.image.load("pictures/forge1.png").convert_alpha()
imageGreatmarket01 = pygame.image.load("pictures/greatmarket2.png").convert_alpha()
imageBarrier01 = pygame.image.load("pictures/barrier1.png").convert_alpha()
imagePotato01 = pygame.image.load("pictures/potato1.png").convert_alpha()
imageWatermelon01 = pygame.image.load("pictures/watermelon1.png").convert_alpha()
imagefish01 = pygame.image.load("pictures/fish1.png").convert_alpha()
imagefish02 = pygame.image.load("pictures/fish2.png").convert_alpha()
imageTablegrande01 = pygame.image.load("pictures/tablegrande.png").convert_alpha()
imageChariot01 = pygame.image.load("pictures/chariot1.png").convert_alpha()
imageChariot02 = pygame.image.load("pictures/chariot2.png").convert_alpha()
imagePnj01 = pygame.image.load("pictures/pnj1.png").convert_alpha()
imagePnj02 = pygame.image.load("pictures/pnj2.png").convert_alpha()
imagePnj03 = pygame.image.load("pictures/pnj3.png").convert_alpha()
imagePnj04 = pygame.image.load("pictures/pnj4.png").convert_alpha()
#Dico d'images perso_____________________________________________________________________
imagesPerso = {}

imagesPerso["right"]=[]
imagesPerso["left"]=[]
imagesPerso["down"]=[]
imagesPerso["up"]=[]

temp = pygame.image.load("pictures/persoframes/prot088.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot089.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot090.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot091.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot070.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot071.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot072.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot073.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot079.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot080.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot081.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot082.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot061.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot062.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot063.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("pictures/persoframes/prot064.png").convert_alpha()
imagesPerso["up"].append(temp)
#_______________________________________________________________________________

ianime = 0
imagePerso = imagesPerso["down"][ianime]
rectPerso = imagePerso.get_rect()

perso = {}
perso["rect"]=rectPerso
perso["img"]=imagePerso
perso["direction"]="right"
perso["canshoot"]=True
perso["cooldown"]=0

perso["rect"].x= largeur/2
perso["rect"].y= hauteur/2
horloge = pygame.time.Clock()

#Initialisation du tableau de l'eau

grilleEau = []
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

largeurCaseEau = 33
hauteurCaseEau = 33

# Initialisation du tableau des Plateformes

grillePlateforme = []
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePlateforme.append([0,0,0,0,5,5,0,0,0,0,0,0,0,0])
grillePlateforme.append([0,0,0,0,5,5,0,0,0,0,0,0,0,0])
grillePlateforme.append([0,0,0,3,3,3,3,3,3,3,3,0,0,0])
grillePlateforme.append([0,0,0,3,3,3,3,3,3,3,3,0,0,0])
grillePlateforme.append([1,1,1,3,3,3,3,3,3,3,3,0,0,0])
grillePlateforme.append([0,0,0,3,3,3,3,3,3,3,3,0,0,0])
grillePlateforme.append([0,0,0,3,3,3,3,3,3,3,3,0,0,0])
grillePlateforme.append([0,0,0,2,2,2,2,2,2,2,2,1,1,1])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,5,0,0,0,0])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,5,0,0,0,0])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,5,0,0,0,0])


largeurCase = 75
hauteurCase = 60

#Initialisation du tableau des décors
# 1 puit 2bigboat 3 boat1 4 boat2 5 horloge 6 market1 7 market2 8 wheatbag1 9 rondin 10 banc 11 lampe 12 tonneau
# 13 Forge 14 Greatmarket 15 barrier 19 pnj1 20 pnj2 21 pnj3 22 pnj4
grilledecors = []
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,3,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,2,0,0,0,0])
grilledecors.append([0,0,0,0,11,0,0,14,0,0,11,0,11,0])
grilledecors.append([0,0,0,0,18,0,0,0,20,10,8,10,0,0])
grilledecors.append([0,0,0,0,8,0,0,0,5,0,0,0,19,0])
grilledecors.append([0,0,0,0,0,0,0,13,0,0,0,6,0,0])
grilledecors.append([0,0,0,0,22,0,21,0,0,0,0,7,0,0])
grilledecors.append([0,0,0,0,11,16,16,0,11,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,4,0,0,0,0,0,0])



largeurcaseDecors = 65
hauteurcaseDecors = 60

grilletable = []
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,3,4,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])

largeurcaseTable = 65
hauteurcaseTable = 60
Chat = ''
continuer=1
timer=1;
while continuer:
    horloge.tick(30)
    timer+=1
    touches = pygame.key.get_pressed();

    if touches[pygame.K_ESCAPE] :
        continuer=0
#Zone test ____________________________________________________________________
    print(str(timer))


# Deplacements du perso
    if touches[pygame.K_UP] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["up"])
            imagePerso = imagesPerso["up"][ianime]
        if not(grillePlateforme[int((perso["rect"].y+HauteurPerso/2)/hauteurCase)][int((perso["rect"].x)/largeurCase)]==0) :
            perso["rect"].y-=5
        #else: perso["rect"].y=perso["rect"].y

    if touches[pygame.K_DOWN] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["down"])
            imagePerso = imagesPerso["down"][ianime]
        if not(grillePlateforme[int((perso["rect"].y+HauteurPerso)/hauteurCase)][int((perso["rect"].x)/largeurCase)]==0) :
            perso["rect"].y+=5
        #else: perso["rect"].y=perso["rect"].y


    if touches[pygame.K_RIGHT] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["right"])
            imagePerso = imagesPerso["right"][ianime]
        if int(perso["rect"].y) > int(hauteur/2) :
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x+LargeurPerso)/largeurCase)]==0) :
                perso["rect"].x+=5
        else:
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)+1][int((perso["rect"].x+LargeurPerso)/largeurCase)]==0) :
                perso["rect"].x+=5
        #else: perso["rect"].x=perso["rect"].x

    if touches[pygame.K_LEFT] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["left"])
            imagePerso = imagesPerso["left"][ianime]
        if int(perso["rect"].y) > int(hauteur/2) :
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x-=5
        else:
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)+1][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x-=5
        #else: perso["rect"].x=perso["rect"].x


# On Attribut un chiffre à une image qu'on placera dans une case dans la grille initialisé ci-dessus

    #EAU
    for k in range(len(grilleEau)) :
        for l in range(len(grilleEau[k])) :
            if grilleEau[k][l] == 0 :
                rectMachin1 = imageFond.get_rect()
                rectMachin1.x = l*largeurCaseEau
                rectMachin1.y = k*largeurCaseEau
                fenetre.blit(imageFond, rectMachin1)

    #PLATEFORMES
    for i in range(len(grillePlateforme)) :
        for j in range(len(grillePlateforme[i])) :
            if grillePlateforme[i][j] == 1 :
                rectBidon1 = imagePont01.get_rect()
                rectBidon1.x = j*largeurCase
                rectBidon1.y = i*hauteurCase
                fenetre.blit(imagePont01,rectBidon1)
            if grillePlateforme[i][j] == 2 :
                rectBidon2 = imageMarketplace01.get_rect()
                rectBidon2.x = j*largeurCase
                rectBidon2.y = i*hauteurCase
                fenetre.blit(imageMarketplace01,rectBidon2)
            if grillePlateforme[i][j] == 3 :
                rectBidon3 = imageMarketplace01.get_rect()
                rectBidon3.x = j*largeurCase
                rectBidon3.y = i*hauteurCase
                fenetre.blit(imageMarketplace02,rectBidon3)
            if grillePlateforme[i][j] == 4 :
                rectBidon4 = imageFond.get_rect()
                rectBidon4.x = j*largeurCase
                rectBidon4.y = i*hauteurCase
                fenetre.blit(imageFond,rectBidon4)
            if grillePlateforme[i][j] == 5 :
                rectBidon5 = imagePontvertical01.get_rect()
                rectBidon5.x = j*largeurCase
                rectBidon5.y = i*hauteurCase
                fenetre.blit(imagePontvertical01,rectBidon5)
    #DECORS
    for p in range(len(grilledecors)) :
        for o in range(len(grilledecors[p])) :
            if grilledecors[p][o] == 1 :
                rectDecors1 = imagePuit01.get_rect()
                rectDecors1.x = o*largeurcaseDecors
                rectDecors1.y = p*largeurcaseDecors
                fenetre.blit(imagePuit01, rectDecors1)
            if grilledecors[p][o] == 2 :
                rectDecors2 = imageBigboat01.get_rect()
                rectDecors2.x = o*largeurcaseDecors
                rectDecors2.y = p*largeurcaseDecors
                fenetre.blit(imageBigboat01, rectDecors2)
            if grilledecors[p][o] == 3 :
                rectDecors3 = imageBoat01.get_rect()
                rectDecors3.x = o*largeurcaseDecors
                rectDecors3.y = p*largeurcaseDecors
                fenetre.blit(imageBoat01, rectDecors3)
            if grilledecors[p][o] == 4 :
                rectDecors4 = imageBoat02.get_rect()
                rectDecors4.x = o*largeurcaseDecors
                rectDecors4.y = p*largeurcaseDecors
                fenetre.blit(imageBoat02, rectDecors4)
            if grilledecors[p][o] == 5 :
                rectDecors5 = imageHorloge01.get_rect()
                rectDecors5.x = o*largeurcaseDecors
                rectDecors5.y = p*largeurcaseDecors
                fenetre.blit(imageHorloge01, rectDecors5)
            if grilledecors[p][o] == 6 :
                rectDecors6 = imageMarket01.get_rect()
                rectDecors6.x = o*largeurcaseDecors
                rectDecors6.y = p*largeurcaseDecors
                fenetre.blit(imageMarket01, rectDecors6)
            if grilledecors[p][o] == 7 :
                rectDecors7 = imageMarket02.get_rect()
                rectDecors7.x = o*largeurcaseDecors
                rectDecors7.y = p*largeurcaseDecors
                fenetre.blit(imageMarket02, rectDecors7)
            if grilledecors[p][o] == 8 :
                rectDecors8 = imageWheatbag01.get_rect()
                rectDecors8.x = o*largeurcaseDecors
                rectDecors8.y = p*largeurcaseDecors
                fenetre.blit(imageWheatbag01, rectDecors8)
            if grilledecors[p][o] == 9 :
                rectDecors9 = imageRondin01.get_rect()
                rectDecors9.x = o*largeurcaseDecors
                rectDecors9.y = p*largeurcaseDecors
                fenetre.blit(imageRondin01, rectDecors9)
            if grilledecors[p][o] == 10 :
                rectDecors10 = imageBanc01.get_rect()
                rectDecors10.x = o*largeurcaseDecors
                rectDecors10.y = p*largeurcaseDecors
                fenetre.blit(imageBanc01, rectDecors10)
            if grilledecors[p][o] == 11 :
                rectDecors11 = imageLampe01.get_rect()
                rectDecors11.x = o*largeurcaseDecors
                rectDecors11.y = p*largeurcaseDecors
                fenetre.blit(imageLampe01, rectDecors11)
            if grilledecors[p][o] == 12 :
                rectDecors12 = imageTonneau01.get_rect()
                rectDecors12.x = o*largeurcaseDecors
                rectDecors12.y = p*largeurcaseDecors
                fenetre.blit(imageTonneau01, rectDecors12)
            if grilledecors[p][o] == 13 :
                rectDecors13 = imageForge01.get_rect()
                rectDecors13.x = o*largeurcaseDecors
                rectDecors13.y = p*largeurcaseDecors
                fenetre.blit(imageForge01, rectDecors13)
            if grilledecors[p][o] == 14 :
                rectDecors14 = imageGreatmarket01.get_rect()
                rectDecors14.x = o*largeurcaseDecors
                rectDecors14.y = p*largeurcaseDecors
                fenetre.blit(imageGreatmarket01, rectDecors14)
            if grilledecors[p][o] == 15 :
                rectDecors15 = imageBarrier01.get_rect()
                rectDecors15.x = o*largeurcaseDecors
                rectDecors15.y = p*largeurcaseDecors
                fenetre.blit(imageBarrier01, rectDecors15)
            if grilledecors[p][o] == 16 :
                rectDecors16 = imageTablegrande01.get_rect()
                rectDecors16.x = o*largeurcaseDecors
                rectDecors16.y = p*largeurcaseDecors
                fenetre.blit(imageTablegrande01, rectDecors16)
            if grilledecors[p][o] == 17 :
                rectDecors17 = imageChariot01.get_rect()
                rectDecors17.x = o*largeurcaseDecors
                rectDecors17.y = p*largeurcaseDecors
                fenetre.blit(imageChariot01, rectDecors17)
            if grilledecors[p][o] == 18 :
                rectDecors18 = imageChariot02.get_rect()
                rectDecors18.x = o*largeurcaseDecors
                rectDecors18.y = p*largeurcaseDecors
                fenetre.blit(imageChariot02, rectDecors18)
            if grilledecors[p][o] == 19 :
                rectDecors19 = imagePnj01.get_rect()
                rectDecors19.x = o*largeurcaseDecors
                rectDecors19.y = p*largeurcaseDecors
                fenetre.blit(imagePnj01, rectDecors19)
            if grilledecors[p][o] == 20 :
                rectDecors20 = imagePnj02.get_rect()
                rectDecors20.x = o*largeurcaseDecors
                rectDecors20.y = p*largeurcaseDecors
                fenetre.blit(imagePnj02, rectDecors20)
            if grilledecors[p][o] == 21 :
                rectDecors21 = imagePnj03.get_rect()
                rectDecors21.x = o*largeurcaseDecors
                rectDecors21.y = p*largeurcaseDecors
                fenetre.blit(imagePnj03, rectDecors21)
            if grilledecors[p][o] == 22 :
                rectDecors22 = imagePnj04.get_rect()
                rectDecors22.x = o*largeurcaseDecors
                rectDecors22.y = p*largeurcaseDecors
                fenetre.blit(imagePnj04, rectDecors22)

    for t in range(len(grilletable)) :
        for t1 in range(len(grilletable[t])) :
            if grilletable[t][t1] == 1 :
                rectTable1 = imagePotato01.get_rect()
                rectTable1.x = t1*largeurcaseTable
                rectTable1.y = t*largeurcaseTable
                fenetre.blit(imagePotato01, rectTable1)
            if grilletable[t][t1] == 2 :
                rectTable2 = imageWatermelon01.get_rect()
                rectTable2.x = t1*largeurcaseTable
                rectTable2.y = t*largeurcaseTable
                fenetre.blit(imageWatermelon01, rectTable2)
            if grilletable[t][t1] == 3 :
                rectTable3 = imagefish01.get_rect()
                rectTable3.x = t1*largeurcaseTable
                rectTable3.y = t*largeurcaseTable
                fenetre.blit(imagefish01, rectTable3)
            if grilletable[t][t1] == 4 :
                rectTable4 = imagefish02.get_rect()
                rectTable4.x = t1*largeurcaseTable
                rectTable4.y = t*largeurcaseTable
                fenetre.blit(imagefish02, rectTable4)
    fenetre.blit(imagePerso, perso["rect"])


    if touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors19) :
        Chat = 'Salut, bienvenu a mon échoppe !'
    elif touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors20) :
        Chat = 'Hey, tu viens chasser avec moi ?'
    elif touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors21) :
        Chat = 'Je connais une bonne taverne !'
    elif touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors22) :
        Chat = 'bonjour petite! une friandise ?'
    label = fontChat.render(Chat, 1, (255,255,255))
    fenetre.blit(imageChatbox, rectChatbox)
    fenetre.blit(label, (rectChatbox.x+10, rectChatbox.y+50))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()
