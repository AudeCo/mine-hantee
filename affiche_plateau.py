import classes as cl
import pygame
from pygame.locals import *

BRIQUE = (132,46,27)
BLACK = (0,0,0)
GREY=(50,50,50)
WHITE=(255,255,255)
ORANGE=(190,46, 20)

### Paramètres pour le tracé du plateau
dimension=7
plateau = cl.Plateau(dimension)

espace = 500
pixel_case = 100
epaisseur_mur=10

print(plateau.carte_jouable.position)

# dictionnaire à fusionner avec le fichier main une fois les fichiers fusionnés

IMAGES_dict={'pepite': pygame.image.load('images/persos/pepite.png'),
			 'chasseur1': pygame.image.load('images/persos/chasseur1.png'),
			 'chasseur2': pygame.image.load('images/persos/chasseur2.png'),
			 'chasseur3': pygame.image.load('images/persos/chasseur3.png'),
			 'chasseur4': pygame.image.load('images/persos/chasseur4.png'),
			 'fantome': pygame.image.load('images/persos/fantome.png'),	 
		}


def init_plateau():
	global espace, pixel_case, maSurface, largeur, hauteur
	
	#Initialisation de la fenetre du plateau
	pygame.init()
	largeur=int(dimension*pixel_case+espace)
	hauteur=int(dimension*pixel_case)
	
	#Affichage du plateau
	maSurface = pygame.display.set_mode((largeur,hauteur))
	pygame.display.set_caption('La mine hantée')
	maSurface.fill(GREY)

	#Zone de jeu 
	pygame.draw.rect(maSurface,ORANGE,(500,0,hauteur,hauteur))
	
	#Zone carte hors plateau
	pygame.draw.rect(maSurface,ORANGE,(175,520,pixel_case,pixel_case))
	pygame.draw.rect(maSurface,WHITE,(169,514,pixel_case+12,pixel_case+12),10)
	
	#Quadrillage
	for i in range (espace,largeur,pixel_case):
		pygame.draw.line(maSurface,GREY,(i,0),(i,hauteur))
		for j in range (0,hauteur,pixel_case):
			pygame.draw.line(maSurface,GREY,(espace,j),(largeur,j),2)
	

def actualisation_plateau():
	global plateau, espace, pixel_case, maSurface, largeur, hauteur
	dimension = plateau.dimension
	matrice = plateau.matrice
	
	#Parcours du plateau pour afficher toutes les cases
	for ligne in range(dimension):
		for col in range(dimension):
			carte = matrice[ligne][col]
			dessine_carte(carte)
			
	#affichage de la carte jouable
	carte_jouable = plateau.carte_jouable
	dessine_carte(carte_jouable)
	
	#informations sur la partie en cours 
	fontObj = pygame.font.SysFont('arial',40)
	maSurfaceDeTexte = fontObj.render('Mission: ',True,WHITE)
	monRectangleDeTexte	 = maSurfaceDeTexte.get_rect()
	monRectangleDeTexte .topleft = (30,20)
	maSurface.blit(maSurfaceDeTexte,monRectangleDeTexte)

	maSurfaceDeTexte = fontObj.render('Nombre de pépites: ',True,WHITE)
	monRectangleDeTexte	 = maSurfaceDeTexte.get_rect()
	monRectangleDeTexte .topleft = (30,120)
	maSurface.blit(maSurfaceDeTexte,monRectangleDeTexte)

	maSurfaceDeTexte = fontObj.render('Fantômes attrapés: ',True,WHITE)
	monRectangleDeTexte	 = maSurfaceDeTexte.get_rect()
	monRectangleDeTexte .topleft = (30,200)
	maSurface.blit(maSurfaceDeTexte,monRectangleDeTexte)

	maSurfaceDeTexte = fontObj.render('Joker: ',True,WHITE)
	monRectangleDeTexte	 = maSurfaceDeTexte.get_rect()
	monRectangleDeTexte .topleft = (30,330)
	maSurface.blit(maSurfaceDeTexte,monRectangleDeTexte)

	maSurfaceDeTexte = fontObj.render('Carte: ',True,WHITE)
	monRectangleDeTexte	 = maSurfaceDeTexte.get_rect()
	monRectangleDeTexte .topleft = (30,510)
	maSurface.blit(maSurfaceDeTexte,monRectangleDeTexte)
	
	
def dessine_carte(Carte):
	global maSurface, BLACK, espace,epaisseur_mur
	
	# On vérifie que la carte est bien présente sur le plateau, i.e. que ce n'est pas la carte jouable
	if Carte.position != None:
		x_carte=Carte.position[0]
		y_carte= Carte.position[1]
		
		#Conversion de la position matricielle en position en pixel
		x_pixel = espace + x_carte * pixel_case
		y_pixel = y_carte * pixel_case
	
	else:
		x_pixel = 175
		y_pixel = 520
	
	# Affichage de la carte de type labyrinthe
	#Carte type 1
	if Carte.type_carte==1:
		if Carte.orientation==0 or Carte.orientation==2:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+(epaisseur_mur/2)-1),(x_pixel+pixel_case,y_pixel+(epaisseur_mur/2)-1),epaisseur_mur)
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+pixel_case-(epaisseur_mur/2)),(x_pixel+pixel_case,y_pixel+pixel_case-(epaisseur_mur/2)),epaisseur_mur)
		else:
			pygame.draw.line(maSurface,BLACK,(x_pixel+(epaisseur_mur/2)-1,y_pixel),(x_pixel+(epaisseur_mur/2)-1,y_pixel+pixel_case),epaisseur_mur)
			pygame.draw.line(maSurface,BLACK,(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel),(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel+pixel_case),epaisseur_mur)
	#Carte type 2
	if Carte.type_carte==2:
		if Carte.orientation==0:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+(epaisseur_mur/2)-1),(x_pixel+pixel_case,y_pixel+(epaisseur_mur/2)-1),epaisseur_mur)
			pygame.draw.line(maSurface,BLACK,(x_pixel+(epaisseur_mur/2)-1,y_pixel),(x_pixel+(epaisseur_mur/2)-1,y_pixel+pixel_case),epaisseur_mur)
		elif Carte.orientation==1:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+(epaisseur_mur/2)-1),(x_pixel+pixel_case,y_pixel+(epaisseur_mur/2)-1),epaisseur_mur)
			pygame.draw.line(maSurface,BLACK,(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel),(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel+pixel_case),epaisseur_mur)
		elif Carte.orientation==2:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+pixel_case-(epaisseur_mur/2)),(x_pixel+pixel_case,y_pixel+pixel_case-(epaisseur_mur/2)),epaisseur_mur)
			pygame.draw.line(maSurface,BLACK,(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel),(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel+pixel_case),epaisseur_mur)
		else:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+pixel_case-(epaisseur_mur/2)),(x_pixel+pixel_case,y_pixel+pixel_case-(epaisseur_mur/2)),epaisseur_mur)
			pygame.draw.line(maSurface,BLACK,(x_pixel+(epaisseur_mur/2)-1,y_pixel),(x_pixel+(epaisseur_mur/2)-1,y_pixel+pixel_case),epaisseur_mur)
	#Carte type 3
	if Carte.type_carte==3:
		if Carte.orientation==0:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+(epaisseur_mur/2)-1),(x_pixel+pixel_case,y_pixel+(epaisseur_mur/2)-1),epaisseur_mur)
		elif Carte.orientation==1:
			pygame.draw.line(maSurface,BLACK,(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel),(x_pixel+pixel_case-(epaisseur_mur/2),y_pixel+pixel_case),epaisseur_mur)
		elif Carte.orientation==2:
			pygame.draw.line(maSurface,BLACK,(x_pixel,y_pixel+pixel_case-(epaisseur_mur/2)),(x_pixel+pixel_case,y_pixel+pixel_case-(epaisseur_mur/2)),epaisseur_mur)
		else:
			pygame.draw.line(maSurface,BLACK,(x_pixel+(epaisseur_mur/2)-1,y_pixel),(x_pixel+(epaisseur_mur/2)-1,y_pixel+pixel_case),epaisseur_mur)
	
	#Affichage de la pépite
	if Carte.pepite == True:
		maSurface.blit(IMAGES_dict['pepite'],(x_pixel+(0,4*pixel_case),y_pixel+(0,4*pixel_case))
	
	#Affichage du chasseur
	id_chasseur = Carte.chasseur
	if id_chasseur != 0:
		maSurface.blit(IMAGES_dict['chasseur'+str(id_chasseur)+'.png'],(x_pixel,y_pixel))
		
	#Affichage du fantôme
	id_fantome = Carte.fantome
	if id_fantome != 0 :
		maSurface.blit(IMAGES_dict['fantome'],(x_pixel+(0,7*pixel_case,y_pixel+(0,1*pixel_case))

		
		

init_plateau()
actualisation_plateau()

inProgress = True

while inProgress:
	for event in pygame.event.get():
		if event.type == QUIT:
			inProgress = False
	pygame.display.update()
pygame.quit()


