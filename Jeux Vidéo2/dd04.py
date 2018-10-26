import os
import sys, math, random, pygame
from pygame.locals import *
from pygame import *
#redblobgames
pygame.init()

#Création de la fenetre

largeur = 1024
hauteur = 768
# fenetre=pygame.display.set_mode((largeur,hauteur))
fenetre=pygame.display.set_mode((largeur,hauteur), RESIZABLE)
rectFenetre = fenetre.get_rect()

score_font = pygame.font.Font(None, 30)
couleur_font = (255,0,0)
# lecture de l'image du perso
#Dico des images---------------------------------------------------------
#boneproj---------------------------------------------------------------
#faire dictionnaire :

bones = []
bonestir = []
tirs=[]

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
ianimeblob = 0
ianime = 0
ianimebone = 0
points = 0
imageblob = imagesBlob["left"][ianimeblob]
imagePerso = imagesPerso["up"][ianime]

rectPerso = imagePerso.get_rect()


perso = {}
perso["rect"]=rectPerso
perso["img"]=imagePerso
perso["direction"]="right"
perso["canshoot"]=True
perso["cooldown"]=0

# creation d'un rectangle pour positioner l'image du personnage
rectBlob = imageblob.get_rect()
rectBlob.x = 240
rectBlob.y = 120
perso["rect"].x = hauteur/2
perso["rect"].y = largeur/2
rectSword = imageSword.get_rect()
rectbone = imagebone.get_rect()
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
score_surface = score_font.render("Score : {:6d} points".format(points), 1, couleur_font)
score_rect = score_surface.get_rect()
score_rect.bottomright = rectFenetre.bottomright



# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle infinie dans laquelle on reste coince
i=1;
continuer=1
upstairsperso = 0
upstairsblob = 0
vartour = -1
dirbone = -1
Pressed = 0
inwater = 0
hit = 0
canshoot = True
cooldown = 0
while continuer:
    print("je peux tirer ? "+str(perso["canshoot"]))

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
                perso["rect"].y = perso["rect"].y - 8

    elif touches[pygame.K_DOWN] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["down"])
            imagePerso = imagesPerso["down"][ianime]
        if perso["rect"].y > 616 :
            perso["rect"].y = 617
        #bloque l escalier droit
        if perso["rect"].x < 730 and perso["rect"].x >= 680 and perso["rect"].y > 155 and upstairsperso ==1 :
            perso["rect"].y = 156
        if perso["rect"].x < 680 and perso["rect"].x >= 630 and perso["rect"].y > 120 and upstairsperso ==1 :
            perso["rect"].y = 121
        if perso["rect"].x < 630 and perso["rect"].x >= 580 and perso["rect"].y > 95 and upstairsperso ==1 :
            perso["rect"].y = 96
        if perso["rect"].x < 580 and perso["rect"].x >= 530 and perso["rect"].y > 70 and upstairsperso ==1 :
            perso["rect"].y = 71
        if perso["rect"].x < 530 and perso["rect"].x >= 480 and perso["rect"].y > 60 and upstairsperso ==1 :
            perso["rect"].y = 61
        if perso["rect"].x < 495 and perso["rect"].x >= 440 and perso["rect"].y > 213 and upstairsperso == 1 :
            perso["rect"].y = 214
        if perso["rect"].x < 285 and perso["rect"].x >= 0 and perso["rect"].y > 214 and upstairsperso == 1 :
            perso["rect"].y = 215
        else :
            if inwater==1 :
                perso["rect"].y = perso["rect"].y + 5
            else :
                perso["rect"].y = perso["rect"].y + 8
    elif touches[pygame.K_LEFT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["left"])
            imagePerso = imagesPerso["left"][ianime]
        if perso["rect"].x > 700 and perso["rect"].x < 710 and perso["rect"].y > 5 and perso["rect"].y < 200 and upstairsperso==0:
            perso["rect"].x = 710
        if perso["rect"].y < 166 and perso["rect"].y >= 156 and perso["rect"].x < 730 and upstairsperso == 1  :
            perso["rect"].x = 731


        if perso["rect"].x < 45 and upstairsperso == 0:
           perso["rect"].x = 44
        if perso["rect"].x < 1 and upstairsperso == 1 :
            perso["rect"].x = 0
        else :
            if inwater==1 :
                perso["rect"].x = perso["rect"].x - 5
            else:
                perso["rect"].x = perso["rect"].x - 8
    elif touches[pygame.K_RIGHT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["right"])
            imagePerso = imagesPerso["right"][ianime]
        if perso["rect"].x > 462 and perso["rect"].x < 470 and perso["rect"].y > 70 and upstairsperso==1:
            perso["rect"].x = 461
        if perso["rect"].x > 918:
            perso["rect"].x = 919
        if perso["rect"].x > 590 and perso["rect"].x < 600 and perso["rect"].y > -1 and perso["rect"].y < 200 and upstairsperso==0:
            perso["rect"].x = 591
        else :
            if inwater==1 :
                perso["rect"].x = perso["rect"].x + 5
            else:
                perso["rect"].x = perso["rect"].x + 8

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

    print("nb Bones"+ str(len(bones)))
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
                                                                                                                                                                        #or touches[pygame.K_UP] or touches[pygame.K_DOWN]
    if ((perso["rect"].x >700 and perso["rect"].x < 710) and (perso["rect"].y >-1 and perso["rect"].y < 163) and (vartour+1 < i) and (touches[pygame.K_LEFT] or touches[pygame.K_RIGHT] )):
        upstairsperso=(upstairsperso+1)%2
        #Pour réguler upstairsperso
        vartour = i
    #changement upstairsblob
    if ((rectBlob.x >700 and rectBlob.x < 710) and (rectBlob.y >-1 and rectBlob.y < 163) and (vartour+1 < i) and (upstairsblob!=upstairsperso)):
        upstairsblob=(upstairsblob+1)%2
        vartour = i
#DEPLACEMENT BLOB TEST 1________________________________________________________

    if rectbone.colliderect(rectBlob):
        hit += 1
        print(hit)

    if perso["rect"].colliderect(rectBlob):
        hit += 1
        print(hit)

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
    if maskPerso.overlap(maskBlob, (rectBlob.left - perso["rect"].left, rectBlob.top - perso["rect"].top)) != None:
        fenetre.blit(imageText,rectText)
    #Affiche le score en bas à droite quand le projectil et le blob ce touche
    if rectbone.colliderect(rectBlob):
        points += 1
        #modification du score
        score_surface = score_font.render("Score : {:5d} points".format(points), 1, couleur_font)










#________________________________________________________________________________
#TEST UPSTAIRSBLOB
    # if i%10==0:
    #     upstairsblob=(upstairsblob+1)%2
    #     print("upstairsblob= ", upstairsblob)
    print("upstairsperso= ", upstairsperso)

    if upstairsperso==1 and upstairsblob==1 :
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imagePerso, perso["rect"])
        fenetre.blit(imageblob, rectBlob)
        fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
        for t in tirs:
            if t["direction"] > -1:
                fenetre.blit(imagebone, t["rect"])
    elif upstairsperso==1 and upstairsblob==0:
        fenetre.blit(imageblob, rectBlob)
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
        fenetre.blit(imagePerso, perso["rect"])
        for t in tirs:
            if t["direction"] > -1:
                fenetre.blit(imagebone, t["rect"])
    elif upstairsperso==0 and upstairsblob==0:
        fenetre.blit(imageblob, rectBlob)
        fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
        fenetre.blit(imagePerso, perso["rect"])
        for t in tirs:
            if t["direction"] > -1:
                fenetre.blit(imagebone, t["rect"])
        fenetre.blit(imageGrille, rectGrille)
    elif upstairsperso==0 and upstairsblob==1:
        fenetre.blit(imageHacheDeZoo, rectHacheDeZoo)
        fenetre.blit(imagePerso, perso["rect"])
        for t in tirs:
            if t["direction"] > -1:
                fenetre.blit(imagebone, t["rect"])
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imageblob, rectBlob)


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
