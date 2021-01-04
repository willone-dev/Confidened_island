import math
import noise
import numpy as np
import random
from Config import *

threshold = 0

class WorldGenerator:

    def __init__(self, hauteur, largeur):
        self.shape = (hauteur, largeur)
        self.scale = random.randint(370, 450)  # min  370 200 _ 355 octave 6
        # self.scale = 375
        self.octaves = 7
        self.lacunarity = 2
        self.baseList = [5, 8, 7, 14, 13, 15]  # 13 /15 water # valid 7
        self.b_id = random.randrange(len(self.baseList))
        self.n_base = self.baseList[self.b_id] * random.randint(1, 10)
        self.persistence = 0.6  ### Map entre 1000 et 2000 0.6. a tester : entre 2000 et 3000 0.5 entre 3000 et 4000 0.4  entre 4000 et 5000 0.3
        self.map = np.zeros(self.shape, )
        self.map_sprite = [['_' for value in range(self.shape[1])] for v in range(self.shape[0])]
        self.mini_map = np.zeros(self.shape + (3,), dtype=np.uint8)

    def get_recap(self):
        recap = ['############# ISLAND GAME Console  ##################',
                        'Dimensions',
                        'hauteur : {} largeur : {}'.format(self.shape[0],self.shape[1]),
                        "Octave: {}  Persistence : {} ".format(self.octaves, self.persistence),
                        "Scale: {} Lacunary {}".format(self.scale, self.lacunarity),
                        "Base nb : {} Generator value : {} ".format(self.baseList[self.b_id],self.n_base)]
        return recap

    def generate_world(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.map[i][j] = noise.pnoise2(i / self.scale,
                                               j / self.scale,
                                               octaves=self.octaves,
                                               persistence=self.persistence,
                                               lacunarity=self.lacunarity,
                                               repeatx=self.shape[0],
                                               repeaty=self.shape[1],
                                               base=self.n_base)
        return self.map

    def generate_island(self):
        center_x, center_y = self.shape[1] // 2, self.shape[0] // 2
        self.circle_grad = np.zeros_like(self.map)
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                distx = abs(x - center_x)
                disty = abs(y - center_y)
                dist = math.sqrt(distx * distx + disty * disty)
                self.circle_grad[y][x] = dist
        # get it between -1 and 1
        self.max_grad = np.max(self.circle_grad)
        self.circle_grad = self.circle_grad / self.max_grad
        self.circle_grad -= 0.5
        self.circle_grad *= 2
        self.circle_grad = - self.circle_grad
        # shrink gradient
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                if self.circle_grad[y][x] > 0:
                    self.circle_grad[y][x] *= 20
        # get it between 0 and 1
        self.max_grad = np.max(self.circle_grad)
        self.circle_grad = self.circle_grad / self.max_grad
        self.world_noise = np.zeros_like(self.map)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.world_noise[i][j] = (self.map[i][j] * self.circle_grad[i][j])
                if self.world_noise[i][j] > 0:
                    self.world_noise[i][j] *= 20
        # get it between 0 and 1
        self.max_grad = np.max(self.world_noise)
        self.world_noise = self.world_noise / self.max_grad
        self.map = self.world_noise
        return self.map

    def add_sprite(self, ):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if i == 0 or i == len(self.map_sprite) - 1:
                    self.map_sprite[i] = ['Z' for value in range(self.shape[0])]
                if j == 0 or j == len(self.map_sprite[0]) - 1:
                    self.map_sprite[i][j] = 'Z'
                elif self.map[i][j] < threshold + 0.015:
                    self.map_sprite[i][j] = WORLD_SPRITES['blue'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['blue'][1]
                elif self.map[i][j] < threshold + 0.05:
                    self.map_sprite[i][j] = WORLD_SPRITES['lightblue'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['lightblue'][1]
                elif self.map[i][j] < threshold + 0.1:
                    self.map_sprite[i][j] = WORLD_SPRITES['sandy'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['sandy'][1]
                elif self.map[i][j] < threshold + 0.25:
                    self.map_sprite[i][j] = WORLD_SPRITES['beach'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['beach'][1]
                elif self.map[i][j] < threshold + 0.45:
                    self.map_sprite[i][j] = WORLD_SPRITES['green'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['green'][1]
                elif self.map[i][j] < threshold + 0.6:
                    self.map_sprite[i][j] = WORLD_SPRITES['darkgreen'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['darkgreen'][1]
                elif self.map[i][j] < threshold + 0.7:
                    self.map_sprite[i][j] = WORLD_SPRITES['montain'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['montain'][1]
                elif self.map[i][j] < threshold + 0.8:
                    self.map_sprite[i][j] = WORLD_SPRITES['snow'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['snow'][1]
                elif self.map[i][j] < threshold + 0.9:
                    self.map_sprite[i][j] = WORLD_SPRITES['obside'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['obside'][1]
                elif self.map[i][j] < threshold + 1.0:
                    self.map_sprite[i][j] = WORLD_SPRITES['lave'][0]
                    self.mini_map[i][j] = WORLD_SPRITES['lave'][1]
        return self.map_sprite

class FloreGenerator:

    def __init__(self, map, hauteur, largeur):
        self.world_map = map
        self.hauteur = hauteur
        self.largeur = largeur
        self.map_flore = self.generate_flore()

    def generate_flore(self):
        map = [['_' for value in range(self.largeur)] for v in range(self.hauteur)]
        for value in FLORE_SPRITE:
            for biome in FLORE_SPRITE[value][2]:
                for tile in range(len(self.world_map)):
                    for ti in range(len(self.world_map[tile])):
                        if self.world_map[tile][ti] == biome:
                            cursor = random.randint(FLORE_SPRITE[value][3][0], FLORE_SPRITE[value][3][1])
                            if cursor == 1 and map[tile][ti] == '_' :
                                map[tile][ti] = FLORE_SPRITE[value][0]
        return map

class StructureGenerator:
    pass

class FauneGenerator:
    pass

class PNJGenerator:
    pass

class LootGenerator:
    pass

class MineralGenerator:
    pass