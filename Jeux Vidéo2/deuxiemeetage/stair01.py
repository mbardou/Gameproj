0import os
import sys, math, random, pygame
from pygame.locals import *
from pygame import *


pygame.init()

largeur = 1024
hauteur = 768
# fenetre=pygame.display.set_mode((largeur,hauteur))
fenetre=pygame.display.set_mode((largeur,hauteur), RESIZABLE)
rectFenetre = fenetre.get_rect()

imageFond = pygame.image.load("eau.png").convert_alpha()
imagePont01 = pygame.image.load("pont1.png").convert_alpha()
imageMarketplace01 = pygame.image.load("marketplace.png").convert_alpha()
imageMarketplace02 = pygame.image.load("marketplace2.png").convert_alpha()
imagePontvertical01 = pygame.image.load("pontvertical01.png").convert_alpha()
# imageBoat = pygame.image.load("boat01.png").convert()

# creation d'un rectangle pour positioner l'image du fond
# rectFond = imageFond.get_rect()
# rectFond.x = 0
# rectFond.y = 0

rectPont1 = imagePont01.get_rect()
rectPont1.x = 150
rectPont1.y = 300

# rectPont2 = imagePont02.get_rect()
# rectPont2.x = 140
# rectPont2.y = 300
#
# rectPont3 = imagePont03.get_rect()
# rectPont3.x = 298
# rectPont3.y = 300
#
# rectPont4 = imagePont04.get_rect()
# rectPont4.x = 455
# rectPont4.y = 300

# rectBoat1 = imageBoat.get_rect()
# rectBoat1.x = 100
# rectBoat1.y = 250

horloge = pygame.time.Clock()
#TEST PATHFINDER-------------------------------------------------------
grillePath = []
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
grillePath.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0])






#_____________________________________________________


grille = []
grille.append([4,4,4,4,4,4,4,4,4,4,4,4,4,4])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])
grille.append([0,0,0,0,3,3,3,3,3,3,1,1,1,1])
grille.append([0,0,0,0,3,3,3,3,3,3,0,0,0,0])
grille.append([1,1,1,1,3,3,3,3,3,3,0,0,0,0])
grille.append([0,0,0,0,3,3,3,3,3,3,0,0,0,0])
grille.append([0,0,0,0,3,3,3,3,3,3,0,0,0,0])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])
grille.append([0,0,0,0,0,5,0,0,0,0,0,0,0,0])

largeurCase = rectPont1.w
hauteurCase = rectPont1.h

i=1;
continuer=1
while continuer:

    horloge.tick(30)

    i= i+1;
    print (i)

    touches = pygame.key.get_pressed();

    if touches[pygame.K_ESCAPE] :
        continuer=0


    # fenetre.blit(imageFond, rectFond)
    #fenetre.blit(imagePont01, rectPont1)
    #fenetre.blit(imagePont02, rectPont2)
    #fenetre.blit(imagePont03, rectPont3)
    #fenetre.blit(imagePont04, rectPont4)
    # fenetre.blit(imageBoat, rectBoat1)
    for i in range(TabBlob): #tableau d ennemi PRESENT SUR LA CARTE a créer
        grillePath[(((LARGEUR_ECRAN(EN PIXEL))+rectBlob)/100(=taille case))-7(=taille carte en case)][...pareil en hauteur...]='B'
            #pour exemple ci dessus, ecran 700px, 1case =100px, 7cases de large. compact:
                #grillePath[((700+rectBlob)/100)-7][pareil en j]
                    #si rectblob en 200x(=3eme case): 700+200/100=9-7=2; 3eme case: grillePath[0,1,2]


    for i in range(len(grille)) :
        for j in range(len(grille[i])) :
            if grille[i][j] == 1 :
                rectBidon1 = imagePont01.get_rect()
                rectBidon1.x = j*largeurCase
                rectBidon1.y = i*hauteurCase
                fenetre.blit(imagePont01,rectBidon1)
            if grille[i][j] == 2 :
                rectBidon2 = imageMarketplace01.get_rect()
                rectBidon2.x = j*largeurCase
                rectBidon2.y = i*hauteurCase
                fenetre.blit(imageMarketplace01,rectBidon2)
            if grille[i][j] == 3 :
                rectBidon3 = imageMarketplace01.get_rect()
                rectBidon3.x = j*largeurCase
                rectBidon3.y = i*hauteurCase
                fenetre.blit(imageMarketplace02,rectBidon3)
            if grille[i][j] == 4 :
                rectBidon4 = imageFond.get_rect()
                rectBidon4.x = j*largeurCase
                rectBidon4.y = i*hauteurCase
                fenetre.blit(imageFond,rectBidon4)
            if grille[i][j] == 5 :
                rectBidon5 = imagePontvertical01.get_rect()
                rectBidon5.x = j*largeurCase
                rectBidon5.y = i*hauteurCase
                fenetre.blit(imagePontvertical01,rectBidon5)





    pygame.display.flip()


    for event in pygame.event.get(): # parcours de la liste des evenements recus
        if event.type == pygame.QUIT: # Si un de ces evenements est de type QUIT
            continuer = 0

pygame.quit()
