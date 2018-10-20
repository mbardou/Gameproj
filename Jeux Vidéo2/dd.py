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
ianime = 0
imagePerso = imagesPerso["up"][ianime]

# creation d'un rectangle pour positioner l'image du personnage
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
upstairs=0
vartour = -10
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
        if rectPerso.x < 45:
           rectPerso.x = 44
        else :
            rectPerso.x = rectPerso.x - 8
    elif touches[pygame.K_RIGHT] :
        if i%5==0 :
            ianime = (ianime+1)%len(imagesPerso["right"])
            imagePerso = imagesPerso["right"][ianime]
        if rectPerso.x > 918:
            rectPerso.x = 919
        if rectPerso.x > 645 and rectPerso.x < 655 and rectPerso.y > 5 and rectPerso.y < 200 and upstairs==0:
            rectPerso.x = 646
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
    if ((rectPerso.x >700 and rectPerso.x < 710) and (rectPerso.y >0 and rectPerso.y < 163) and (vartour+10 < i)):
        upstairs=(upstairs+1)%2
        #Pour réguler upstairs
        vartour = i
    if upstairs==1 :
        fenetre.blit(imageGrille, rectGrille)
        fenetre.blit(imagePerso, rectPerso)
    else:
        # Affichage Perso
        fenetre.blit(imagePerso, rectPerso)
        fenetre.blit(imageGrille, rectGrille)
    # rafraichissement
    pygame.display.flip()
    print ( upstairs)


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
