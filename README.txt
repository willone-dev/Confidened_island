################################################################################################################
    _____ ____  _   _ ______ _____ _   _ ______ _____    _____  _____ _               _   _ _____  
   / ____/ __ \| \ | |  ____|_   _| \ | |  ____|  __ \  |_   _|/ ____| |        /\   | \ | |  __ \
  | |   | |  | |  \| | |__    | | |  \| | |__  | |  | |   | | | (___ | |       /  \  |  \| | |  | |
  | |   | |  | | . ` |  __|   | | | . ` |  __| | |  | |   | |  \___ \| |      / /\ \ | . ` | |  | |
  | |___| |__| | |\  | |     _| |_| |\  | |____| |__| |  _| |_ ____) | |____ / ____ \| |\  | |__| |
   \_____\____/|_| \_|_|    |_____|_| \_|______|_____/  |_____|_____/|______/_/    \_\_| \_|_____/

#################################################################################################################
#   VERSION : 0.0.4-Alpha
#   DEMO-VIDEO : https://www.youtube.com/watch?v=WU5-Z5-mRcI
#################################################################################################################
#
#   THANKS :
#     - opengameart.org and his contributor for sprite.
#     - Yvanscher for this Perlin tutorial :
#        https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401
#
#################################################################################################################
#
#   DESCRIPTION:
#         CONFINDED-ISLAND is a pygame RPG like Minecraft/Zelda who generate ISLAND with noise algorithme.
#
#################################################################################################################
#    _____  ______ _      ______           _____ ______   _   _  ____ _______ ______
#   |  __ \|  ____| |    |  ____|   /\    / ____|  ____| | \ | |/ __ \__   __|  ____|
#   | |__) | |__  | |    | |__     /  \  | (___ | |__    |  \| | |  | | | |  | |__   
#   |  _  /|  __| | |    |  __|   / /\ \  \___ \|  __|   | . ` | |  | | | |  |  __|  
#   | | \ \| |____| |____| |____ / ____ \ ____) | |____  | |\  | |__| | | |  | |____
#   |_|  \_\______|______|______/_/    \_\_____/|______| |_| \_|\____/  |_|  |______|
#
#################################################################################################################
#    REQUIEREMENTS :

#         - noise==1.2.2
#         - numpy==1.19.4
#         - Pillow==8.1.0
#         - pygame==2.0.1

#    WORKING :

#        - Generate Island srite_map
#        - Generate Flore sprite_map
#        - Skinable player (cloth, body, weapon)
#        - MiniMap position
#        - Lava Tile make damages
#        - Flore mapping can stop player's deplacement.
#        - UI skeleton
#        - Screen class Display game
#
#    IN PROGRESS :
#
#        - Add structure mapping
#        - Creat class Flore,
#        - Create item class,
#        - Use Best flore sprite_set
#        - add Enemies
#        - add PNJ
#        - add Stuff interaction and craft
#        - add Night/day time
#        - Modify flore statut with Game of life algorithm
#        - Add pnj and Map evenements (quest,cataclysm,attack etc.)
#        - Add Dungeon
#        - Game save implementation
#
#################################################################################################################
#                ____   ____  _    _ _______   __  __ ______
#          /\   |  _ \ / __ \| |  | |__   __| |  \/  |  ____|
#         /  \  | |_) | |  | | |  | |  | |    | \  / | |__   
#        / /\ \ |  _ <| |  | | |  | |  | |    | |\/| |  __|  
#       / ____ \| |_) | |__| | |__| |  | |    | |  | | |____
#      /_/    \_\____/ \____/ \____/   |_|    |_|  |_|______|
#
#################################################################################################################
#                                            
#         I'm French self-taught python developper if you want help me for this project
#         (suggestion/contribution/encouragement), you can tell me by mail : mailto://developpement@willone-atelier.com.
#
#         In 'real-life' i am a jewellery designer : https://wwww.willone-atelier.com
#
#         If you want make a gift and support this project : https://paypal.me/willonedev
#
#         Thanks
#         Willone,
#
#################################################################################################################
