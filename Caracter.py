from random import randint
import pygame
from Config import *
from TEMPLATE import *
import random

class Stuff:

    def __init__(self, nb_place,fenetre):
        self.fenetre = fenetre
        self.screen_size = fenetre.get_size()
        self.stuff = [0 for nb in range(nb_place)]
        self.fav = [0 for n in range(10)]
        self.ecart_item = len(self.fav)/2
        self.update_position()

    def update_position(self,):
        self.screen_size = self.fenetre.get_size()
        self.largeur = int(LARGEUR_SPRITE+4)
        self.hauteur = int(HAUTEUR_SPRITE+4)
        self.x = int(self.fenetre.get_size()[0]/2-((self.largeur*len(self.fav))+((self.largeur/2)*(len(self.fav)-1)))/2)
        self.y = int(self.fenetre.get_size()[1]-(self.hauteur+HAUTEUR_SPRITE/2))

    def afficher(self, fenetre):
        self.update_position()
        x_item = self.x
        y_item = self.y
        for value in self.fav:
            item_cadre = pygame.Surface((self.largeur, self.hauteur))
            item_cadre.fill([10, 10, 10])
            fenetre.blit(item_cadre, (x_item, y_item))
            x_item += self.largeur + LARGEUR_SPRITE/2

class CaractereSpriteSet:

    def __init__(self, caractere, fenetre, kwargs):
        self.dict = {}
        self.fenetre = fenetre
        self.sprites_image = []
        self.caractere = caractere
        self.template ={}
        if self.caractere.car_type == 'humanoid':
            self.template['Body'] = TEMPLATE_CONF["humanoid"]["Body"]
        for value in kwargs:
            self.dict[value] = kwargs[value]
            image = pygame.image.load(self.dict[value]).convert_alpha()
            self.sprites_image.append(image)
        self.dimensions = TEMPLATE_CONF["humanoid"]['dimensions']
        self.sub_surfaces = {}
        self.generate()

    def generate(self):
        for k, value in enumerate(self.dict):
            self.sub_surfaces[value]={}
            for action in self.template['Body']:
                self.sub_surfaces[value][action]={}
                for direction in self.template['Body'][action]:
                    if direction != 'nb':
                        x = 0
                        y = self.template['Body'][action][direction]*64
                        self.sub_surfaces[value][action][direction]=[]
                        for i in range(self.template['Body'][action]['nb']):
                            self.sub_surfaces[value][action][direction].append(self.sprites_image[k].subsurface(x, y, 64, 64))
                            x+=64


class Caracter:

    def __init__(self, car_type, gender, race, peau, name, statut, life,armor,magic,fenetre):
        self.car_type = car_type ##### humanoid
        self.gender = gender
        self.race = race
        self.peau = peau
        self.name = name
        self.statut = statut
        self.fenetre = fenetre
        self.health = int(life)
        self.armor = int(armor)
        self.magic = int(magic)

class Player(Caracter):
    """Classe permettant de créer un personnage"""
    def __init__(self,car_type, gender, race, peau, name, statut, life,armor,magic,fenetre):
        Caracter.__init__(self,car_type, gender, race, peau, name, statut, life,armor,magic,fenetre)
        # Sprites du personnage
        #self.sex = 'Female'
        #self.race = 'Elf'
        #self.peau = 'darkelf'

        self.skin = {
            'Corps': 'Sprites/Caractere/{gender}/Base/{race}/Body/{peau}.png'.format(gender=self.gender, race=self.race,peau=self.peau),
            'Tete': 'Sprites/blonde.png',
            'Torse': 'Sprites/dress.png',
            'Armes': 'Sprites/dagger_female.png'
        }
        self.stuff = Stuff(10,fenetre)
        # Position du personnage en cases et en pixels
        self.case_x = 1
        self.case_y = 1
        self.ascii = "8"
        self.x = int((self.fenetre.get_size()[1] / 2) - (LARGEUR_SPRITE + 32))
        self.y = int((self.fenetre.get_size()[0] / 2) - (HAUTEUR_SPRITE + 16))
        # Direction par défaut
        self.action = 'walk'
        self.direction = 'bottom'
        # Niveau dans lequel le personnage se trouve
        self.alive = True
        self.cursor = 0
        self.skin_image = CaractereSpriteSet(self,fenetre, self.skin)
        self.deplacement = False

    def update(self):
        self.x = int((self.fenetre.get_size()[1] / 2) - (LARGEUR_SPRITE + 32))
        self.y = int((self.fenetre.get_size()[0] / 2) - (HAUTEUR_SPRITE + 16))

    def damage(self, damage):
        if self.health > 0:
            self.health -= damage
        else:
            self.alive = False
            self.action = 'ko'
            self.direction = 'bottom'
            
    def deplacer(self):
        for k, value in enumerate(self.skin_image.dict):
            self.img = self.animation(self.skin_image.sub_surfaces[value][self.action][self.direction])
        self.deplacement = False

    def animation(self,value):
        if self.cursor >= len(value):
            self.cursor = 0
        if self.deplacement == True:
            self.img = self.fenetre.blit(value[self.cursor], (self.y, self.x))
            self.cursor += 1
        if self.deplacement == False:
            if self.alive == True:
                self.img = self.fenetre.blit(value[0], (self.y, self.x))
            if self.alive == False:
                self.img = self.fenetre.blit(value[-1], (self.y, self.x))
