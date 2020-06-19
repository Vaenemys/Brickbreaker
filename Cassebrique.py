import pygame

from pygame import *

from numpy import *

import sys
taille_ecran = (width,height) = (800,600)
noir = (0,0,0)
couleurs = [rouge, vert, bleu, rose, blanc] = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 105, 183),(255, 255, 255)]
rectangle = (25, 10)
vitesse = 11
#pygame.mixer.init()
#poyo = pygame.mixer.Sound("Externe/kirby-poyo.ogg")




class Cassebrique():
    def __init__(self):
        pygame.font.init()
        self.horloge = pygame.time.Clock()
        self.ecran = pygame.display.set_mode(taille_ecran)
        self.briques = []
        self.raquette = [[pygame.Rect(300, 500, 25, 10), 120],
                         [pygame.Rect(310, 500, 25, 10), 100],
                         [pygame.Rect(320, 500, 25, 10), 80],
                         [pygame.Rect(330, 500, 25, 10), 45],
                         ]
        self.balle = pygame.Rect(300,350,6,6)
        self.vitesses = [6, 2]
        self.fps = 60
        self.score = 0
        #pygame.font.get_default_font()
        #pygame.font.Font(self.score, 15)
        pygame.display.set_caption('Poyo Brick Breaker')

    def creer_briques(self):
        y = 50
        for ordonnee in arange(200 / 15):
            x = 50
            for abcisse in arange(800 / 25 - 6):
                brique = pygame.Rect(x, y, 25, 10)
                self.briques.append(brique)
                x += 26
            y += 11

    def majballe(self):
        self.balle.x += self.vitesses[0]
        self.balle.y += self.vitesses[1]
        if not 0 <= self.balle.x <= width:
            self.vitesses[0] *= -1
        if not 0 <= self.balle.y <= height:
            self.vitesses[1] *= -1



        for raquette in self.raquette:
            if raquette[0].colliderect(self.balle):
                self.vitesses[1] *= -1

        destruction = self.balle.collidelist(self.briques)
        if destruction != -1:
            brique = self.briques[destruction]
            proche = None
            vertical = (brique.top, brique.bottom)
            horizontal = (brique.left, brique.right)
            for y in vertical:
                distance = abs(y - self.balle.y)
                if proche is None:
                    proche = (distance, 0)
                elif proche[0] > distance:
                    proche = (distance, 0)
            for x in horizontal:
                distance = abs(x - self.balle.x)
                if proche[0] > distance:
                    proche = (distance, 1)
            self.vitesses[proche[1]] *= -1
            self.briques.pop(destruction)
            self.score += 100
            #poyo.play()
            if not self.briques:
                pygame.image.load('Externe/kirby_win.jpg')

    def majraquette(self):
        keystroke = pygame.key.get_pressed()
        if keystroke[K_LEFT]:
            if self.raquette[0][0].x > 0:
                for raquette in self.raquette:
                    raquette[0].x -= vitesse
        elif keystroke[K_RIGHT]:
            if self.raquette[-1][0].x < 790:
                for raquette in self.raquette:
                    raquette[0].x += vitesse

    def main(self):
        self.creer_briques()


        gameover = False
        while not gameover:
            if self.balle.y < 50:
                event.type == pygame.QUIT

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                    pygame.image.load('Externe/lost.jpg')

            print(f"score: {self.score}", end="\r")
            self.ecran.fill(noir)
            self.majraquette()
            self.majballe()


            for brique in self.briques:
                pygame.draw.rect(self.ecran, rouge, brique)
            for raquette in self.raquette:
                pygame.draw.rect(self.ecran, bleu, raquette[0])
            pygame.draw.rect(self.ecran, rose, self.balle)
            #pygame.font.Font.render(self.score, 15)
            pygame.display.update()

            self.horloge.tick(self.fps)
        pygame.quit()
        quit()




if __name__ == "__main__":
    Cassebrique().main()
