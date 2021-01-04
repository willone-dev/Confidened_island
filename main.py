# venv/bin/python3
import pygame
from pygame.locals import *
from Config import *
from Caracter import Player
from World import *
from Screen import Affichage, Interface

VERSION = "0.0.4-Alpha"
WINDOW_TITLE = "ISLAND {}".format(VERSION)

class Menu:
    """ Création et gestion des boutons d'un menu """

    def __init__(self, application, *groupes):
        self.couleurs = dict(
            normal=(0, 200, 0),
            survol=(0, 200, 200),
        )
        font = pygame.font.SysFont('Helvetica', 24, bold=True)
        # noms des menus et commandes associées
        items = (
            ('PLAY', application.partie),
            ('CONFIG', application.config),
            ('QUIT', application.quitter)
        )
        x = LARGEUR_FENETRE/2
        y = (HAUTEUR_FENETRE/2)-32
        self._boutons = []
        for texte, cmd in items:
            mb = MenuBouton(texte,self.couleurs['normal'],font,x,y,200,40,cmd)
            self._boutons.append(mb)
            y += 64
            for groupe in groupes:
                groupe.add(mb)

    def update(self, events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            # Si le pointeur souris est au-dessus d'un bouton
            if bouton.rect.collidepoint(*posPointeur):
                # Changement du curseur par un quelconque
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                # Changement de la couleur du bouton
                bouton.dessiner(self.couleurs['survol'])
                # Si le clic gauche a été pressé
                if clicGauche:
                    # Appel de la fonction du bouton
                    bouton.executerCommande()
                break
            else:
                # Le pointeur n'est pas au-dessus du bouton
                bouton.dessiner(self.couleurs['normal'])
        else:
            # Le pointeur n'est pas au-dessus d'un des boutons
            # initialisation au pointeur par défaut
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)  # initialisation du pointeur

class MenuBouton(pygame.sprite.Sprite):
    """ Création d'un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande):
        super().__init__()
        self._commande = commande
        self.image = pygame.Surface((largeur, hauteur))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (int(largeur / 2), int(hauteur / 2))
        self.dessiner(couleur)

    def dessiner(self, couleur):
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self):
        # Appel de la commande du bouton
        self._commande()

class Partie:

    def __init__(self, jeu, fenetre, *groupe):
        self._fenetre = fenetre
        self.player = Player(fenetre=self._fenetre,car_type='humanoid',gender='Female', race='Elf', peau='darkelf', name='Quentin', statut='State test',life='100', armor='100', magic='100')
        self.environnement = Environnement(type_map='island', player=self.player, fenetre=self._fenetre)
        self.interface = Interface(perso=self.player, environnement=self.environnement, fenetre=self._fenetre)
        self.screen = Affichage(fenetre=self._fenetre, environnement=self.environnement, interface=self.interface, player=self.player)

    def update(self,events):
        pygame.time.delay(20)     #### GEstion du delaide rafraichissement met la boucle en pause.
        keys = pygame.key.get_pressed()
        inwalkable = ['Fn','Fa','Fc','Ft']
        damageable = {'W$':{'damage':1},}
        if keys[K_d]and keys[K_z]:
            if self.environnement.flore.map_flore[self.player.position[0]-1][self.player.position[1] + 1] not in inwalkable and self.environnement.map_sprite[self.player.position[0]-1][self.player.position[1] + 1] !='Z' and self.player.alive:
                self.player.position[0] -=1
                self.player.position[1] +=1
                self.player.action = 'walk'
                self.player.direction ='top'
                self.player.deplacement = True
        elif keys[K_q]and keys[K_z]:
            if self.environnement.flore.map_flore[self.player.position[0]-1][self.player.position[1] -1] not in inwalkable and self.environnement.map_sprite[self.player.position[0]-1][self.player.position[1] -1] != 'Z' and self.player.alive:
                self.player.position[0] -= 1
                self.player.position[1] -= 1
                self.player.action = 'walk'
                self.player.direction = 'top'
                self.player.deplacement = True

        elif keys[K_d]and keys[K_s]:
            if self.environnement.flore.map_flore[self.player.position[0]+1][self.player.position[1] + 1] not in inwalkable and self.environnement.map_sprite[self.player.position[0]+1][self.player.position[1] + 1] != 'Z' and self.player.alive :
                self.player.position[0] += 1
                self.player.position[1] += 1
                self.player.action = 'walk'
                self.player.direction = 'right'
                self.player.deplacement = True

        elif keys[K_q]and keys[K_s]:
            if self.environnement.flore.map_flore[self.player.position[0]+1][self.player.position[1] - 1] not in inwalkable and self.environnement.map_sprite[self.player.position[0]+1][self.player.position[1] - 1] != 'Z' and self.player.alive:
                self.player.position[0] += 1
                self.player.position[1] -= 1
                self.player.action = 'walk'
                self.player.direction = 'left'
                self.player.deplacement = True

        elif keys[K_d]:
            if self.environnement.flore.map_flore[self.player.position[0]][self.player.position[1] +1] not in inwalkable and self.environnement.map_sprite[self.player.position[0]][self.player.position[1]+1] != 'Z' and self.player.alive:
                self.direction = 'right'
                self.player.action = 'walk'
                self.player.direction = 'right'
                self.player.position[1] += 1
                self.player.deplacement = True

        elif keys[K_q]:
            if self.environnement.flore.map_flore[self.player.position[0]][self.player.position[1] - 1] not in inwalkable and self.environnement.map_sprite[self.player.position[0]][self.player.position[1] - 1]  !='Z'and self.player.alive:
                self.direction = 'left'
                self.player.action = 'walk'
                self.player.direction = 'left'
                self.player.position[1] -= 1
                self.player.deplacement = True

        elif keys[K_z]:
            if self.environnement.flore.map_flore[self.player.position[0] - 1][self.player.position[1]] not in inwalkable and self.environnement.map_sprite[self.player.position[0]-1][self.player.position[1]]  != 'Z' and self.player.alive:
                self.direction = 'top'
                self.player.action = 'walk'
                self.player.direction = 'top'
                self.player.position[0] -= 1
                self.player.deplacement = True

        elif keys[K_s]:
            if self.environnement.flore.map_flore[self.player.position[0] +1][self.player.position[1] ] not in inwalkable and self.environnement.map_sprite[self.player.position[0] +1][self.player.position[1] ] != 'Z' and self.player.alive:
                self.direction = 'bottom'
                self.player.action = 'walk'
                self.player.direction = 'bottom'
                self.player.position[0] += 1
                self.player.deplacement = True

        for value in damageable:
            if self.environnement.map_sprite[self.player.position[0]][self.player.position[1]] in value:
                self.player.damage(damageable[value]['damage'])
        self.screen.update()

class Jeu:
    """ Simulacre de l'interface du jeu """

    def __init__(self, jeu, *groupes):
        self._fenetre = jeu.fenetre
        jeu.fond = (0, 0, 0)

        from itertools import cycle
        couleurs = [(0, 48, i) for i in range(0, 256, 15)]
        couleurs.extend(sorted(couleurs[1:-1], reverse=True))
        self._couleurTexte = cycle(couleurs)

        self._font = pygame.font.SysFont('Helvetica', 36, bold=True)
        self.creerTexte()
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (int(LARGEUR_FENETRE / 2), int(HAUTEUR_FENETRE / 2))
        # Création d'un event
        self._CLIGNOTER = pygame.USEREVENT + 1
        pygame.time.set_timer(self._CLIGNOTER, 80)

    def creerTexte(self):
        self.texte = self._font.render(
            'LE JEU EST EN COURS D\'EXÉCUTION',
            True,
            next(self._couleurTexte)
        )

    def update(self, events):
        self._fenetre.blit(self.texte, self.rectTexte)
        for event in events:
            if event.type == self._CLIGNOTER:
                self.creerTexte()
                break

    def detruire(self):
        pygame.time.set_timer(self._CLIGNOTER, 0)  # désactivation du timer

class Application:
    """ Classe maîtresse gérant les différentes interfaces du jeu """
    global version
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.fond = (150,) * 3
        self.fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE),RESIZABLE)
        # Groupe de sprites utilisé pour l'affichage
        self.groupeGlobal = pygame.sprite.Group()
        self.statut = True

    def _initialiser(self):
        try:
            self.ecran.detruire()
            # Suppression de tous les sprites du groupe
            self.groupeGlobal.empty()
        except AttributeError:
            pass

    def menu(self):
        # Affichage du menu
        self._initialiser()
        self.ecran = Menu(self, self.groupeGlobal)

    def jeu(self):
        # Affichage du jeu
        self._initialiser()
        self.ecran = Jeu(self, self.groupeGlobal)

    def quitter(self):
        self.statut = False

    def config(self):
        self._initialiser()
        self.ecran=Jeu(self, self.groupeGlobal)

    def partie(self):
        self._initialiser()
        self.ecran=Partie(self, self.fenetre, self.groupeGlobal,)

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.quitter()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.menu()

        self.fenetre.fill(self.fond)
        self.ecran.update(events)
        self.groupeGlobal.update()
        self.groupeGlobal.draw(self.fenetre)
        pygame.display.update()

app = Application()
app.menu()
clock = pygame.time.Clock()
direction = None

while app.statut:
    app.update()
    clock.tick(60)
pygame.quit()