import pygame
from Generator import *
from Config import *
from math import ceil

class Environnement:

    def __init__(self, type_map, player, fenetre):
        ################ type de map #########################
        self.type_map = type_map
        self.fenetre = fenetre
        self.world = WorldGenerator(HAUTEUR_MAP, LARGEUR_MAP)
        self.map = self.world.generate_world()
        if self.type_map == 'island':
            self.map = self.world.generate_island()
        self.map_sprite = self.world.add_sprite()
        self.mini_map = self.world.mini_map
        self.player = player
        self.map_sprite = self.point_apparition()

        self.screen_size = self.fenetre.get_size()
        self.center_x = (self.screen_size[1]/ 2) - LARGEUR_SPRITE
        self.center_y = (self.screen_size[0] / 2) - HAUTEUR_SPRITE

        self.flore = FloreGenerator(self.map_sprite, self.world.shape[0], self.world.shape[1])


        self.largeur = int(self.screen_size[0]/LARGEUR_SPRITE)
        self.hauteur = int(self.screen_size[1]/HAUTEUR_SPRITE)

    def update(self):
        self.screen_size = self.fenetre.get_size()
        self.largeur = int(self.screen_size[0] / LARGEUR_SPRITE)
        self.hauteur = int(self.screen_size[1] / HAUTEUR_SPRITE)

    def point_apparition(self):
        point = 0
        while point == 0:
            random_x = random.randint(0, len(self.map_sprite[0]) - 1)
            random_y = random.randint(0, len(self.map_sprite) - 1)
            if self.map_sprite[random_y][random_x] == 'Ws':
                self.map_sprite[random_y][random_x] = '8'
                point = 1
                self.player.position = [random_y, random_x]
        return self.map_sprite
