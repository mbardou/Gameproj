import os
import sys, math, random, pygame
from pygame.locals import *
from pygame import *

pygame.init()

#Création de la fenetre

largeur = 1024
hauteur = 768
# fenetre = pygame.display.set_mode((largeur,hauteur))
fenetre=pygame.display.set_mode((largeur,hauteur), RESIZABLE)
rectFenetre = fenetre.get_rect()

score_font = pygame.font.Font(None, 30)
couleur_font = (255,0,0)

fontChat = pygame.font.SysFont("monospace", 15)
# lecture de l'image du perso
#Dico des images---------------------------------------------------------
#boneproj---------------------------------------------------------------
#faire dictionnaire :

bones = []
bonestir = []
tirs=[]
blobs = []

imagesbone = {}

imagesbone["proj"]=[]
temp = pygame.image.load("boneframes/femur.png").convert_alpha()
imagesbone["proj"].append(temp)
temp = pygame.image.load("boneframes/femur02.png").convert_alpha()
imagesbone["proj"].append(temp)
temp = pygame.image.load("boneframes/femur03.png").convert_alpha()
imagesbone["proj"].append(temp)
temp = pygame.image.load("boneframes/femur04.png").convert_alpha()
imagesbone["proj"].append(temp)







#blob---------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------
#animations perso---------------------------------------------------------------------
imagesPersoH20 = {}

imagesPersoH20["face"]=[]

temp = pygame.image.load("PersoH20frames/persofaceplonge.png").convert_alpha()
imagesPersoH20["face"].append(temp)
temp = pygame.image.load("PersoH20frames/persofaceplonge02.png").convert_alpha()
imagesPersoH20["face"].append(temp)

imagesPerso = {}

imagesPerso["right"]=[]
imagesPerso["left"]=[]
imagesPerso["down"]=[]
imagesPerso["up"]=[]

temp = pygame.image.load("persoframes/perso1.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoframes/persoright02.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoframes/persoright03.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoframes/persoright04.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoframes/persoleft.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoframes/persoleft02.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoframes/persoleft03.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoframes/persoleft04.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoframes/persoface.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persoframes/persodown02.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persoframes/persodown03.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persoframes/persodown04.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persoframes/persoup.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("persoframes/persoup02.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("persoframes/persoup03.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("persoframes/persoup04.png").convert_alpha()
imagesPerso["up"].append(temp)
#fin du dico --------------------------------------------------------------
imageSword = pygame.image.load("swordpics/sword1.png").convert_alpha()
imagebone = pygame.image.load("boneframes/femur.png").convert_alpha()
imageGrille = pygame.image.load("gridpics/GrilleComplete.png").convert_alpha()
imageHacheDeZoo = pygame.image.load("HacheDeZoo2.png").convert_alpha()
imageTree = pygame.image.load("tree1.png").convert_alpha()

#images inv chat_____________________________________________________________________
imageIconeBag = pygame.image.load("pictures/BagIcon.png").convert_alpha()
rectIconeBag = imageIconeBag.get_rect()
imageInventory = pygame.image.load("pictures/Inventory.png").convert_alpha()
rectInventory = imageInventory.get_rect()
rectInventory.y = 624
imageIconeChat = pygame.image.load("pictures/ChatIcon.png").convert_alpha()
rectIconeChat = imageIconeChat.get_rect()
imageHealthPot01 = pygame.image.load("pictures/pt01.png").convert_alpha()
rectInv01 = imageHealthPot01.get_rect()

imageChatbox = pygame.image.load("pictures/FenetreChat1.png").convert_alpha()
rectChatbox = imageChatbox.get_rect()
rectChatbox.x = 0
rectChatbox.y = 624

ianimeblob = 0
ianime = 0
ianimebone = 0
pvblob = 50
imageblob = imagesBlob["left"][ianimeblob]
imagePerso = imagesPerso["up"][ianime]

rectPerso = imagePerso.get_rect()
rectbone = imagebone.get_rect()

perso = {}
perso["rect"]=rectPerso
perso["img"]=imagePerso
perso["direction"]="right"
perso["canshoot"]=True
perso["cooldown"]=0



#dico blob______________________________________________________________________
rectBlob = imageblob.get_rect()
blob = {}


blob["pv"] = pvblob
blob["rect"] = rectBlob
blob["upstairs"] = 0
blob["nbBlob"] = 2
blob["vitesse"] = 4


# rectBlob2 = imageblob.get_rect()
# blob2 = {}
#
#
# blob2["pv"] = pvblob
# blob2["rect"] = rectBlob2
# blob2["upstairs"] = 0
# blob2["nbBlob"] = 2
# blob2["vitesse"] = 4

#_______________________________________________________________________________
# creation d'un rectangle pour positioner l'image du personnage
blob["rect"].x = 240
blob["rect"].y = 120
blobs.append(blob)

# blob2["rect"].x = 500
# blob2["rect"].y = 120
# blobs.append(blob2)






perso["rect"].x = hauteur/2
perso["rect"].y = largeur/2
rectSword = imageSword.get_rect()

rectHacheDeZoo = imageHacheDeZoo.get_rect()
rectHacheDeZoo.x = 684
rectHacheDeZoo.y = 480

# rectSword = imageSword.get_rect()
# rectSword.x = 2000
# rectSword.y = 2000

rectGrille = imageGrille.get_rect()
rectGrille.x = 0
rectGrille.y = 0
# lecture de l'image du fond
imageFond = pygame.image.load("fond1.png").convert()

# creation d'un rectangle pour positioner l'image du fond
rectFond = imageFond.get_rect()
rectFond.x = 0
rectFond.y = 0


rectTree = imageTree.get_rect()
rectTree.x = 300
rectTree.y = 600
## Ajoutons un texte fixe dans la fenetre :
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)

# Creation de l'image correspondant au texte
imageText = font.render('Collision', True, (255, 255, 55))


# creation d'un rectangle pour positioner l'image du texte
rectText = imageText.get_rect()
rectText.x = 10
rectText.y = 10

maskPerso = pygame.mask.from_surface(imagePerso)
maskBlob = pygame.mask.from_surface(imageblob)

# Positionnement de la surface pour le score
score_surface = score_font.render("Pvblob : {:6d} pv".format(blob["pv"]), 1, couleur_font)
score_rect = score_surface.get_rect()
score_rect.bottomright = rectFenetre.bottomright



# servira a regler l'horloge du jeu
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
#fct GET REWARD
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

# la boucle infinie dans laquelle on reste coince
i=1
continuer=1
#perso en haut de la grille = 1 en dessous =0
upstairsperso = 0
#regule UPSTAIRS
vartour = -1
#direction projectile os du PERSO
dirbone = -1
#pour plongeon(en attente, garder au cas ou...)
# Pressed = 0
#verifie si entité dans l'EAU
inwater = 0
#hp MAX du PERSO
hpBarMax = 200
#hp actuels du PERSO
hp = 200
#hp PERSO affichés (au cas ou hp < 0, hpAffiche = 0)
hpAffiche = hp
#cooldown degats au personnage
cdmg =50
#dedouble le blob si il meurt avec nbBlob>1
dedouble = 0
newblobx = 0
newbloby = 0
newnbBlob = 0
rectBlob01 = imageblob.get_rect()
rectBlob02 = imageblob.get_rect()
#ajoute 2 potions a l inventaire (pour tester)
donnepotion = 0
#compte les Hp pour la potion
Heal = 0
#initialise str a mettre dans chat
Chat = ''
#switch fenetre
CurrentWindow = 'Chat'
#cd chat
chatcd = 20
#compte hp pour potion
hpHealed = 0
#cd inventaire
cdinv = 20
cdpot = 50
while continuer:
    # print("je peux tirer ? "+str(perso["canshoot"]))

    horloge.tick(30)

    i= i+1;
    #print (i)
    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0
    if perso["rect"].x > 624 and perso["rect"].y > 390 :
        inwater = 1
    else : inwater = 0
#DEPLACE BLOB____________________________________________________________


    for b in blobs :
        if rectPerso.x > b["rect"].x:
            b["rect"].x += b["vitesse"]
        if rectPerso.x < b["rect"].x :
            b["rect"].x -= b["vitesse"]
        if rectPerso.y > b["rect"].y:
            b["rect"].y += b["vitesse"]
        if rectPerso.y < b["rect"].y:
            b["rect"].y -= b["vitesse"]









#______________________________________________________________________

        # rafraichissement
    # Affichage du Texte
    fenetre.blit(imageText, rectText)


    if touches[pygame.K_UP] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["up"])
            imagePerso = imagesPerso["up"][ianime]
        if perso["rect"].y < 1 :
           perso["rect"].y = 0
        else :
            if inwater==1 :
                perso["rect"].y = perso["rect"].y - 5
            else :
                perso["rect"].y = perso["rect"].y - 12

    if touches[pygame.K_DOWN] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["down"])
            imagePerso = imagesPerso["down"][ianime]
        if perso["rect"].y > 616 :
            perso["rect"].y = 617
        if perso["rect"].x < 760 and perso["rect"].x >= 480 and perso["rect"].y > 110 and upstairsperso ==1 :
            perso["rect"].y = 111
        if perso["rect"].x < 525 and perso["rect"].x >= 0 and perso["rect"].y > 215 and upstairsperso ==1 :
            perso["rect"].y = 216
        else :
            if inwater==1 :
                perso["rect"].y = perso["rect"].y + 5
            else :
                perso["rect"].y = perso["rect"].y + 12


    if touches[pygame.K_LEFT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["left"])
            imagePerso = imagesPerso["left"][ianime]
        if perso["rect"].x < 45 and upstairsperso == 0:
           perso["rect"].x = 44
        if perso["rect"].x < 1 and upstairsperso == 1 :
            perso["rect"].x = 0
        else :
            if inwater==1 :
                perso["rect"].x = perso["rect"].x - 5
            else:
                perso["rect"].x = perso["rect"].x - 12



    if touches[pygame.K_RIGHT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["right"])
            imagePerso = imagesPerso["right"][ianime]
        if perso["rect"].x > 462 and perso["rect"].x < 475 and perso["rect"].y > 120 and upstairsperso==1:
            perso["rect"].x = 461
        if perso["rect"].x > 918:
            perso["rect"].x = 919
        if perso["rect"].x > 590 and perso["rect"].x < 603 and perso["rect"].y > -1 and perso["rect"].y < 200 and upstairsperso==0:
            perso["rect"].x = 591
        else :
            if inwater==1 :
                perso["rect"].x = perso["rect"].x + 5
            else:
                perso["rect"].x = perso["rect"].x + 12
    #Changement fenetre chat/Inventory__________________________________________
    if CurrentWindow == 'Chat' and cdinv == 20 and pygame.mouse.get_pressed() == (True,False,False):
        if (rectIconeBag).collidepoint(pygame.mouse.get_pos()):
            CurrentWindow = 'Bag'
            cdinv = 0
    elif CurrentWindow == 'Bag' and cdinv == 20 and pygame.mouse.get_pressed() == (True,False,False):
        if (rectIconeChat).collidepoint(pygame.mouse.get_pos()):
            CurrentWindow = 'Chat'
            cdinv = 0


#Utilisation potion_____________________________________________________________
    tempTab = []
    if pygame.mouse.get_pressed() == (True,False,False)and cdpot == 50:
        if (objet["rect"]).collidepoint(pygame.mouse.get_pos()):
            cdpot = 0
            done = False
            for objet in objets :
                if not(done) and objet["CodeItem"] == 1 and objet["nbItem"] > 0 :
                    Heal = 50
                    done = True
                    # grilleInventaire[objet["i"]][objet["j"]] = 0
                    objet["nbItem"] -= 1
                    print(str(objet["nbItem"]))
                if objet["nbItem"] > 0 :
                    tempTab.append(objet)
                else:
                    grilleInventaire[objet["i"]][objet["j"]] = 0
            objets = tempTab

    if Heal > 0 :
        Heal -= 1
        # hpHealed = 50
        # if hpHealed > 0 :
        hpHealed-=1
        if hp < 200:
            hp = hp+1
    if cdpot < 50 :
        cdpot +=1
#-----------------------CD INV--------------------------------------------------
    if touches[pygame.K_RCTRL] and CurrentWindow == 'Bag' and cdinv == 20:
        CurrentWindow = 'Chat'
        cdinv = 0
    elif touches[pygame.K_RCTRL] and CurrentWindow == 'Chat' and cdinv == 20:
        CurrentWindow = 'Bag'
        cdinv = 0

    if cdinv < 20 :
        cdinv+=1
#_______________________________________________________________________________
    # elif touches[pygame.K_SPACE] :
    #     #Affichage de l'épée
    #     fenetre.blit(imageSword, rectSword)
    #     rectSword.x = perso["rect"].x
    #     rectSword.y = perso["rect"].y
    #     fenetre.blit(imageSword, rectSword)
    if touches[pygame.K_SPACE] and perso["canshoot"] :
        rectbone = imagebone.get_rect()
        rectbone.x = perso["rect"].x
        rectbone.y = perso["rect"].y

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
        tir["rect"] = rectbone
        tir["direction"] = dirbone


        tirs.append(tir)
        perso["canshoot"] = False
        perso["cooldown"] = 0

    if perso["canshoot"] == False:
        perso["cooldown"] += 1
        if perso["cooldown"] > 8 :
            perso["canshoot"] = True


        # if ibones%3==0:
        #     rectbone1.x = perso["rect"].x
        #     rectbone1.y = perso["rect"].y
        #     ibones+=1
        # elif ibones%3 == 1:
        #     rectbone2.x = perso["rect"].x
        #     rectbone2.y = perso["rect"].y
        #     ibones+=1
        # elif ibones%3 == 2:
        #     rectbone3.x = perso["rect"].x
        #     rectbone3.y = perso["rect"].y
        #     ibones+=1


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
        if not(t["rect"].x > 1024 or t["rect"].x < 0 or t["rect"].y > 768 or t["rect"].y<0) :
            tempTab.append(t)
    tirs = tempTab
    # else:
    #     imagePerso = imagesPerso["right"][0]


    # Affichage du fond
    fenetre.blit(imageFond, rectFond)

    #affichage os
    #Affichage grille
    pygame.draw.rect(fenetre, (200, 0,255), pygame.Rect(700, -1,12, 162),0)                                                                                                                                                            #or touches[pygame.K_UP] or touches[pygame.K_DOWN]
    if ((perso["rect"].x >700 and perso["rect"].x < 713) and (perso["rect"].y >-1 and perso["rect"].y < 163) and (vartour+1 < i) and (touches[pygame.K_LEFT] or touches[pygame.K_RIGHT] )):
        upstairsperso=(upstairsperso+1)%2
        #Pour réguler upstairsperso
        vartour = i
    #changement upstairsblob
    if ((blob["rect"].x >700 and blob["rect"].x < 707) and (blob["rect"].y >-1 and blob["rect"].y < 163) and (vartour+1 < i) and (blob["upstairs"]!=upstairsperso)):
        blob["upstairs"]=(blob["upstairs"]+1)%2
        vartour = i
#DEPLACEMENT BLOB TEST 1________________________________________________________



#deplacer le blob avec le curseur
    # for event in pygame.event.get():
    #     if event.type == MOUSEMOTION:
    #     # if event.type == MOUSEBUTTONDOWN:
    #         # if event.button == 1:
    #             rectBlob.x = event.pos[0]
    #             rectBlob.y = event.pos[1]
    #(Si ce n'est pas en pleine écran) Permet de redimensionner la fenetre (Non Responsive) tant que sa ne depasse la taille max initialisé
    # if event.type == VIDEORESIZE:
    #     if event.w > largeur or event.h > hauteur :
    #         continuer = 0



    ## Afficher Collision en haut à gauche quand le Perso et le blob ce touche
    # if perso["rect"].colliderect(rectBlob):
    for blob in blobs :
        if maskPerso.overlap(maskBlob, (blob["rect"].left - perso["rect"].left, blob["rect"].top - perso["rect"].top)) != None:
            fenetre.blit(imageText,rectText)
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
        b01["upstairs"] = 0
        b01["rect"] = rectBlob01
        b01["rect"].x = newblobx
        b01["rect"].y = newbloby
        b01["nbBlob"] = newnbBlob
        b01["pv"] = 80
        b01["vitesse"] = 2
        blobs.append(b01)

        b02 = {}
        b02["upstairs"] = 0
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








#________________________________________________________________________________
#TEST UPSTAIRSBLOB
    # if i%10==0:
    #     upstairsblob=(upstairsblob+1)%2
    #     print("upstairsblob= ", upstairsblob)
    # print("upstairsperso= ", upstairsperso)
#_________________________FONCTIONNEL MAIS LOURD________________________________
    # if upstairsperso==1 and upstairsblob==1 :
    #     fenetre.blit(imageGrille, rectGrille)
    #     fenetre.blit(imagePerso, perso["rect"])
    #     fenetre.blit(imageblob, rectBlob)
    #     fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
    #     for t in tirs:
    #         if t["direction"] > -1:
    #             fenetre.blit(imagebone, t["rect"])
    # elif upstairsperso==1 and upstairsblob==0:
    #     fenetre.blit(imageblob, rectBlob)
    #     fenetre.blit(imageGrille, rectGrille)
    #     fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
    #     fenetre.blit(imagePerso, perso["rect"])
    #     for t in tirs:
    #         if t["direction"] > -1:
    #             fenetre.blit(imagebone, t["rect"])
    # elif upstairsperso==0 and upstairsblob==0:
    #     fenetre.blit(imageblob, rectBlob)
    #     fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
    #     fenetre.blit(imagePerso, perso["rect"])
    #     for t in tirs:
    #         if t["direction"] > -1:
    #             fenetre.blit(imagebone, t["rect"])
    #     fenetre.blit(imageGrille, rectGrille)
    # elif upstairsperso==0 and upstairsblob==1:
    #     fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
    #     fenetre.blit(imagePerso, perso["rect"])
    #     for t in tirs:
    #         if t["direction"] > -1:
    #             fenetre.blit(imagebone, t["rect"])
    #     fenetre.blit(imageGrille, rectGrille)
    #     fenetre.blit(imageblob, rectBlob)
#_______________________NOUVEL AFFICHAGE________________________________________
    for blob in blobs :
        if blob["upstairs"] == 0 :
            fenetre.blit(imageblob, blob["rect"])


    if upstairsperso == 0 :
        fenetre.blit(imagePerso, perso["rect"])
        for t in tirs:
            if t["direction"] > -1:
                fenetre.blit(imagebone, t["rect"])

    fenetre.blit(imageGrille, rectGrille)
    fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)

    for blob in blobs :
        if blob["upstairs"] == 1 :
            fenetre.blit(imageblob, blob["rect"])

    if upstairsperso == 1 :
        fenetre.blit(imagePerso, perso["rect"])
        for t in tirs:
            if t["direction"] > -1:
                fenetre.blit(imagebone, t["rect"])

#AJOUT POTIONS POUR TESTER !!!_______________________________________________________
    if touches[pygame.K_t] and donnepotion == 0:
        getReward(2,1)
        donnepotion = 1


#plongeon
    # if touches[pygame.K_c]:
    #     if i%5==0:
    #         imagePerso = imagesPersoH20["face"][0]
    #         fenetre.blit(imagePerso, perso["rect"])
    #     elif i%5==4:
    #         imagePerso = imagesPersoH20["face"][1]
    #         fenetre.blit(imagePerso, perso["rect"])
    #     Pressed = 1
    # if touches[pygame.K_c]==0 and Pressed == 1:
    #     imagePersoHacheDeZoo = imagesPersoH20["face"][1]
    #     fenetre.blit(imagePerso, perso["rect"])
    #     imagePersoHacheDeZoo = imagesPersoH20["face"][0]
    #     fenetre.blit(imagePerso, perso["rect"])
    #
    # if touches[pygame.K_c]:
    #     fenetre.blit(imagePerso, perso["rect"])
    #     fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
    # else:
    #     fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
    #     fenetre.blit(imagePerso, perso["rect"])
    if i%3==0 :
        ianimeblob = (ianimeblob+1)%len(imagesBlob["left"])
        imageblob = imagesBlob["left"][ianimeblob]
        ianimebone = (ianimebone+1)%len(imagesbone["proj"])
        imagebone = imagesbone["proj"][ianimebone]

    # if upstairsblob==1 :
    #     fenetre.blit(imageGrille, rectGrille)
    #     fenetre.blit(imageblob, rectBlob)
    # else:
    #         # Affichage Perso
    #     fenetre.blit(imageblob, rectBlob)
    #     fenetre.blit(imageGrille, rectGrille)
    # rafraichissement
    fenetre.blit(imageTree, rectTree)
    fenetre.blit(score_surface, score_rect)

    #______________________________INV+CHAT_____________________________________
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

        for s in range(len(grilleInventaire)) :
            for j in range(len(grilleInventaire[s])) :
                if grilleInventaire[s][j] == 1 :
                    for objet in objets :
                        if objet["CodeItem"] == 1:

                            objet["rect"] = imageHealthPot01.get_rect()
                            objet["i"] = s
                            objet["j"] = j
                            objet["rect"].x = 10+(j*largeurCaseInv)
                            objet["rect"].y = (rectInventory.y+20)+(s*hauteurCaseInv)
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
                elif grilleInventaire[s][j] == 2 :
                    rectCarquois = imageCarquois.get_rect()
                    objet["i"] = s
                    objet["j"] = j
                    rectCarquois.x = 10+(j*largeurCaseInv)
                    rectCarquois.y = (rectInventory.y+20)+(i*hauteurCaseInv)
                    fenetre.blit(imageCarquois, rectCarquois)
#_______________________________________________________________________________


    #Health Bar contour
    pygame.draw.rect(fenetre, (200, 0,255), pygame.Rect(largeur-233, hauteur-(hauteur-35), hpBarMax+4, 14),4)
    #HealthBar
    if hp < 0 :
        hpAffiche = 0
    else :
        hpAffiche = hp
    pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(largeur-230, hauteur-(hauteur-38), hpAffiche, 10))
    if hp <= 0 :
        pygame.quit()

    pygame.display.flip()
    #print ( upstairsperso)


    # Si on a clique sur le bouton de fermeture on sortira
    # au debut du prochain tour de boucle
    # Pour cela, on parcours la liste des evenements
    # et on cherche un QUIT...
    for event in pygame.event.get(): # parcours de la liste des evenements recus
        if event.type == pygame.QUIT: # Si un de ces evenements est de type QUIT
            continuer = 0

# fin du programme principal.
# On n'y accedera jamais dans le cas de ce programme


pygame.quit()
