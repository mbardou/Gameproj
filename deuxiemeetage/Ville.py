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
# fenetre=pygame.display.set_mode((largeur,hauteur),HWSURFACE|DOUBLEBUF|RESIZABLE)
fenetre=pygame.display.set_mode((largeur,hauteur), FULLSCREEN)
# rectFenetre = fenetre.get_rect()
imageChatbox = pygame.image.load("pictures/FenetreChat1.png").convert_alpha()
rectChatbox = imageChatbox.get_rect()
rectChatbox.x = 200
rectChatbox.y = 700
# rectChatbox.x = 0
# rectChatbox.y = (hauteur)-(rectChatbox.h)
# imageFond = pygame.image.load("pictures/sol/marecage1.png").convert_alpha()
# imageFond01 = pygame.image.load("pictures/sol/marecage2.png").convert_alpha()
imageFond = pygame.image.load("pictures/eau.png").convert_alpha()
imageFond02 = pygame.image.load("pictures/sol/solpierre9.png").convert_alpha()
imageFond03 = pygame.image.load("pictures/sol/solterre11.png").convert_alpha()
imageFond04 = pygame.image.load("pictures/sol/solterre14.png").convert_alpha()
imageFond05 = pygame.image.load("pictures/sol/solterre12.png").convert_alpha()
imageFond06 = pygame.image.load("pictures/sol/solterre13.png").convert_alpha()
imageFond07 = pygame.image.load("pictures/sol/solpierre10.png").convert_alpha()
imageFond08 = pygame.image.load("pictures/sol/solpierre11.png").convert_alpha()
imageFond09 = pygame.image.load("pictures/sol/solterre17.png").convert_alpha()
imageFond10 = pygame.image.load("pictures/sol/solcurse1.png").convert_alpha()
imageFond11 = pygame.image.load("pictures/sol/soldust1.png").convert_alpha()
imageFond12 = pygame.image.load("pictures/sol/solpierre15.png").convert_alpha()
imageHerbe01 = pygame.image.load("pictures/herbe1.png").convert_alpha()
imagePont01 = pygame.image.load("pictures/pont01.png").convert_alpha()
imagePont02 = pygame.image.load("pictures/pont2.png").convert_alpha()
imagePont03 = pygame.image.load("pictures/pont3.png").convert_alpha()
imagePont04 = pygame.image.load("pictures/pont4.png").convert_alpha()
imageIlot01 = pygame.image.load("pictures/ilot1.png").convert_alpha()
imageMarketplace01 = pygame.image.load("pictures/marketplace4.png").convert_alpha()
imageMarketplace02 = pygame.image.load("pictures/marketplace3.png").convert_alpha()
imagePontvertical01 = pygame.image.load("pictures/pontvertical01.png").convert_alpha()
imageHorloge01 = pygame.image.load("pictures/horloge2.png").convert_alpha()
imagePuit01 = pygame.image.load("pictures/puit1.png").convert_alpha()
imageTonneau01 = pygame.image.load("pictures/tonneau1.png").convert_alpha()
imageTonneau02 = pygame.image.load("pictures/tonneau2.png").convert_alpha()
imageLampe01 = pygame.image.load("pictures/lampe2.png").convert_alpha()
imageBanc01 = pygame.image.load("pictures/banc1.png").convert_alpha()
imageBoat01 = pygame.image.load("pictures/boat1.png").convert_alpha()
imageBoat02 = pygame.image.load("pictures/boat2.png").convert_alpha()
imageMarket01 = pygame.image.load("pictures/market1.png").convert_alpha()
imageMarket02 = pygame.image.load("pictures/market2.png").convert_alpha()
imageMarket03 = pygame.image.load("pictures/market3.png").convert_alpha()
imageRondin01 = pygame.image.load("pictures/rondin1.png").convert_alpha()
imageTree02 = pygame.image.load("pictures/tree3.png").convert_alpha()
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
imageBarrier02 = pygame.image.load("pictures/barrier2.png").convert_alpha()
imageCaisse01 = pygame.image.load("pictures/caisse2.png").convert_alpha()
imagePnj01 = pygame.image.load("pictures/pnj1.png").convert_alpha()
imagePnj02 = pygame.image.load("pictures/pnj2.png").convert_alpha()
imagePnj03 = pygame.image.load("pictures/pnj3.png").convert_alpha()
imagePnj04 = pygame.image.load("pictures/pnj4.png").convert_alpha()
imagePnj04bas = pygame.image.load("pictures/pnj4bas.png").convert_alpha()
imagePnj04left = pygame.image.load("pictures/pnj4left.png").convert_alpha()
imagePnj05 = pygame.image.load("pictures/pnj5.png").convert_alpha()
imagePnj06 = pygame.image.load("pictures/pnj6.png").convert_alpha()
imagePnj07 = pygame.image.load("pictures/pnj7.png").convert_alpha()
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
imagePortebarrier = pygame.image.load("pictures/portebarrier2.png").convert_alpha()
imageBarrier03 = pygame.image.load("pictures/barrier3.png").convert_alpha()
imageBarrier04 = pygame.image.load("pictures/barrier5.png").convert_alpha()
imageTombe01 = pygame.image.load("pictures/tombe1.png").convert_alpha()
imageTombe02 = pygame.image.load("pictures/tombe2.png").convert_alpha()
imageTombe03 = pygame.image.load("pictures/tombe3.png").convert_alpha()
imageTombe04 = pygame.image.load("pictures/tombe4.png").convert_alpha()
imageLampe02 = pygame.image.load("pictures/lampe3.png").convert_alpha()
imageCampement01 = pygame.image.load("pictures/campement1.png").convert_alpha()
imageTree03 = pygame.image.load("pictures/tree4.png").convert_alpha()
imageBonfire01 = pygame.image.load("pictures/bonfire1.png").convert_alpha()
imageTree04 = pygame.image.load("pictures/tree5.png").convert_alpha()
imageTree05 = pygame.image.load("pictures/tree6.png").convert_alpha()
imageFlaquedeau01 = pygame.image.load("pictures/flaquedeau1.png").convert_alpha()
imageRondincut01 = pygame.image.load("pictures/rondincut1.png").convert_alpha()
# imageRondincut02 = pygame.image.load("pictures/rondincut2.png").convert_alpha()
imageSquelette01 = pygame.image.load("pictures/zs/sk01.png").convert_alpha()
imageBuisson03 = pygame.image.load("pictures/buisson3.png").convert_alpha()
imagePnjdown08 = pygame.image.load("pictures/pnj8left.png").convert_alpha()
imagePnjright08 = pygame.image.load("pictures/pnj8right.png").convert_alpha()
imagePnjleft08 = pygame.image.load("pictures/pnj8down.png").convert_alpha()
imageTree06 = pygame.image.load("pictures/tree7.png").convert_alpha()
imagePont05a = pygame.image.load("pictures/pont5a.png").convert_alpha()
imagePont05b = pygame.image.load("pictures/pont5b.png").convert_alpha()
imagePont05c = pygame.image.load("pictures/pont5c.png").convert_alpha()
imagePont05d = pygame.image.load("pictures/pont5d.png").convert_alpha()
imagePont05e = pygame.image.load("pictures/pont5e.png").convert_alpha()
imagePont05f = pygame.image.load("pictures/pont5f.png").convert_alpha()
rectCarquois2 = imageCarquois.get_rect()


# animation de l'ouverture du coffre_____________________________________________________

imagesCoffre = {}

imagesCoffre["fermer"]=[]
imagesCoffre["ouvert"]=[]

temp = pygame.image.load("pictures/coffre1.png").convert_alpha()
imagesCoffre["fermer"].append(temp)
temp = pygame.image.load("pictures/coffre2.png").convert_alpha()
imagesCoffre["ouvert"].append(temp)

icoffre = 0
imageCoffre = imagesCoffre["fermer"][icoffre]

coffre = {}

coffre["img"] = imageCoffre

# animation de l'ouverture de poubelle___________________________________________________

imagesTrash = {}

imagesTrash["fermer"]=[]
imagesTrash["ouvert"]=[]

temp = pygame.image.load("pictures/trash1.png").convert_alpha()
imagesTrash["fermer"].append(temp)
temp = pygame.image.load("pictures/trash2.png").convert_alpha()
imagesTrash["ouvert"].append(temp)

itrash = 0
imageTrash = imagesTrash["fermer"][itrash]

trash = {}

trash["img"] = imageTrash

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
imagesCGblob = {}

imagesCGblob["proj"]=[]
temp = pygame.image.load("pictures/CGblob01.png").convert_alpha()
imagesCGblob["proj"].append(temp)
temp = pygame.image.load("pictures/CG02.png").convert_alpha()
imagesCGblob["proj"].append(temp)



imagesBlob = {}

imagesBlob["left"]=[]
imagesBlob["right"]=[]

temp = pygame.image.load("blobframes/idle/blob01.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob02.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob03.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob04.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob05.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob06.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob07.png").convert_alpha()
imagesBlob["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blob08.png").convert_alpha()
imagesBlob["left"].append(temp)


imageCGblob = pygame.image.load("pictures/CGblob01.png").convert_alpha()


imagesBlobf = {}

imagesBlobf["left"]=[]
imagesBlobf["right"]=[]

temp = pygame.image.load("blobframes/idle/blobf01.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf02.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf03.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf04.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf05.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf06.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf07.png").convert_alpha()
imagesBlobf["left"].append(temp)
temp = pygame.image.load("blobframes/idle/blobf08.png").convert_alpha()
imagesBlobf["left"].append(temp)

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
rectPersounvirgulecinq = imagePerso.get_rect()
perso = {}
perso["rect"]=rectPerso
perso["img"]=imagePerso
perso["direction"]="right"
perso["canshoot"]=True
perso["cooldown"]=0

perso["rect"].x= 1300
perso["rect"].y= 750

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

#Initialisation du tableau des Fonds

grilleFond = []

largeurCaseEau = 33
hauteurCaseEau = 33

# Initialisation du tableau des Plateformes

grillePlateforme = []

largeurCase = 33
hauteurCase = 33

#Initialisation du tableau des décors
# 1 puit 2bigboat 3 boat1 4 boat2 5 horloge 6 market1 7 market2 8 wheatbag1 9 rondin 10 banc 11 lampe 12 tonneau
# 13 Forge 14 Greatmarket 15 barrier 16 tablegrande 17chariot1 18 chariot2 19 pnj1 20 pnj2 21 pnj3 22 pnj4 'C' carquois "Cane" Cane
# 23 Nenu1 24 Nenu2 25 Nenu3 26 market3 27 buisson2 28 supplies1 29 pnj4bas 30 pnj5 31 pnj4left 32 pnj6 33 cadavre1
# 34 potdefleur 35 litpaille1 36 coffre 37 treespooky1 38 wolf

grilledecors = []

largeurcaseDecors = 33
hauteurcaseDecors = 33

grilletable = []

largeurcaseTable = 33
hauteurcaseTable = 33


def Position(myRect):
    myRect.x = j*largeurCase -xf
    myRect.y = i*hauteurCase -yf
    if not ((myRect.x < 0 or myRect.x > largeur ) or ( myRect.y > hauteur or myRect.y < 0)) :
        fenetre.blit(img,myRect)


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
#APPEL DES GRILLES DE DIFFERENTS FICHIER TEXTE______________________________________
with open("decorsville.txt") as f:
    for line in f:
        tabLigne = line.split()
        newLine=[]
        for c in tabLigne :
            newLine.append(int(c))
        grilledecors.append(newLine)

with open("fondville.txt") as f :
    for line in f :
        tabLigne = line.split()
        newLine = []
        for c in tabLigne :
            newLine.append(int(c))
        grilleFond.append(newLine)

with open("plateforme.txt") as f :
    for line in f :
        tabLigne = line.split()
        newLine = []
        for c in tabLigne :
            newLine.append(int(c))
        grillePlateforme.append(newLine)

with open("table.txt") as f :
    for line in f :
        tabLigne = line.split()
        newLine = []
        for c in tabLigne :
            newLine.append(int(c))
        grilletable.append(newLine)

#_______________________________________________________________________________
score_font = pygame.font.Font(None, 30)
couleur_font = (255,0,0)
xf = 0
yf = 0

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
cdmg = 50
dedouble = 0
i=0

ianimeblobf = 0
ianimeblob = 0
ianimeblobCG = 0
imageblob = imagesBlob["left"][ianimeblob]
imageblobf = imagesBlobf["left"][ianimeblobf]
imagePerso = imagesPerso["up"][ianime]
rectCGblob = imageCGblob.get_rect()
pvblob = 50
tirs = []
blobs = []
tirsblob = []

rectBlob = imageblob.get_rect()
blob = {}

blob["nom"] = "Bob"
blob["pv"] = pvblob
blob["rect"] = rectBlob
blob["nbBlob"] = 2
blob["vitesse"] = 4
cdblob = 20
dirblob = 0
newblobx = 0
newbloby = 0
newnbBlob = 0
rectBlob01 = imageblob.get_rect()
rectBlob02 = imageblob.get_rect()
maskPerso = pygame.mask.from_surface(imagePerso)
maskBlob = pygame.mask.from_surface(imageblob)
blob["rect"].x = 2000
blob["rect"].y = 600
blobs.append(blob)
rectbone = imageCGblob.get_rect()
tab = []
lvl = 0
while continuer:
    horloge.tick(30)
    timer+=1
    touches = pygame.key.get_pressed()

    if (RangerQuest==2 and lvl== 0):
        lvl = 1
        # grillePlateforme = tab
        with open("stairs01.txt") as f :
            for line in f :
                tabLigne = line.split()
                newLine = []
                for c in tabLigne :
                    newLine.append(int(c))
                grillePlateforme.append(newLine)

        grilletable = tab
        # grilleFond = tab
        grilledecors = tab
        print("nimp")

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
    for b in blobs :
        if rectPerso.x > b["rect"].x:
            b["rect"].x += b["vitesse"]
        if rectPerso.x < b["rect"].x :
            b["rect"].x -= b["vitesse"]
        if rectPerso.y > b["rect"].y:
            b["rect"].y += b["vitesse"]
        if rectPerso.y < b["rect"].y:
            b["rect"].y -= b["vitesse"]

    for ti in tirsblob :
        if ti["direction"] == 4:
                ti["rect"].y -=  20
        if ti["direction"] == 5:
                ti["rect"].x +=  15
                ti["rect"].y -= 15
        if ti["direction"] == 6:
                ti["rect"].x += 20
        if ti["direction"] == 7:
                ti["rect"].x +=  15
                ti["rect"].y += 15
        if ti["direction"] == 8:
                ti["rect"].y += 20
        if ti["direction"] == 9:
                ti["rect"].x -=  15
                ti["rect"].y += 15
        if ti["direction"] == 10:
                ti["rect"].x -= 20
        if ti["direction"] == 11:
                ti["rect"].x -=  15
                ti["rect"].y -= 15

    for t in tirsblob :
        if t["rect"].colliderect(perso["rect"]):
            hp-=10

    tempTablob = []
    for ti in tirsblob:
        if not(ti["rect"].x > perso["rect"].x+largeur/2 or ti["rect"].x < perso["rect"].x - largeur/2  or ti["rect"].y > perso["rect"].y + hauteur/2 or ti["rect"].y<perso["rect"].y - hauteur/2) :
            tempTablob.append(ti)
    tirsblob = tempTablob

    for b in blobs :
        if  cdblob == 20 and b["nom"] == "fürher":
            if ((perso["rect"].x > b["rect"].x and (perso["rect"].x - b["rect"].x) < 300) or (perso["rect"].x < b["rect"].x and (b["rect"].x - perso["rect"].x) < 300)) :
                cdblob = 0
                rectbone = imageCGblob.get_rect()
                rectbone.x = b["rect"].x
                rectbone.y = b["rect"].y
                if perso["rect"].x < b["rect"].x and perso["rect"].y < b["rect"].y:
                    dirblob = 11
                if perso["rect"].x < b["rect"].x and perso["rect"].y == b["rect"].y:
                    dirblob = 10
                if perso["rect"].x < b["rect"].x and perso["rect"].y > b["rect"].y:
                    dirblob = 9
                if perso["rect"].x == b["rect"].x and perso["rect"].y > b["rect"].y:
                    dirblob = 8
                if perso["rect"].x > b["rect"].x and perso["rect"].y > b["rect"].y:
                    dirblob = 7
                if perso["rect"].x > b["rect"].x and perso["rect"].y == b["rect"].y:
                    dirblob = 6
                if perso["rect"].x > b["rect"].x and perso["rect"].y < b["rect"].y:
                    dirblob = 5
                if perso["rect"].x == b["rect"].x and perso["rect"].y < b["rect"].y:
                    dirblob = 4

                tirblob = {}
                tirblob["canhit"] = True
                tirblob["rect"] = rectbone
                tirblob["direction"] = dirblob



                tirsblob.append(tirblob)
    if cdblob < 20 :
        cdblob +=1


    for blob in blobs :
        if maskPerso.overlap(maskBlob, (blob["rect"].left - perso["rect"].left, blob["rect"].top - perso["rect"].top)) != None:
            if cdmg == 50 :
                hp -= 10
                cdmg = 0
    if cdmg < 50 :
        cdmg +=1
    #Affiche le score en bas à droite quand le projectil et le blob ce touche
    for t in tirs:
        for blob in blobs :
            if t["rect"].colliderect(blob["rect"]) :
                if t["canhit"] == True:
                    blob["pv"] -= 10
                    t["canhit"] = False
                    t["touche"] = 0
    temptablob = []
    for b in blobs :
        if b["pv"] <= 0 :
            b["nbBlob"] -= 1
            if b["nbBlob"] >=1:
                dedouble = 1

    if dedouble == 1 :
        for b in blobs:
            if b["pv"] <= 0  and b["nbBlob"] >= 1:
                newblobx = b["rect"].x + 20
                newbloby = b["rect"].y + 20
                newnbBlob = b["nbBlob"]
        b01 = {}
        b01["nom"] = "fürher"
        b01["rect"] = rectBlob01
        b01["rect"].x = newblobx
        b01["rect"].y = newbloby
        b01["nbBlob"] = newnbBlob
        b01["pv"] = 80
        b01["vitesse"] = 2
        blobs.append(b01)

        b02 = {}
        b02["nom"] = "Blobby"
        b02["rect"] = rectBlob02
        b02["rect"].x = newblobx-30
        b02["rect"].y = newbloby-30
        b02["nbBlob"] = newnbBlob
        b02["pv"] = 40
        b02["vitesse"] = 6
        blobs.append(b02)

        print(str(blobs))

    dedouble = 0

    for blob in blobs :
        if blob["pv"] > 0 and blob["nbBlob"] >= 1 :
            temptablob.append(blob)
    blobs = temptablob
        # fenetre.blit(imageFond, rectFond)
        # display.update(rectBlob)
        #modification du score
    #     score_surface = score_font.render("Score : {:5d} points".format(points), 1, couleur_font)


    score_surface = score_font.render("Pvblob : {:5d} Pvblob".format(blob["pv"]), 1, couleur_font)


    if i%3==0 :
        ianimeblob = (ianimeblob+1)%len(imagesBlob["left"])
        imageblob = imagesBlob["left"][ianimeblob]
        ianimeblobCG = (ianimeblobCG+1)%len(imagesCGblob["proj"])
        imageCGblob = imagesCGblob["proj"][ianimeblobCG]
        # ianimebone = (ianimebone+1)%len(imagesbone["proj"])
        # imagebone = imagesbone["proj"][ianimebone]
        ianimeblobf = (ianimeblobf+1)%len(imagesBlobf["left"])
        imageblobf = imagesBlobf["left"][ianimeblobf]






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
            perso["rect"].y-=25
        elif not(grilleFond[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
            perso["rect"].y-=25
        #else: perso["rect"].y=perso["rect"].y

    if touches[pygame.K_DOWN] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["down"])
            imagePerso = imagesPerso["down"][ianime]
        if not(grillePlateforme[int((perso["rect"].y+HauteurPerso+100)/hauteurCase)][int((perso["rect"].x)/largeurCase)]==0) :
            perso["rect"].y+=25
        elif not(grilleFond[int((perso["rect"].y+100)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
            perso["rect"].y+=25
        #else: perso["rect"].y=perso["rect"].y


    if touches[pygame.K_RIGHT] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["right"])
            imagePerso = imagesPerso["right"][ianime]
        if int(perso["rect"].y) > int(hauteur/2) :
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x+LargeurPerso)/largeurCase)]==0) :
                perso["rect"].x+=25
            elif not(grilleFond[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x+=25
        else:
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)+1][int((perso["rect"].x+LargeurPerso)/largeurCase)]==0) :
                perso["rect"].x+=25
            elif not(grilleFond[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x+=25
        #else: perso["rect"].x=perso["rect"].x

    if touches[pygame.K_LEFT] :
        if timer%5==0 :
            ianime = (ianime+1)%len(imagesPerso["left"])
            imagePerso = imagesPerso["left"][ianime]
        if int(perso["rect"].y) > int(hauteur/2) :
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x-=25
            elif not(grilleFond[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x-=25
        else:
            if not(grillePlateforme[int((perso["rect"].y)/hauteurCase)+1][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x-=25
            elif not(grilleFond[int((perso["rect"].y)/hauteurCase)][int((perso["rect"].x-6)/largeurCase)]==0) :
                perso["rect"].x-=25
        #else: perso["rect"].x=perso["rect"].x


    if touches[pygame.K_SPACE] and perso["canshoot"] :
        rectCarquois2 = imageCarquois.get_rect()
        rectCarquois2.x = perso["rect"].x
        rectCarquois2.y = perso["rect"].y

        if touches[pygame.K_UP] :
            dirbone = 0
        elif touches[pygame.K_RIGHT] :
            dirbone = 1
        elif touches[pygame.K_DOWN] :
            dirbone = 2
        elif touches[pygame.K_LEFT] :
            dirbone = 3
        else :
            dirbone = 4


        tir = {}
        tir["canhit"] = True
        tir["rect"] = rectCarquois2
        tir["direction"] = dirbone
        tir["touche"] = 1


        tirs.append(tir)
        perso["canshoot"] = False
        perso["cooldown"] = 0

    if perso["canshoot"] == False:
        perso["cooldown"] += 1
        if perso["cooldown"] > 8 :
            perso["canshoot"] = True



    for t in tirs:
        if t["direction"] == 0:
                t["rect"].y += - 20
        if t["direction"] == 1:
                t["rect"].x += + 20
        if t["direction"] == 2:
                t["rect"].y += + 20
        if t["direction"] == 3:
                t["rect"].x += - 20

    tempTab = []
    for t in tirs:
        if not(t["rect"].x > perso["rect"].x+largeur/2 or t["rect"].x < perso["rect"].x - largeur/2 or t["rect"].y > perso["rect"].y + hauteur/2 or t["rect"].y<perso["rect"].y - hauteur/2) and t["touche"]==1 :
            tempTab.append(t)
    tirs = tempTab
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

    xf = perso["rect"].x -largeur/2
    yf = perso["rect"].y -hauteur/2

    rectPersounvirgulecinq.x =  perso["rect"].x - xf
    rectPersounvirgulecinq.y = perso["rect"].y -yf
    # pygame.draw.rect(fenetre, (0, 0, 255), perso["rect"])
    # pygame.draw.rect(fenetre, (0, 255, 0), rectPersounvirgulecinq)
    # rectPersounvirgulecinq.x = largeur/2
    # rectPersounvirgulecinq.y = hauteur/2

# On Attribut un chiffre à une image qu'on placera dans une case dans la grille initialisé ci-dessus
    #FOND
    myRect = imageFond.get_rect()

    for i in range(len(grilleFond)) :
        for j in range(len(grilleFond[i])) :
            img = 0
            if grilleFond[i][j] == 0 :
                img = imageFond

            if grilleFond[i][j] == 1 :
                img = imageFond02

            if grilleFond[i][j] == 2 :
                img = imageFond03

            if grilleFond[i][j] == 3 :
                img = imageFond04

            if grilleFond[i][j] == 4 :
                img = imageFond05

            if grilleFond[i][j] == 5 :
                img = imageFond06

            if grilleFond[i][j] == 6 :
                img = imageFond07

            if grilleFond[i][j] == 7 :
                img = imageFond08

            if grilleFond[i][j] == 8 :
                img = imageFond09

            if grilleFond[i][j] == 9 :
                img = imageFond10

            if grilleFond[i][j] == 10 :
                img = imageFond11

            if grilleFond[i][j] == 11 :
                img = imageFond12




            if not img == 0 :
                Position(myRect)

    #PLATEFORMES
    for i in range(len(grillePlateforme)) :
        for j in range(len(grillePlateforme[i])) :
            img = 0
            if grillePlateforme[i][j] == 1 :
                img = imagePont01

            if grillePlateforme[i][j] == 2 :
                img = imageMarketplace01

            if grillePlateforme[i][j] == 3 :
                img = imageMarketplace01

            if grillePlateforme[i][j] == 4 :
                img = imageFond

            if grillePlateforme[i][j] == 5 :
                img = imagePontvertical01

            if grillePlateforme[i][j] == 6 :
                img = imageIlot01

            if grillePlateforme[i][j] == 7 :
                img = imagePont03
            if grillePlateforme[i][j] == 8 :
                img = imageBonfire01

            if grillePlateforme[i][j] == 9 :
                img = imagePont05a
            if grillePlateforme[i][j] == 10 :
                img = imagePont05b
            if grillePlateforme[i][j] == 11 :
                img = imagePont05c
            if grillePlateforme[i][j] == 12 :
                img = imagePont05d
            if grillePlateforme[i][j] == 13 :
                img = imagePont05e
            if grillePlateforme[i][j] == 14 :
                img = imagePont05f

            if not img == 0 :
                Position(myRect)

    #DECORS
    for i in range(len(grilledecors)) :
        for j in range(len(grilledecors[i])) :
            img = 0
            if grilledecors[i][j] == 1 :
                img = imagePuit01

            if grilledecors[i][j] == 2 :
                img = imageBigboat01

            if grilledecors[i][j] == 3 :
                img = imageBoat01

            if grilledecors[i][j] == 4 :
                img = imageBoat02

            if grilledecors[i][j] == 5 :
                img = imageHorloge01

            if grilledecors[i][j] == 6 :
                img = imageMarket01

            if grilledecors[i][j] == 7 :
                img = imageMarket02

            if grilledecors[i][j] == 8 :
                img = imageWheatbag01

            if grilledecors[i][j] == 9 :
                img = imageRondin01

            if grilledecors[i][j] == 10 :
                img = imageBanc01

            if grilledecors[i][j] == 11 :
                img = imageLampe01

            if grilledecors[i][j] == 12 :
                img = imageTonneau01

            if grilledecors[i][j] == 13 :
                img = imageForge01

            if grilledecors[i][j] == 14 :
                img = imageGreatmarket01

            if grilledecors[i][j] == 15 :
                img = imageBarrier01

            if grilledecors[i][j] == 16 :
                img = imageTablegrande01

            if grilledecors[i][j] == 17 :
                img = imageChariot01

            if grilledecors[i][j] == 18 :
                img = imageChariot02

            if grilledecors[i][j] == 19 :
                rectDecors19 = imagePnj01.get_rect()
                rectDecors19.x = j*largeurcaseDecors -xf
                rectDecors19.y = i*largeurcaseDecors -yf
                fenetre.blit(imagePnj01, rectDecors19)

            if grilledecors[i][j] == 20 :
                rectDecors20 = imagePnj02.get_rect()
                rectDecors20.x = j*largeurcaseDecors -xf
                rectDecors20.y = i*largeurcaseDecors -yf
                fenetre.blit(imagePnj02, rectDecors20)

            if grilledecors[i][j] == 21 :
                rectDecors21 = imagePnj03.get_rect()
                rectDecors21.x = j*largeurcaseDecors -xf
                rectDecors21.y = i*largeurcaseDecors -yf
                fenetre.blit(imagePnj03, rectDecors21)

            if grilledecors[i][j] == 22 :
                rectDecors22 = imagePnj04.get_rect()
                rectDecors22.x = j*largeurcaseDecors -xf
                rectDecors22.y = i*largeurcaseDecors -yf
                fenetre.blit(imagePnj04, rectDecors22)

            if grilledecors[i][j] == 23 :
                img = imageNenu01

            if grilledecors[i][j] == 24 :
                img = imageNenu02

            if grilledecors[i][j] == 25 :
                img = imageNenu03

            if grilledecors[i][j] == 26 :
                img = imageMarket03

            if grilledecors[i][j] == 27 :
                img = imageBuisson02

            if grilledecors[i][j] == 28 :
                img = imageSupplies01

            if grilledecors[i][j] == 29 :
                img = imagePnj04bas

            if grilledecors[i][j] == 30 :
                img = imagePnj05

            if grilledecors[i][j] == 31 :
                img = imagePnj04left

            if grilledecors[i][j] == 32 :
                img = imagePnj06

            if grilledecors[i][j] == 33 :
                img = imageCadavre01

            if grilledecors[i][j] == 34 :
                img = imageiotdefleur01

            if grilledecors[i][j] == 35 :
                img = imageLitpaille01

            if grilledecors[i][j] == 36 :
                rectDecors36 = imageCoffre.get_rect()
                rectDecors36.x = j*largeurcaseDecors -xf
                rectDecors36.y = i*hauteurcaseDecors -yf
                fenetre.blit(imageCoffre, rectDecors36)
                if touches[pygame.K_SPACE] and rectPersounvirgulecinq.colliderect(rectDecors36) :
                    if timer%2==0:
                        icoffre = (icoffre+1)%len(imagesCoffre["ouvert"])
                        imageCoffre = imagesCoffre["ouvert"][icoffre]
                elif not(rectPersounvirgulecinq.colliderect(rectDecors36)) :
                    imageCoffre = imagesCoffre["fermer"][icoffre]

            if grilledecors[i][j] == 37 :
                rectDecors37 = imageTreesiooky01

            if grilledecors[i][j] == 38 :
                rectDecors38 = imageWolf.get_rect()
                rectDecors38.x = j*largeurcaseDecors -xf
                rectDecors38.y = i*largeurcaseDecors -yf
                fenetre.blit(imageWolf, rectDecors38)
                if touches[pygame.K_SPACE] and rectPersounvirgulecinq.colliderect(rectDecors38) :
                    if timer%2==0:
                        iwolf = (iwolf+1)%len(imagesWolf["sleepleft"])
                        imageWolf = imagesWolf["sleepleft"][iwolf]

            if grilledecors[i][j] == 39 :
                rectDecors = imageCarquois
                rectCarquois = imageCarquois.get_rect()
                rectCarquois.x = j*largeurcaseDecors -xf
                rectCarquois.y = i*largeurcaseDecors -yf
                fenetre.blit(imageCarquois, rectCarquois)
                if touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectCarquois) :
                    RangerQuest = 1
                    grilledecors[i][j] = 0
                    getReward(1,2)
            if grilledecors[i][j] == 40 :
                rectCane = imageCane.get_rect()
                rectCane.x = j*largeurcaseDecors -xf
                rectCane.y = i*largeurcaseDecors -yf
                fenetre.blit(imageCane, rectCane)
                if touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectCane) :
                    fishermanQuest = 2
                    grilledecors[i][j] = 0
                    getReward(1,3)

            if grilledecors[i][j] == 41 :
                img = imageBarrier02

            if grilledecors[i][j] == 42 :
                rectDecors42 = imageTrash.get_rect()
                rectDecors42.x = j*largeurcaseDecors -xf
                rectDecors42.y = i*largeurcaseDecors -yf
                fenetre.blit(imageTrash, rectDecors42)
                if touches[pygame.K_SPACE] and rectPersounvirgulecinq.colliderect(rectDecors42) :
                    if timer%2==0:
                        itrash = (itrash+1)%len(imagesTrash["ouvert"])
                        imageTrash = imagesTrash["ouvert"][itrash]
                elif not(rectPersounvirgulecinq.colliderect(rectDecors42)) :
                    imageTrash = imagesTrash["fermer"][itrash]

            if grilledecors[i][j] == 43 :
                img = imageCaisse01
            if grilledecors[i][j] == 44 :
                img = imageTree02
            if grilledecors[i][j] == 45 :
                img = imageTonneau02
            if grilledecors[i][j] == 46 :
                img = imagePortebarrier
            if grilledecors[i][j] == 47 :
                img = imageBarrier03
            if grilledecors[i][j] == 48 :
                img = imageBarrier04
            if grilledecors[i][j] == 49 :
                img = imageTombe01
            if grilledecors[i][j] == 50 :
                img = imageLampe02
            if grilledecors[i][j] == 51 :
                img = imageCampement01
            if grilledecors[i][j] == 52 :
                img = imageHerbe01
            if grilledecors[i][j] == 53 :
                img = imageTree03
            if grilledecors[i][j] == 54 :
                img = imageBonfire01
            if grilledecors[i][j] == 55 :
                img = imageTree04
            if grilledecors[i][j] == 56 :
                img = imageTree05
            if grilledecors[i][j] == 57 :
                rectDecors57 = imagePnj07.get_rect()
                rectDecors57.x = j*largeurcaseDecors -xf
                rectDecors57.y = i*largeurcaseDecors -yf
                fenetre.blit(imagePnj07, rectDecors57)
            if grilledecors[i][j] == 58 :
                img = imageFlaquedeau01
            if grilledecors[i][j] == 59 :
                img = imageTombe02
            if grilledecors[i][j] == 60 :
                img = imageTombe03
            if grilledecors[i][j] == 61 :
                img = imageTombe04
            if grilledecors[i][j] == 62 :
                img = imageRondincut01
            # if grilledecors[i][j] == 63 :
            #     img = imageRondincut02
            if grilledecors[i][j] == 64 :
                img = imageSquelette01
            if grilledecors[i][j] == 65 :
                img = imageBuisson03
            if grilledecors[i][j] == 66 :
                rectDecors66 = imagePnjright08.get_rect()
                rectDecors66.x = j*largeurcaseDecors -xf
                rectDecors66.y = i*largeurcaseDecors -yf
                fenetre.blit(imagePnjright08, rectDecors66)
            if grilledecors[i][j] == 67 :
                img = imagePnjdown08
            if grilledecors[i][j] == 68 :
                img = imagePnjleft08
            if grilledecors[i][j] == 69 :
                img = imageTree06


            if not img == 0 :
                Position(myRect)


    for i in range(len(grilletable)) :
        for j in range(len(grilletable[i])) :
            img = 0
            if grilletable[i][j] == 1 :
                img = imagePotato01
            if grilletable[i][j] == 2 :
                img = imageWatermelon01
            if grilletable[i][j] == 3 :
                img = imagefish01
            if grilletable[i][j] == 4 :
                img = imagefish02
            if not img == 0 :
                Position(myRect)
    for t in tirs:
        fenetre.blit(imageCarquois, (t["rect"].x-xf,t["rect"].y-yf))
    # if rectCarquois.get_rect().collidepoint(pygame.mouse.get_pos()) and :
    for blob in blobs :
            if blob["nom"] == "fürher" :
                fenetre.blit(imageblobf, (blob["rect"].x-xf,blob["rect"].y-yf))
            else :
                fenetre.blit(imageblob, (blob["rect"].x-xf,blob["rect"].y-yf))

            for ti in tirsblob:
                if ti["direction"] > -1:
                    fenetre.blit(imageCGblob, (ti["rect"].x-xf,ti["rect"].y-yf))
    fenetre.blit(imagePerso, (perso["rect"].x - xf, perso["rect"].y -yf))


    if touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectDecors19) :
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

    elif touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectDecors57) :
                RanChat = random.randint(1,10)
                if RanChat == 1 and chatcd > 20 :
                    Chat = """Vous là bas,
il serait préférable pour vous
de rebrousser chemin
..."""
                    chatcd = 0
                elif RanChat == 2 and chatcd > 20 :
                    Chat = """Suite aux plaintes des habitants,
mon supérieur ...
m'a ordonné d'enquêter
sur ce cimetière ..."""
                    chatcd = 0
                elif RanChat == 3 and chatcd > 20 :
                    Chat = """Quelque chose à reveiller les morts
...
Ils en rodent partout
dans ces lieux """
                    chatcd = 0
                elif RanChat == 4 and chatcd > 20 :
                    Chat = """Certains tombent en mer
...
et leur corps flottent
tout le long du village """
                    chatcd = 0
                elif RanChat == 5 and chatcd > 20 :
                    Chat = """ M m m MOI, p pe PEUR
...
JE SUIS UN COURAGEUX chevalier,
je réglerai ce problème
u u une fois que
...
j'aurais finis thé"""
                    chatcd = 0

    elif touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectDecors20) :
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
    if touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectDecors21) :
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

    elif touches[pygame.K_RETURN] and rectPersounvirgulecinq.colliderect(rectDecors66) :
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
