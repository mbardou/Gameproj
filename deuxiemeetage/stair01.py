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
rectChatbox.x = 200
rectChatbox.y = 700
# rectChatbox.x = 0
# rectChatbox.y = (hauteur)-(rectChatbox.h)
imageFond = pygame.image.load("pictures/eau.png").convert_alpha()
imageFond02 = pygame.image.load("pictures/sol/solpierre9.png").convert_alpha()
imageFond03 = pygame.image.load("pictures/sol/solterre11.png").convert_alpha()
imageFond04 = pygame.image.load("pictures/sol/solterre14.png").convert_alpha()
imageFond05 = pygame.image.load("pictures/sol/solterre12.png").convert_alpha()
imageFond06 = pygame.image.load("pictures/sol/solterre13.png").convert_alpha()
imagePont01 = pygame.image.load("pictures/pont01.png").convert_alpha()
imagePont02 = pygame.image.load("pictures/pont2.png").convert_alpha()
imageMarketplace01 = pygame.image.load("pictures/marketplace4.png").convert_alpha()
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
imageMarket03 = pygame.image.load("pictures/market3.png").convert_alpha()
imageRondin01 = pygame.image.load("pictures/rondin1.png").convert_alpha()
imageWheatbag01 = pygame.image.load("pictures/wheatbag1.png").convert_alpha()
imageBigboat01 = pygame.image.load("pictures/bigboat1.png").convert_alpha()
imageForge01 = pygame.image.load("pictures/forge2.png").convert_alpha()
imageGreatmarket01 = pygame.image.load("pictures/greatmarket2.png").convert_alpha()
imageBarrier01 = pygame.image.load("pictures/barrier1.png").convert_alpha()
imagePotato01 = pygame.image.load("pictures/potato1.png").convert_alpha()
imageWatermelon01 = pygame.image.load("pictures/watermelon1.png").convert_alpha()
imagefish01 = pygame.image.load("pictures/fish1.png").convert_alpha()
imagefish02 = pygame.image.load("pictures/fish2.png").convert_alpha()
imageTablegrande01 = pygame.image.load("pictures/tablegrande.png").convert_alpha()
imageChariot01 = pygame.image.load("pictures/chariot1.png").convert_alpha()
imageChariot02 = pygame.image.load("pictures/chariot2.png").convert_alpha()
imageNenu01 = pygame.image.load("pictures/nenu1.png").convert_alpha()
imageNenu02 = pygame.image.load("pictures/nenu2.png").convert_alpha()
imageNenu03 = pygame.image.load("pictures/nenu3.png").convert_alpha()
imageBuisson02 = pygame.image.load("pictures/buisson2.png").convert_alpha()
imageSupplies01= pygame.image.load("pictures/supplies1.png").convert_alpha()
imagePotdefleur01= pygame.image.load("pictures/potdefleur1.png").convert_alpha()
imageTreespooky01 = pygame.image.load("pictures/treespooky1.png").convert_alpha()
imagePnj01 = pygame.image.load("pictures/pnj1.png").convert_alpha()
imagePnj02 = pygame.image.load("pictures/pnj2.png").convert_alpha()
imagePnj03 = pygame.image.load("pictures/pnj3.png").convert_alpha()
imagePnj04 = pygame.image.load("pictures/pnj4.png").convert_alpha()
imagePnj04bas = pygame.image.load("pictures/pnj4bas.png").convert_alpha()
imagePnj04left = pygame.image.load("pictures/pnj4left.png").convert_alpha()
imagePnj05 = pygame.image.load("pictures/pnj5.png").convert_alpha()
imagePnj06 = pygame.image.load("pictures/pnj6.png").convert_alpha()
imageCadavre01 = pygame.image.load("pictures/cadavre1.png").convert_alpha()
imageLitpaille01 = pygame.image.load("pictures/litpaille1.png").convert_alpha()
imageCarquois = pygame.image.load("pictures/Carquois.png").convert_alpha()
imageCane = pygame.image.load("pictures/Cane.png").convert_alpha()
imageIconeBag = pygame.image.load("pictures/BagIcon.png").convert_alpha()
rectIconeBag = imageIconeBag.get_rect()
imageInventory = pygame.image.load("pictures/Inventory.png").convert_alpha()
rectInventory = imageInventory.get_rect()
rectInventory.y = (hauteur)-(rectInventory.h)
imageIconeChat = pygame.image.load("pictures/ChatIcon.png").convert_alpha()
rectIconeChat = imageIconeChat.get_rect()
imageHealthPot01 = pygame.image.load("pictures/pt01.png").convert_alpha()
rectInv01 = imageHealthPot01.get_rect()

# animation de l'ouverture du coffre_____________________________________________________

imagesCoffre = {}

imagesCoffre["fermer"]=[]
imagesCoffre["ouvert"]=[]

temp = pygame.image.load("pictures/coffre1.png").convert_alpha()
imagesCoffre["fermer"].append(temp)
temp = pygame.image.load("pictures/coffre2.png").convert_alpha()
imagesCoffre["ouvert"].append(temp)
# temp = pygame.image.load("pictures/coffre3.png").convert_alpha()
# imagesCoffre["ouvert"].append(temp)

icoffre = 0

imageCoffre = imagesCoffre["fermer"][icoffre]

coffre = {}

coffre["img"] = imageCoffre

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


#Dico image Wolf________________________________________________________________

imagesWolf = {}
imagesWolf["stationnaryup"] = []
imagesWolf["stationnarydown"] = []
imagesWolf["stationnaryleft"] = []
imagesWolf["stationnaryright"] = []
imagesWolf["walkingup"] = []
imagesWolf["walkingdown"] = []
imagesWolf["walkingleft"] = []
imagesWolf["walkingright"] = []
imagesWolf["runup"] = []
imagesWolf["rundown"] = []
imagesWolf["runleft"] = []
imagesWolf["runright"] = []
imagesWolf["attackup"] = []
imagesWolf["attackdown"] = []
imagesWolf["attackleft"] = []
imagesWolf["attackright"] = []
imagesWolf["sleepup"] = []
imagesWolf["sleepdown"] = []
imagesWolf["sleepleft"] = []
imagesWolf["sleepright"] = []

#WOLFSTATIONNARY__________________________________________________________
temp = pygame.image.load("pictures/wolf/wolfstationnaryup1.png").convert_alpha()
imagesWolf["stationnaryup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnarydown1.png").convert_alpha()
imagesWolf["stationnarydown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnarydown2.png").convert_alpha()
imagesWolf["stationnarydown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnarydown3.png").convert_alpha()
imagesWolf["stationnarydown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnarydown4.png").convert_alpha()
imagesWolf["stationnarydown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnarydown5.png").convert_alpha()
imagesWolf["stationnarydown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryleft1.png").convert_alpha()
imagesWolf["stationnaryleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryleft2.png").convert_alpha()
imagesWolf["stationnaryleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryleft3.png").convert_alpha()
imagesWolf["stationnaryleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryleft4.png").convert_alpha()
imagesWolf["stationnaryleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryright1.png").convert_alpha()
imagesWolf["stationnaryright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryright2.png").convert_alpha()
imagesWolf["stationnaryright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryright3.png").convert_alpha()
imagesWolf["stationnaryright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfstationnaryright4.png").convert_alpha()
imagesWolf["stationnaryright"].append(temp)

#WOLFWALK_________________________________________________________________
temp = pygame.image.load("pictures/wolf/wolfwalkingup1.png").convert_alpha()
imagesWolf["walkingup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingup2.png").convert_alpha()
imagesWolf["walkingup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingup3.png").convert_alpha()
imagesWolf["walkingup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingup4.png").convert_alpha()
imagesWolf["walkingup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingdown1.png").convert_alpha()
imagesWolf["walkingdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingdown2.png").convert_alpha()
imagesWolf["walkingdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingdown3.png").convert_alpha()
imagesWolf["walkingdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingdown4.png").convert_alpha()
imagesWolf["walkingdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingleft1.png").convert_alpha()
imagesWolf["walkingleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingleft2.png").convert_alpha()
imagesWolf["walkingleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingleft3.png").convert_alpha()
imagesWolf["walkingleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingleft4.png").convert_alpha()
imagesWolf["walkingleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingleft5.png").convert_alpha()
imagesWolf["walkingleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingright1.png").convert_alpha()
imagesWolf["walkingright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingright2.png").convert_alpha()
imagesWolf["walkingright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingright3.png").convert_alpha()
imagesWolf["walkingright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingright4.png").convert_alpha()
imagesWolf["walkingright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfwalkingright5.png").convert_alpha()
imagesWolf["walkingright"].append(temp)

#WOLFRUN__________________________________________________________________
temp = pygame.image.load("pictures/wolf/wolfrunup1.png").convert_alpha()
imagesWolf["runup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunup2.png").convert_alpha()
imagesWolf["runup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunup3.png").convert_alpha()
imagesWolf["runup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunup4.png").convert_alpha()
imagesWolf["runup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunup5.png").convert_alpha()
imagesWolf["runup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrundown1.png").convert_alpha()
imagesWolf["rundown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrundown2.png").convert_alpha()
imagesWolf["rundown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrundown3.png").convert_alpha()
imagesWolf["rundown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrundown4.png").convert_alpha()
imagesWolf["rundown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrundown5.png").convert_alpha()
imagesWolf["rundown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunleft1.png").convert_alpha()
imagesWolf["runleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunleft2.png").convert_alpha()
imagesWolf["runleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunleft3.png").convert_alpha()
imagesWolf["runleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunleft4.png").convert_alpha()
imagesWolf["runleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunleft5.png").convert_alpha()
imagesWolf["runleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunright1.png").convert_alpha()
imagesWolf["runright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunright2.png").convert_alpha()
imagesWolf["runright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunright3.png").convert_alpha()
imagesWolf["runright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunright4.png").convert_alpha()
imagesWolf["runright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfrunright5.png").convert_alpha()
imagesWolf["runright"].append(temp)

#WOLFATTACK_______________________________________________________________
temp = pygame.image.load("pictures/wolf/wolfattackup1.png").convert_alpha()
imagesWolf["attackup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackup2.png").convert_alpha()
imagesWolf["attackup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackup3.png").convert_alpha()
imagesWolf["attackup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackup4.png").convert_alpha()
imagesWolf["attackup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackup5.png").convert_alpha()
imagesWolf["attackup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackdown1.png").convert_alpha()
imagesWolf["attackdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackdown2.png").convert_alpha()
imagesWolf["attackdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackdown3.png").convert_alpha()
imagesWolf["attackdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackdown4.png").convert_alpha()
imagesWolf["attackdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackdown5.png").convert_alpha()
imagesWolf["attackdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackleft1.png").convert_alpha()
imagesWolf["attackleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackleft2.png").convert_alpha()
imagesWolf["attackleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackleft3.png").convert_alpha()
imagesWolf["attackleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackleft4.png").convert_alpha()
imagesWolf["attackleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackleft5.png").convert_alpha()
imagesWolf["attackleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackright1.png").convert_alpha()
imagesWolf["attackright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackright2.png").convert_alpha()
imagesWolf["attackright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackright3.png").convert_alpha()
imagesWolf["attackright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackright4.png").convert_alpha()
imagesWolf["attackright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfattackright5.png").convert_alpha()
imagesWolf["attackright"].append(temp)

#WOLFSLEEP________________________________________________________________
temp = pygame.image.load("pictures/wolf/wolfsleepup1.png").convert_alpha()
imagesWolf["sleepup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepup2.png").convert_alpha()
imagesWolf["sleepup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepup3.png").convert_alpha()
imagesWolf["sleepup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepup4.png").convert_alpha()
imagesWolf["sleepup"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepdown1.png").convert_alpha()
imagesWolf["sleepdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepdown2.png").convert_alpha()
imagesWolf["sleepdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepdown3.png").convert_alpha()
imagesWolf["sleepdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepdown4.png").convert_alpha()
imagesWolf["sleepdown"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepleft1.png").convert_alpha()
imagesWolf["sleepleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepleft2.png").convert_alpha()
imagesWolf["sleepleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepleft3.png").convert_alpha()
imagesWolf["sleepleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepleft4.png").convert_alpha()
imagesWolf["sleepleft"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepright1.png").convert_alpha()
imagesWolf["sleepright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepright2.png").convert_alpha()
imagesWolf["sleepright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepright3.png").convert_alpha()
imagesWolf["sleepright"].append(temp)
temp = pygame.image.load("pictures/wolf/wolfsleepright4.png").convert_alpha()
imagesWolf["sleepright"].append(temp)


#_______________________________________________________________________________

iwolf = 0

imageWolf = imagesWolf["sleepleft"][iwolf]

wolf = {}

wolf["img"] = imageWolf

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
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grilleEau.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
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
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
grillePlateforme.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
largeurCase = 33
hauteurCase = 33

#Initialisation du tableau des décors
# 1 puit 2bigboat 3 boat1 4 boat2 5 horloge 6 market1 7 market2 8 wheatbag1 9 rondin 10 banc 11 lampe 12 tonneau
# 13 Forge 14 Greatmarket 15 barrier 16 tablegrande 17chariot1 18 chariot2 19 pnj1 20 pnj2 21 pnj3 22 pnj4 'C' carquois "Cane" Cane
# 23 Nenu1 24 Nenu2 25 Nenu3 26 market3 27 buisson2 28 supplies1 29 pnj4bas 30 pnj5 31 pnj4left 32 pnj6 33 cadavre1
# 34 potdefleur 35 litpaille1 36 coffre 37 treespooky1 38 wolf

grilledecors = []
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,11,0,14,0,0,0,0,29,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,11,0,26,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,8,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,28,0,0,'Cane',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,20,0,0,0,0,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,12,0,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,0,0,0,0,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,27,27,27,27,0,0,0,0,0,0,'C',0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,27,27,27,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,36,0,0,0,7,0,0,11,0,23,0,0,24,0,0,0,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,0,0,0,0,0,0,25,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,21,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,24,0,0,0,23,0,0,17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,37,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,27,27,27,27,0,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,27,27,27,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,37,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,33,0,0,0,0,0,0,0,0,0,0,0,37,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
# grilledecors.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,33,0,0,0,0,0,0,0,0,0,0,37,0,0,0,0,0,0,0,0,0,0,0])


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
# def changemonde():
    # with open("stair02.txt") as f:
    #     for line in f:
    #         grilledecors[].append(line)
    # contenu = mon_fichier.read()
    # grille[]
    # if perso["rect"].colliderect(rectDecors38):
    #     fenetre.blit(mon_fichier)
with open("decorsville.txt") as f:
    for line in f:
        tabLigne = line.split()
        #print (line)
        #print (tabLigne)
        newLine=[]
        for c in tabLigne :
            newLine.append(int(c))
        print (newLine)
        grilledecors.append(newLine)


Heal = 0
Chat = ''
chatcd = 20
continuer=1
timer=1
RangerQuest = 0
fishermanQuest = 0
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
            largeur = 1024
            hauteur = 768
            rectInventory.y = (hauteur)-(rectInventory.h)
            rectChatbox.y = (hauteur)-(rectChatbox.h)
            fenetre=pygame.display.set_mode((largeur,hauteur), FULLSCREEN)
        else :
            largeur = 1920
            hauteur = 1080
            rectInventory.y = (hauteur)-(rectInventory.h)
            rectChatbox.y = (hauteur)-(rectChatbox.h)
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
                    # grilleInventaire[objet["i"]][objet["j"]] = 0
                    objet["nbItem"] -= 1
                if objet["nbItem"] > 0 :
                    tempTab.append(objet)
                else :
                    grilleInventaire[objet["i"]][objet["j"]] = 0
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

    #FOND
    for k in range(len(grilleEau)) :
        for l in range(len(grilleEau[k])) :
            if grilleEau[k][l] == 0 :
                rectFond1 = imageFond.get_rect()
                rectFond1.x = l*largeurCaseEau
                rectFond1.y = k*largeurCaseEau
                fenetre.blit(imageFond, rectFond1)
            if grilleEau[k][l] == 1 :
                rectFond2 = imageFond02.get_rect()
                rectFond2.x = l*largeurCaseEau
                rectFond2.y = k*largeurCaseEau
                fenetre.blit(imageFond02, rectFond2)
            if grilleEau[k][l] == 2 :
                rectFond3 = imageFond03.get_rect()
                rectFond3.x = l*largeurCaseEau
                rectFond3.y = k*largeurCaseEau
                fenetre.blit(imageFond03, rectFond3)
            if grilleEau[k][l] == 3 :
                rectFond4 = imageFond04.get_rect()
                rectFond4.x = l*largeurCaseEau
                rectFond4.y = k*largeurCaseEau
                fenetre.blit(imageFond04, rectFond4)
            if grilleEau[k][l] == 4 :
                rectFond5 = imageFond05.get_rect()
                rectFond5.x = l*largeurCaseEau
                rectFond5.y = k*largeurCaseEau
                fenetre.blit(imageFond05, rectFond5)
            if grilleEau[k][l] == 5 :
                rectFond6 = imageFond06.get_rect()
                rectFond6.x = l*largeurCaseEau
                rectFond6.y = k*largeurCaseEau
                fenetre.blit(imageFond06, rectFond6)

    #PLATEFORMES
    for i in range(len(grillePlateforme)) :
        for j in range(len(grillePlateforme[i])) :
            if grillePlateforme[i][j] == 1 :
                rectPlateforme1 = imagePont01.get_rect()
                rectPlateforme1.x = j*largeurCase
                rectPlateforme1.y = i*hauteurCase
                fenetre.blit(imagePont01,rectPlateforme1)
            if grillePlateforme[i][j] == 2 :
                rectPlateforme2 = imageMarketplace01.get_rect()
                rectPlateforme2.x = j*largeurCase
                rectPlateforme2.y = i*hauteurCase
                fenetre.blit(imageMarketplace01,rectPlateforme2)
            if grillePlateforme[i][j] == 3 :
                rectPlateforme3 = imageMarketplace01.get_rect()
                rectPlateforme3.x = j*largeurCase
                rectPlateforme3.y = i*hauteurCase
                fenetre.blit(imageMarketplace02,rectPlateforme3)
            if grillePlateforme[i][j] == 4 :
                rectPlateforme4 = imageFond.get_rect()
                rectPlateforme4.x = j*largeurCase
                rectPlateforme4.y = i*hauteurCase
                fenetre.blit(imageFond,rectPlateforme4)
            if grillePlateforme[i][j] == 5 :
                rectPlateforme5 = imagePontvertical01.get_rect()
                rectPlateforme5.x = j*largeurCase
                rectPlateforme5.y = i*hauteurCase
                fenetre.blit(imagePontvertical01,rectPlateforme5)
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
            if grilledecors[p][o] == 23 :
                rectDecors23 = imageNenu01.get_rect()
                rectDecors23.x = o*largeurcaseDecors
                rectDecors23.y = p*largeurcaseDecors
                fenetre.blit(imageNenu01, rectDecors23)
            if grilledecors[p][o] == 24 :
                rectDecors24 = imageNenu02.get_rect()
                rectDecors24.x = o*largeurcaseDecors
                rectDecors24.y = p*largeurcaseDecors
                fenetre.blit(imageNenu02, rectDecors24)
            if grilledecors[p][o] == 25 :
                rectDecors25 = imageNenu03.get_rect()
                rectDecors25.x = o*largeurcaseDecors
                rectDecors25.y = p*largeurcaseDecors
                fenetre.blit(imageNenu03, rectDecors25)
            if grilledecors[p][o] == 26 :
                rectDecors26 = imageMarket03.get_rect()
                rectDecors26.x = o*largeurcaseDecors
                rectDecors26.y = p*largeurcaseDecors
                fenetre.blit(imageMarket03, rectDecors26)
            if grilledecors[p][o] == 27 :
                rectDecors27 = imageBuisson02.get_rect()
                rectDecors27.x = o*largeurcaseDecors
                rectDecors27.y = p*largeurcaseDecors
                fenetre.blit(imageBuisson02, rectDecors27)
            if grilledecors[p][o] == 28 :
                rectDecors28 = imageSupplies01.get_rect()
                rectDecors28.x = o*largeurcaseDecors
                rectDecors28.y = p*largeurcaseDecors
                fenetre.blit(imageSupplies01, rectDecors28)
            if grilledecors[p][o] == 29 :
                rectDecors29 = imagePnj04bas.get_rect()
                rectDecors29.x = o*largeurcaseDecors
                rectDecors29.y = p*largeurcaseDecors
                fenetre.blit(imagePnj04bas, rectDecors29)
            if grilledecors[p][o] == 30 :
                rectDecors30 = imagePnj05.get_rect()
                rectDecors30.x = o*largeurcaseDecors
                rectDecors30.y = p*largeurcaseDecors
                fenetre.blit(imagePnj05, rectDecors30)
            if grilledecors[p][o] == 31 :
                rectDecors31 = imagePnj04left.get_rect()
                rectDecors31.x = o*largeurcaseDecors
                rectDecors31.y = p*largeurcaseDecors
                fenetre.blit(imagePnj04left, rectDecors31)
            if grilledecors[p][o] == 32 :
                rectDecors32 = imagePnj06.get_rect()
                rectDecors32.x = o*largeurcaseDecors
                rectDecors32.y = p*largeurcaseDecors
                fenetre.blit(imagePnj06, rectDecors32)
            if grilledecors[p][o] == 33 :
                rectDecors33 = imageCadavre01.get_rect()
                rectDecors33.x = o*largeurcaseDecors
                rectDecors33.y = p*largeurcaseDecors
                fenetre.blit(imageCadavre01, rectDecors33)
            if grilledecors[p][o] == 34 :
                rectDecors34 = imagePotdefleur01.get_rect()
                rectDecors34.x = o*largeurcaseDecors
                rectDecors34.y = p*largeurcaseDecors
                fenetre.blit(imagePotdefleur01, rectDecors34)
            if grilledecors[p][o] == 35 :
                rectDecors35 = imageLitpaille01.get_rect()
                rectDecors35.x = o*largeurcaseDecors
                rectDecors35.y = p*largeurcaseDecors
                fenetre.blit(imageLitpaille01, rectDecors35)
            if grilledecors[p][o] == 36 :
                rectDecors36 = imageCoffre.get_rect()
                rectDecors36.x = o*largeurcaseDecors
                rectDecors36.y = p*largeurcaseDecors
                fenetre.blit(imageCoffre, rectDecors36)
                if touches[pygame.K_SPACE] and perso["rect"].colliderect(rectDecors36) :
                    if timer%2==0:
                        icoffre = (icoffre+1)%len(imagesCoffre["ouvert"])
                        imageCoffre = imagesCoffre["ouvert"][icoffre]
                elif not(perso["rect"].colliderect(rectDecors36)) :
                    imageCoffre = imagesCoffre["fermer"][icoffre]
            if grilledecors[p][o] == 37 :
                rectDecors37 = imageTreespooky01.get_rect()
                rectDecors37.x = o*largeurcaseDecors
                rectDecors37.y = p*largeurcaseDecors
                fenetre.blit(imageTreespooky01, rectDecors37)
            if grilledecors[p][o] == 39 :
                rectCarquois = imageCarquois.get_rect()
                rectCarquois.x = o*largeurcaseDecors
                rectCarquois.y = p*largeurcaseDecors
                fenetre.blit(imageCarquois, rectCarquois)
                if touches[pygame.K_RETURN] and perso["rect"].colliderect(rectCarquois) :
                    RangerQuest = 1
                    grilledecors[p][o] = 0
                    getReward(1,2)
            if grilledecors[p][o] == 40 :
                rectCane = imageCane.get_rect()
                rectCane.x = o*largeurcaseDecors
                rectCane.y = p*largeurcaseDecors
                fenetre.blit(imageCane, rectCane)
                if touches[pygame.K_RETURN] and perso["rect"].colliderect(rectCane) :
                    fishermanQuest = 2
                    grilledecors[p][o] = 0
                    getReward(1,3)
            if grilledecors[p][o] == 38 :
                rectDecors38 = imageWolf.get_rect()
                rectDecors38.x = o*largeurcaseDecors
                rectDecors38.y = p*largeurcaseDecors
                fenetre.blit(imageWolf, rectDecors38)
                if touches[pygame.K_SPACE] and perso["rect"].colliderect(rectDecors38) :
                    if timer%2==0:
                        iwolf = (iwolf+1)%len(imagesWolf["sleepleft"])
                        imageWolf = imagesWolf["sleepleft"][iwolf]



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
    if touches[pygame.K_RETURN] and perso["rect"].colliderect(rectDecors21) :
            RanChat = random.randint(1,10)
            if fishermanQuest == 2:
                chatcd = 0
                Chat = """Merci ! le plus dur n'est pas
de l'attrapper, mais de le vendre!
j'en ai mal au dos! Maintenant
prends cette canne, et attrapes
moi n'importe quoi !"""

                fishermanQuest = 3


            if RanChat == 1 and chatcd > 20 :
                Chat = """L'air est frais aujourd'hui !"""
                chatcd = 0
            elif RanChat == 2 and chatcd > 20 :
                Chat = """La mer n'a jamais été
aussi calme ! Les poissons
sautent presque dans nos bras !"""
                chatcd = 0
            elif RanChat == 3 and chatcd > 20 :
                Chat = """Y'a peut-être pas d'arrêtes
dans le beefsteak mais mon
poisson est riche en Oméga 3 !"""
                chatcd = 0
            elif RanChat == 4 and chatcd > 20 and fishermanQuest <= 1:
                Chat = """Comment ça tu ne sais pas
pêcher ? Va me chercher ma canne
et je t'apprendrai les secrets
du métier !"""
                fishermanQuest = 1

                chatcd = 0
            elif RanChat == 5 and chatcd > 20 :
                Chat = """IL EST FRAIS MON POISSON !"""
                chatcd = 0

            elif RanChat == 6 and chatcd > 20 and fishermanQuest <= 1:
                Chat = """Comment ça tu ne sais pas
pêcher ? Va me chercher ma canne
et je t'apprendrai les secrets
du métier !"""
                fishermanQuest = 1
                chatcd = 0

            elif RanChat == 7 and chatcd > 20 :
                Chat = """Hey toi ! tu veux voir mon
plus grand secret ? La voici:
Une botte secrète de 65cm de
long ! imagine les péniches
de la bête !!!"""
                chatcd = 0
            elif RanChat == 8 and chatcd > 20 :
                Chat = """Tu penses que les poissons
pierre existaient déjà durant
l'âge de pierre ?"""
                chatcd = 0
            elif RanChat == 9 and chatcd > 20 :
                Chat = """Devines : les oursins sont
les petits des ours
ou des oursons ?"""
                chatcd = 0
            elif RanChat == 10 and chatcd > 20 :
                Chat = """J'ai pêché un requin marteau
l'année dèrniere. On m'a dit
qu'ils ne valaient
pas un clou !"""
                chatcd = 0

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

                elif grilleInventaire[i][j] == 3 :
                    rectCane = imageCane.get_rect()
                    objet["i"] = i
                    objet["j"] = j
                    rectCane.x = 10+(j*largeurCaseInv)
                    rectCane.y = (rectInventory.y+20)+(i*hauteurCaseInv)
                    fenetre.blit(imageCane, rectCane)
#Health Bar contour
    pygame.draw.rect(fenetre, (200, 0,255), pygame.Rect(largeur-233, hauteur-(hauteur-35), hpBarMax+4, 14),4)
    #HealthBar
    pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(largeur-230, hauteur-(hauteur-38), hp, 10))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()
