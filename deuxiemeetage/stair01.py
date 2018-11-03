import os
import sys, math, random, pygame
from pygame.locals import *
from pygame import *
import random
pygame.init()
largeur = 1920
hauteur = 1080
modeecran = 0
cdecran = 50
LargeurPerso = 30
HauteurPerso = 50
fontChat = pygame.font.SysFont("monospace", 15)
# fenetre=pygame.display.set_mode((largeur,hauteur))
# fenetre=pygame.display.set_mode((largeur,hauteur), RESIZABLE)
fenetre=pygame.display.set_mode((largeur,hauteur), FULLSCREEN)
rectFenetre = fenetre.get_rect()
imageChatbox = pygame.image.load("pictures/FenetreChat1.png").convert_alpha()
rectChatbox = imageChatbox.get_rect()
rectChatbox.y = 624
imageFond = pygame.image.load("pictures/eau.png").convert_alpha()
imagePont01 = pygame.image.load("pictures/pont01.png").convert_alpha()
imagePont02 = pygame.image.load("pictures/pont2.png").convert_alpha()
imageMarketplace01 = pygame.image.load("pictures/marketplace.png").convert_alpha()
imageMarketplace02 = pygame.image.load("pictures/marketplace3.png").convert_alpha()
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
imageCarquois = pygame.image.load("pictures/Carquois.png").convert_alpha()
imageIconeBag = pygame.image.load("pictures/BagIcon.png").convert_alpha()
rectIconeBag = imageIconeBag.get_rect()
imageInventory = pygame.image.load("pictures/Inventory.png").convert_alpha()
rectInventory = imageInventory.get_rect()
rectInventory.y = 624
imageIconeChat = pygame.image.load("pictures/ChatIcon.png").convert_alpha()
rectIconeChat = imageIconeChat.get_rect()
imageHealthPot01 = pygame.image.load("pictures/pt01.png").convert_alpha()
rectInv01 = imageHealthPot01.get_rect()
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

perso["rect"].x= 450
perso["rect"].y= 300
horloge = pygame.time.Clock()

objet = {}
objet["CodeItem"] = 0
objet["nbItem"] = 0

objets = []
#place dans la grille d inventaire
objet["i"] = -1
objet["j"] = -1
objet["rect"] = rectInv01

grilleInventaire = []
grilleInventaire.append([0,0,0,0,0,0])
grilleInventaire.append([0,0,0,0,0,0])

largeurCaseInv = 45
hauteurCaseInv = 60

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
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])

largeurCase = 33
hauteurCase = 33

#Initialisation du tableau des décors
# 1 puit 2bigboat 3 boat1 4 boat2 5 horloge 6 market1 7 market2 8 wheatbag1 9 rondin 10 banc 11 lampe 12 tonneau
# 13 Forge 14 Greatmarket 15 barrier 19 pnj1 20 pnj2 21 pnj3 22 pnj4

grilledecors = []
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,11,0,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,8,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'C',0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,22,0,0,0,0,0,13,0,0,0,0,0,0,0,7,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,21,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

largeurcaseDecors = 33
hauteurcaseDecors = 33

grilletable = []
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilletable.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


largeurcaseTable = 33
hauteurcaseTable = 33

def getReward(nbItem,CodeItem):
    # ajoutReussi = False
    for i in range(len(grilleInventaire)) :
        for j in range(len(grilleInventaire[i])) :
            if grilleInventaire[i][j] == 0 :
                grilleInventaire[i][j] = CodeItem
                objet["nbItem"] = nbItem
                # nbItem -= 1
                objet["CodeItem"] = CodeItem
                objets.append(objet)

            # if nbItem == 0:
            #     ajoutReussi = True
                return
    # Chat = 'Vous avez besoin de plus de place !'
    # return



Heal = 0
Chat = ''
chatcd = 20
continuer=1
timer=1;
RangerQuest = 0
cdinv = 20
CurrentWindow = 'Chat'
hpBarMax = 200
hp = 200
hpHealed = 0
while continuer:
    horloge.tick(30)
    timer+=1
    touches = pygame.key.get_pressed()
    if touches[pygame.K_TAB] and cdecran ==50 :
        cdcdecran =0
        modeecran = (modeecran + 1)%2
        if modeecran == 0 :
            fenetre=pygame.display.set_mode((1024,768), RESIZABLE)
        else :
            fenetre=pygame.display.set_mode((largeur,hauteur), FULLSCREEN)





    if cdecran<50 :
        cdecran+=1
    if touches[pygame.K_ESCAPE] :
        continuer=0
#Zone test ____________________________________________________________________
    if touches[pygame.K_F1] and hp > 0 :
        hp -= 1

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


#Changement fenetre chat/Inventory
    if CurrentWindow == 'Chat' and cdinv == 20 and pygame.mouse.get_pressed() == (True,False,False):
        if (rectIconeBag).collidepoint(pygame.mouse.get_pos()):
            CurrentWindow = 'Bag'
            cdinv = 0
    elif CurrentWindow == 'Bag' and cdinv == 20 and pygame.mouse.get_pressed() == (True,False,False):
        if (rectIconeChat).collidepoint(pygame.mouse.get_pos()):
            CurrentWindow = 'Chat'
            cdinv = 0
#Utilisation potion
    tempTab = []
    if pygame.mouse.get_pressed() == (True,False,False):
        if (objet["rect"]).collidepoint(pygame.mouse.get_pos()):
            print(str(hp))
            done = False
            for objet in objets :
                if not(done) and objet["CodeItem"] == 1 and objet["nbItem"] > 0 :
                    Heal = 50
                    done = True
                    grilleInventaire[objet["i"]][objet["j"]] = 0
                    objet["nbItem"] -= 1
                if objet["nbItem"] > 0 :
                    tempTab.append(objet)
            objets = tempTab

    if Heal > 0 :
        Heal -= 1
        # hpHealed = 50
        # if hpHealed > 0 :
        hpHealed-=1
        if hp < 200:
            hp = hp+1
    # print(str(cdinv))

    if touches[pygame.K_RCTRL] and CurrentWindow == 'Bag' and cdinv == 20:
        CurrentWindow = 'Chat'
        cdinv = 0
    elif touches[pygame.K_RCTRL] and CurrentWindow == 'Chat' and cdinv == 20:
        CurrentWindow = 'Bag'
        cdinv = 0

    if cdinv < 20 :
        cdinv+=1

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
            fenetre.blit(imagePerso, perso["rect"])
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
            if grilledecors[p][o] == 'C' :
                rectCarquois = imageCarquois.get_rect()
                rectCarquois.x = o*largeurcaseDecors
                rectCarquois.y = p*largeurcaseDecors
                fenetre.blit(imageCarquois, rectCarquois)
                if touches[pygame.K_RETURN] and perso["rect"].colliderect(rectCarquois) :
                    RangerQuest = 1
                    grilledecors[p][o] = 0
                    getReward(1,2)

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
    # if rectCarquois.get_rect().collidepoint(pygame.mouse.get_pos()) and :


    if touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors19) :
            RanChat = random.randint(1,10)
            if RanChat == 1 and chatcd > 20 :
                Chat = """bienvenue a mon échoppe !"""
                chatcd = 0
            elif RanChat == 2 and chatcd > 20 :
                Chat = """fruits & légumes frais ! !"""
                chatcd = 0
            elif RanChat == 3 and chatcd > 20 :
                Chat = """Le maire du bourg est étrange
en ce moment... Tu devrais
peut-êtreparler avec sa fille."""
                chatcd = 0
            elif RanChat == 4 and chatcd > 20 :
                Chat = """La mer est calme, Les légumes
arrivent encore frais en
ce moment ! Pourvu que ça
dure..."""
                chatcd = 0
            elif RanChat == 5 and chatcd > 20 :
                Chat = """Les DJ ont le sens de l'esthétique
n'est-ce pas ?"""
                chatcd = 0
            elif RanChat == 6 and chatcd > 20 :
                Chat = """Mes tomates sont bien rouges !
moins de 10% de peinture
garanti !"""
                chatcd = 0
            elif RanChat == 7 and chatcd > 20 :
                Chat = """Si on m'avait prévenue que de
tenir une échope dans un jeu
était si difficile..."""
                chatcd = 0
            elif RanChat == 8 and chatcd > 20 :
                Chat = """Avant, j'étais décoratrice
d'intérieur. Puis j'ai
reçu une flèche dans
le genou..."""
                chatcd = 0
            elif RanChat == 9 and chatcd > 20 :
                Chat = """Pssst... N'achètes pas de
poisson a ce type là-bas...
soit sa marchandise n'est pas
fraîche, soit c'est le marchand
..."""
                chatcd = 0
            elif RanChat == 10 and chatcd > 20 :
                Chat = """Tu est nouveau dans ce bourg
n'est-ce pas ?"""
                chatcd = 0

    elif touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors20) :
        RanChat = random.randint(1,10)
        if RangerQuest == 1:
            chatcd = 0
            Chat = """Merci !!! Tu viens de sauver plus
de vies que tu ne l'imagines...
Vous obtenez 1 potion de santé"""
            getReward(1,1)
            RangerQuest = 2
        else:
            if RanChat == 1 and chatcd > 20 :
                Chat = """..."""
                chatcd = 0
            elif RanChat == 2 and chatcd > 20 :
                Chat = """Tu le sens aussi, n'est-ce pas ?
Quelquechose flotte dans l'air..."""
                chatcd = 0
            elif RanChat == 3 and chatcd > 20 :
                Chat = """ne juge pas sur les apparences,
la mer a beau être calme,
elle est toujours prête a se
déchainer"""
                chatcd = 0
            elif RanChat == 4 and chatcd > 20 :
                Chat = """J'espère pouvoir enfin
me reposer, avant que les choses
ne dégénèrent encore..."""
                chatcd = 0
            elif RanChat == 5 and chatcd > 20 :
                Chat = """Je viens d'un endroit lointain;
des forêts luxurieuses y
couvrent les plaines gelées...
Ah, ma maison, ma famille..."""
                chatcd = 0
            elif RanChat == 6 and chatcd > 20 :
                Chat = """Profites du calme de ce bourg
tant que tu le peux..."""
                chatcd = 0
            elif RanChat == 7 and chatcd > 20 :
                Chat = """..."""
                chatcd = 0
            elif RanChat == 8 and chatcd > 20 :
                Chat = """Hey, toi, tu pourrais me ramener
mon carquois ? je l'ai oublié aux
abords de la cité alors que je
campais !"""
                chatcd = 0
            elif RanChat == 9 and chatcd > 20 :
                Chat = """Le ciel est dégagé aujourd'hui.
Au moins, nous vivrons un jour
de plus."""
                chatcd = 0
            elif RanChat == 10 and chatcd > 20 and RangerQuest >= 1:
                Chat = """Merci !!! Tu viens de sauver plus
de vies que tu ne l'imagines..."""
                chatcd = 0
    elif touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors21) :
        Chat = 'Je connais une bonne taverne !'
    elif touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors22) :
        Chat = 'bonjour petite! une friandise ?'


    if chatcd < 21 :
        chatcd +=1
    if CurrentWindow == 'Chat':
        rectIconeBag.x = rectChatbox.x+274
        rectIconeBag.y = rectChatbox.y+30
        label = fontChat.render(Chat, 1, (255,255,255))
        fenetre.blit(imageChatbox, rectChatbox)
        x,y = rectChatbox.x+10,rectChatbox.y+20
        fenetre.blit(imageIconeBag, rectIconeBag)
        for ligne in Chat.splitlines():
            x,y = fenetre.blit(fontChat.render(ligne,1,(255,255,255)),(x,y)).bottomleft
            # fenetre.blit(label, (rectChatbox.x+10, rectChatbox.y+50))
    elif CurrentWindow == 'Bag':
        rectIconeChat.x = rectInventory.x+274
        rectIconeChat.y = rectInventory.y+30
        fenetre.blit(imageInventory, rectInventory)
        fenetre.blit(imageIconeChat, rectIconeChat)

        for i in range(len(grilleInventaire)) :
            for j in range(len(grilleInventaire[i])) :
                if grilleInventaire[i][j] == 1 :
                    for objet in objets :
                        if objet["CodeItem"] == 1:

                            objet["rect"] = imageHealthPot01.get_rect()
                            objet["i"] = i
                            objet["j"] = j
                            objet["rect"].x = 10+(j*largeurCaseInv)
                            objet["rect"].y = (rectInventory.y+20)+(i*hauteurCaseInv)
                            fenetre.blit(imageHealthPot01, objet["rect"])
                # elif grilleInventaire[i][j] == 2 :
                #     for objet in objets :
                #         if objet["CodeItem"] == 2:
                #             print(str(grilleInventaire[0][0]))
                #
                #             objet["rect"] = imageCarquois.get_rect()
                #             objet["i"] = i
                #             objet["j"] = j
                #             objet["rect"].x = 10+(j*largeurCaseInv)
                #             objet["rect"].y = (rectInventory.y+20)+(i*hauteurCaseInv)
                #             fenetre.blit(imageCarquois, objet["rect"])
                elif grilleInventaire[i][j] == 2 :
                    rectCarquois = imageCarquois.get_rect()
                    objet["i"] = i
                    objet["j"] = j
                    rectCarquois.x = 10+(j*largeurCaseInv)
                    rectCarquois.y = (rectInventory.y+20)+(i*hauteurCaseInv)
                    fenetre.blit(imageCarquois, rectCarquois)
#Health Bar contour
    pygame.draw.rect(fenetre, (200, 0,255), pygame.Rect(largeur-233, hauteur-(hauteur-35), hpBarMax+4, 14),4)
    #HealthBar
    pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(largeur-230, hauteur-(hauteur-38), hp, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()
