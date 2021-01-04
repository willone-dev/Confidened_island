import pygame
from Config import *
from PIL import Image
from math import ceil

class Minimap :

    def __init__(self, environnement, fenetre):
        self.mini_map = environnement.mini_map
        self.fenetre = fenetre
        self.largeur = 250
        self.hauteur = 250
        self.coef = LARGEUR_MAP/self.largeur
        self.update_position()
        self.couleur = [10,10,10]
        self.image = Image.fromarray(self.mini_map, mode='RGB')
        self.image.save('full_size.png')
        self.image = self.image.resize((self.hauteur, self.largeur), Image.ANTIALIAS)
        self.image.save("minimap.png")
        self.size_tile = 1

    def update_position(self):
        self.pos_x = int(self.fenetre.get_size()[0] -(self.largeur+LARGEUR_SPRITE/2))
        self.pos_y = int(LARGEUR_SPRITE / 2)

    def  afficher(self,fenetre, perso):
        self.fenetre = fenetre
        self.update_position()
        cadre = pygame.Surface((self.largeur+4, self.hauteur+4))
        cadre.fill(self.couleur)
        image = pygame.image.load("minimap.png").convert()
        self.fenetre.blit(cadre, ( self.pos_x-2,self.pos_y-2))
        self.fenetre.blit(image, (self.pos_x ,self.pos_y))
        self.get_perso_cursor(perso)

    def get_perso_cursor(self, perso):
        position_x = self.pos_x + int(perso.position[1] / self.coef)
        position_y = self.pos_y + int(perso.position[0] / self.coef)
        cursor_perso = pygame.Surface((3, 3))
        self.fenetre.blit(cursor_perso, (position_x, position_y))

class Message:

    def __init__(self, message,fenetre,x,y):
        self.fenetre = fenetre
        self.message = message
        self.font = pygame.font.SysFont('Helvetica', 15, bold=True)
        self.texte = self.font.render(self.message, True, (0, 0, 0))
        self.position = (x,y)
        self.rectTexte = self.texte.get_rect()
        self.dessiner()

    def dessiner(self):
        self.fenetre.blit(self.texte, self.position)

class Interface:

    def __init__(self, perso, environnement, fenetre):
        self.player = perso
        self.fenetre = fenetre
        self.environnement = environnement
        self.stuff = self.player.stuff
        self.minimap = Minimap(self.environnement,self.fenetre)
        self.screen_size = self.fenetre.get_size()
        self.largeur = int(self.screen_size[0] / LARGEUR_SPRITE)
        self.hauteur = int(self.screen_size[1] / HAUTEUR_SPRITE)
        self.world_recap = self.environnement.world.get_recap()

    def update(self):
        pass
    #mouse = pygame.mouse.get_pos()
    #self.interface.afficher(mouse)

    def update_fav_stuff_position(self):
        self.screen_size = self.fenetre.get_size()
        self.largeur = int(LARGEUR_SPRITE+4)
        self.hauteur = int(HAUTEUR_SPRITE+4)
        self.x = int(self.fenetre.get_size()[0]/2-((self.largeur*len(self.stuff.fav))+((self.largeur/2)*(len(self.stuff.fav)-1)))/2)
        self.y = int(self.fenetre.get_size()[1]-(self.hauteur+HAUTEUR_SPRITE/2))

    def afficher_fav_stuff(self):
        self.update_fav_stuff_position()
        x_item = self.x
        y_item = self.y
        for value in self.stuff.fav:
            item_cadre = pygame.Surface((self.largeur, self.hauteur))
            item_cadre.fill([10, 10, 10])
            self.fenetre.blit(item_cadre, (x_item, y_item))
            x_item += self.largeur + LARGEUR_SPRITE / 2

    def console(self):
        y = 10
        x = 10
        espace = 150
        variables = [
            'Perso : X {}, Y {}'.format(self.player.position[1], self.player.position[0]),
            'Block : {}'.format(SPRITE[self.environnement.map_sprite[self.player.position[0]][self.player.position[1]]]),
            'Type {}'.format(self.player.car_type), ##### humanoid
            'Vie : {}'.format(self.player.health),
            'Magie : {}'.format(self.player.magic),
            'Genre : {}'.format(self.player.gender),
            'Race : {}'.format(self.player.race),
            'Peau ::{}'.format(self.player.peau),
            'Name : {}'.format(self.player.name),
            'Alive : {}'.format(self.player.alive),
        ]
        for value in self.world_recap:
            msg = Message(str(value), self.fenetre, x, y)
            y += 20
        x += 250
        y = 30
        for value in  variables :
            self.message = Message(str(value), self.fenetre, x, y)
            y += 20

    def afficher(self):
        self.update_fav_stuff_position()
        self.afficher_fav_stuff()
        self.minimap.afficher(self.fenetre, self.player)
        self.console()

class Affichage:

    def __init__(self, fenetre, environnement, interface, player):

        self.fenetre = fenetre
        self.environnement = environnement
        self.player = player
        self.interface = interface
        self.screen_map = {}
        self.sprite_set = {}
        self.update()

    def update(self,):
        self.get_variable()
        self.environnement.update()
        self.generate_screen_map()
        self.afficher_zone()
        self.interface.afficher()
        self.player.deplacer()

    def get_variable(self,):

        self.screen_size = self.fenetre.get_size()

        self.largeur = int(self.screen_size[0] / LARGEUR_SPRITE)
        self.hauteur = int(self.screen_size[1] / HAUTEUR_SPRITE)

        self.coordonne_y = int(self.player.position[0] - self.hauteur / 2)+1
        self.coordonne_x = int(self.player.position[1] - self.largeur / 2)+1

        self.player.x = int((self.screen_size[1]/2)-(LARGEUR_SPRITE+32))
        self.player.y = int((self.screen_size[0]/2)-(HAUTEUR_SPRITE+16))

        self.screen_map['world'] = [['!' for i in range(self.largeur)] for j in range(self.hauteur)]
        self.screen_map['flore'] = [['!' for i in range(self.largeur)] for j in range(self.hauteur)]
        self.sprite_set['world'] = SPRITE_COLOR
        self.sprite_set['flore'] = FLORE_COLOR

        self.yoffset = 0
        self.xoffset = 0

        if self.coordonne_y != 0:
            self.yoffset = ceil((HAUTEUR_MAP - self.hauteur) / self.coordonne_y)
        if self.coordonne_x != 0:
            self.xoffset = ceil((LARGEUR_MAP - self.largeur) / self.coordonne_x)
        if self.yoffset < 0:
           self.yoffset = 0
        if self.xoffset < 0:
            self.xoffset = 0

    def generate_screen_map(self,):
        y_screen = 0
        x_screen = 0
        y_map = self.coordonne_y
        x_map = self.coordonne_x
        if self.coordonne_x <= 0:
            x_screen = abs(self.coordonne_x)
            x_map = 0
        if self.coordonne_y < 0:
            y_screen = abs(self.coordonne_y)
            y_map = self.coordonne_y
        ymax = int(self.hauteur + y_map)
        xmax = int(self.largeur + x_map)
        for i in range(self.hauteur):
            for j in range(self.largeur):
                #if y_map > HAUTEUR_MAP or x_map > LARGEUR_MAP:
                    #screen_map[self.type][i][j] = "!"
                if y_map < ymax and x_map < xmax and i >= y_screen and j >= x_screen:
                    if y_map < HAUTEUR_MAP and x_map < LARGEUR_MAP:
                        self.screen_map['world'][i][j] = self.environnement.map_sprite[y_map][x_map]
                        self.screen_map['flore'][i][j] = self.environnement.flore.map_flore[y_map][x_map]
                        x_map += 1
                        x_screen += 1
            y_map += 1
            if self.coordonne_x < 0:
                x_screen = abs(self.coordonne_x)
                x_map = 0
            else:
                x_screen = 0
                x_map = self.coordonne_x

    def afficher_zone(self):
        for value in self.screen_map:
            num_case = 0
            num_ligne = 0
            for map in self.screen_map[value]:
                for sprite in map:
                    img = pygame.Surface((HAUTEUR_SPRITE, LARGEUR_SPRITE))
                    x = num_case * LARGEUR_SPRITE
                    y = num_ligne * HAUTEUR_SPRITE
                    if value == 'world':
                        if sprite in self.sprite_set['world']:  # rien == herbe
                            img.fill((self.sprite_set['world'][sprite][0], self.sprite_set['world'][sprite][1], self.sprite_set['world'][sprite][2]))
                            self.fenetre.blit(img, (x, y))
                    if value == 'flore':
                        if sprite in self.sprite_set['flore']:
                            img = pygame.image.load(self.sprite_set['flore'][sprite]).convert_alpha()
                            if int(img.get_size()[1]) > HAUTEUR_SPRITE:
                                coef = (img.get_size()[1] / HAUTEUR_SPRITE) - 1
                                y -= HAUTEUR_SPRITE * coef
                            self.fenetre.blit(img, (x, y))
                    num_case += 1
                num_case = 0
                num_ligne += 1