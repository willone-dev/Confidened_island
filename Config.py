HAUTEUR_FENETRE = 960
LARGEUR_FENETRE = 1280

HAUTEUR_MAP = 1000
LARGEUR_MAP = 1000

HAUTEUR_SPRITE = 32
LARGEUR_SPRITE = 32

NB_TILE_SCREEN_X = int(LARGEUR_FENETRE/LARGEUR_SPRITE)
NB_TILE_SCREEN_Y = int(HAUTEUR_FENETRE/HAUTEUR_SPRITE)

IMAGE_DE_FOND ="background.png"

SPRITE_COLOR = {
    'Z': [250,6,50],
    '!': [0,0,0],
    'W~': [36, 126, 136],
    'W_' : [36, 93, 158],
    'W*' : [36, 163, 48],
    'W#' : [36, 99, 48],
    'Ws' : [255, 208, 153],
    'Wb' : [255, 207, 100],
    'W=' : [255, 250, 250],
    'W^' : [139, 137, 137],
    'W$' : [243, 89, 28],
    'W£' : [87, 80, 80],
    '8' : [0,0,0],
}
WORLD_SPRITES = {
    'lightblue' : ('W~',[36, 126, 136]),
    'blue': ('W_',[36, 93, 158]),
    'green': ('W*',[36, 163, 48]),
    'darkgreen': ('W#',[36, 99, 48]),
    'sandy': ('Ws',[255, 208, 153]),
    'beach': ('Wb',[255, 207, 93]),
    'snow': ('W=',[255, 250, 250]),
    'montain': ('W^',[139, 137, 137]),
    'lave': ('W$',[243, 89, 28]),
    'obside': ('W£', [87, 80, 80]),
}
SPRITE = {
    'W~' : 'Lagon',
    'W_' : 'Ocean',
    'W*' : 'Plaine',
    'W#' : 'Foret',
    'Ws' : "Plage",
    "Wb":"Desert",
    'W=' : 'Neige',
    'W^':'Montagne',
    'W$':'Lave',
    'W£':'Volcan',
    '8':'spawn_point'
}
FLORE_SPRITE = {
    'buisson' :['Fn', [127, 221, 76,],['W*'],(1,40)],
    'arbre' : ['Fa', [86, 130, 3],['W#'],(1,10),],
    'cactus' : ['Fc', [194, 247, 50],['Wb'],(1,100),],
    'tounesol': ['Ft', [232, 214, 48],['W*'],(1,55),],
    'fleur':['Ff',[253, 108, 158],['W*','W#'],(1,50),],
}

FLORE_ASSET_FILES = ['Sprites/Flore/Tree/plant repack_2.png', ]

FLORE_ASSET = {
    'file':'Sprites/Flore/Tree/plant repack_2.png',
    'Arbre': {
        'Pi' : {
            'Name': 'Pin',
            'Type' : 'Conifère',
            'Life': '100',
            'File': FLORE_ASSET_FILES[0],
            'Biomes':['W#'],
            'Skin' :
                {
                    'Pi1' : {
                        'y' : 0,
                        'x' : 0,
                        'y_off': 128,
                        'x_off': 16,
                        'size_x' : 64,
                        'size_y' : 160,}
            }
        },
        'Pi2':'',
    },
    'Buisson':{
    },
    'Fleur':{},
}
FLORE_COLOR = {
    'Fn' : "Sprites/buisson.png",
    'Fa': "Sprites/arbre.png",
    'Fc': "Sprites/cactus.png",
    'Ft':"Sprites/tournesol.png",
    'Ff':"Sprites/flower.png",
}
MINERAIS = {
    'Cuivre' : ('$c',[231, 62, 1]),
    'Argent' : ('$a', [132, 132, 132]),
    'Or' : ('$o', [255, 215, 0]),
}

