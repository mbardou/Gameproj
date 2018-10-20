import os
import pygame
#redblobgames
pygame.init()

#Création de la fenetre

largeur = 1024
hauteur = 768
fenetre=pygame.display.set_mode((largeur,hauteur))

# lecture de l'image du perso
#Dico des images---------------------------------------------------------

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
imagesPerso = {}

imagesPerso["right"]=[]
imagesPerso["left"]=[]
imagesPerso["down"]=[]
imagesPerso["up"]=[]

temp = pygame.image.load("perso1.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoright02.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoright03.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoright04.png").convert_alpha()
imagesPerso["right"].append(temp)
temp = pygame.image.load("persoleft.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoleft02.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoleft03.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoleft04.png").convert_alpha()
imagesPerso["left"].append(temp)
temp = pygame.image.load("persoface.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persodown02.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persodown03.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persodown04.png").convert_alpha()
imagesPerso["down"].append(temp)
temp = pygame.image.load("persoup.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("persoup02.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("persoup03.png").convert_alpha()
imagesPerso["up"].append(temp)
temp = pygame.image.load("persoup04.png").convert_alpha()
imagesPerso["up"].append(temp)
#fin du dico --------------------------------------------------------------
imageSword = pygame.image.load("sword1.png").convert_alpha()

imageGrille = pygame.image.load("GrilleComplete.png").convert_alpha()
ianimeblob = 0
ianime = 0
imageblob = imagesBlob["left"][ianime]
imagePerso = imagesPerso["up"][ianime]

# creation d'un rectangle pour positioner l'image du personnage
rectBlob = imageblob.get_rect()
rectBlob.x = 240
rectBlob.y = 120
rectPerso = imagePerso.get_rect()
rectPerso.x = hauteur/2
rectPerso.y = largeur/2

rectSword = imageSword.get_rect()
rectSword.x = 2000
rectSword.y = 2000

rectGrille = imageGrille.get_rect()
rectGrille.x = 0
rectGrille.y = 0
# lecture de l'image du fond
imageFond = pygame.image.load("fond1.png").convert()

# creation d'un rectangle pour positioner l'image du fond
rectFond = imageFond.get_rect()
rectFond.x = 0
rectFond.y = 0

## Ajoutons un texte fixe dans la fenetre :
# Choix de la police pour le texte
font = pygame.font.Font(None, 34)

# Creation de l'image correspondant au texte
imageText = font.render('<Escape> pour quitter', True, (255, 255, 255))

# creation d'un rectangle pour positioner l'image du texte
rectText = imageText.get_rect()
rectText.x = 10
rectText.y = 10



# servira a regler l'horloge du jeu
horloge = pygame.time.Clock()

# la boucle infinie dans laquelle on reste coince
i=1;
continuer=1
upstairsperso = 0
upstairsblob = 0
vartour = -1
while continuer:


    horloge.tick(30)

    i= i+1;
    #print (i)
    # on recupere l'etat du clavier
    touches = pygame.key.get_pressed();

    # si la touche ESC est enfoncee, on sortira
    # au debut du prochain tour de boucle
    if touches[pygame.K_ESCAPE] :
        continuer=0



        # rafraichissement
    # Affichage du Texte
    fenetre.blit(imageText, rectText)



    if touches[pygame.K_UP] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["up"])
            imagePerso = imagesPerso["up"][ianime]
        if rectPerso.y < 1 :
           rectPerso.y = 0
        else :
            rectPerso.y = rectPerso.y - 8

    elif touches[pygame.K_DOWN] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["down"])
            imagePerso = imagesPerso["down"][ianime]
        if rectPerso.y > 616 :
            rectPerso.y = 617

        else :
           rectPerso.y = rectPerso.y + 8
    elif touches[pygame.K_LEFT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["left"])
            imagePerso = imagesPerso["left"][ianime]
        if rectPerso.x > 700 and rectPerso.x < 710 and rectPerso.y > 5 and rectPerso.y < 200 and upstairsperso==0:
            rectPerso.x = 710
        if rectPerso.x < 45:
           rectPerso.x = 44
        else :
            rectPerso.x = rectPerso.x - 8
    elif touches[pygame.K_RIGHT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["right"])
            imagePerso = imagesPerso["right"][ianime]
        if rectPerso.x > 462 and rectPerso.x < 470 and rectPerso.y > 70 and upstairsperso==1:
            rectPerso.x = 461
        if rectPerso.x > 918:
            rectPerso.x = 919
        if rectPerso.x > 590 and rectPerso.x < 600 and rectPerso.y > -1 and rectPerso.y < 200 and upstairsperso==0:
            rectPerso.x = 591
        else :
            rectPerso.x = rectPerso.x + 8

    elif touches[pygame.K_SPACE] :
        rectSword.x = rectPerso.x
        rectSword.y = rectPerso.y

    else:
        imagePerso = imagesPerso["right"][0]


    # Affichage du fond
    fenetre.blit(imageFond, rectFond)
    #Affichage de l'épée
    fenetre.blit(imageSword, rectSword)
    #Affichage grille
    if ((rectPerso.x >700 and rectPerso.x < 710) and (rectPerso.y >-1 and rectPerso.y < 163) and (vartour+1 < i) and (touches[pygame.K_LEFT] or touches[pygame.K_RIGHT] or touches[pygame.K_UP] or touches[pygame.K_DOWN])):
        upstairsperso=(upstairsperso+1)%2
        #Pour réguler upstairsperso
        vartour = i
#TEST UPSTAIRSBLOB
    # if i%10==0:
    #     upstairsblob=(upstairsblob+1)%2
    #     print("upstairsblob= ", upstairsblob)
    #     print("upstairsperso= ", upstairsperso)

    if upstairsperso==1 and upstairsblob==1 :
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imagePerso, rectPerso)
        fenetre.blit(imageblob, rectBlob)
    elif upstairsperso==1 and upstairsblob==0:
        fenetre.blit(imageblob, rectBlob)
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imagePerso, rectPerso)
    elif upstairsperso==0 and upstairsblob==0:
        fenetre.blit(imageblob, rectBlob)
        fenetre.blit(imagePerso, rectPerso)
        fenetre.blit(imageGrille, rectGrille)
    elif upstairsperso==0 and upstairsblob==1:
        fenetre.blit(imagePerso, rectPerso)
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imageblob, rectBlob)


    if i%3==0 :
        ianimeblob = (ianimeblob+1)%len(imagesBlob["left"])
        imageblob = imagesBlob["left"][ianimeblob]

    # if upstairsblob==1 :
    #     fenetre.blit(imageGrille, rectGrille)
    #     fenetre.blit(imageblob, rectBlob)
    # else:
    #         # Affichage Perso
    #     fenetre.blit(imageblob, rectBlob)
    #     fenetre.blit(imageGrille, rectGrille)
    # rafraichissement
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
