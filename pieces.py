import pygame
from pygame.locals import *
import os

grid = [[(10, 10), (80, 10), (150, 10), (222, 10), (292, 10), (365, 10), (435, 10), (505, 10), (575, 10)],
        [(10, 80), (80, 80), (150, 80), (222, 80), (292, 80), (365, 80), (435, 80), (505, 80), (575, 80)],
        [(10, 150), (80, 150), (150, 150), (222, 150), (292, 150), (365, 150), (435, 150), (505, 150), (575, 150)],
        [(10, 225), (80, 225), (150, 225), (222, 225), (292, 225), (365, 225), (435, 225), (505, 225), (575, 225)],
        [(10, 297), (80, 297), (150, 297), (222, 297), (292, 297), (365, 297), (435, 297), (505, 297), (575, 297)],
        [(10, 372), (80, 372), (150, 372), (222, 372), (292, 372), (365, 372), (435, 372), (505, 372), (575, 372)],
        [(10, 445), (80, 445), (150, 445), (222, 445), (292, 445), (365, 445), (435, 445), (505, 445), (575, 445)],
        [(10, 517), (80, 517), (150, 517), (222, 517), (292, 517), (365, 517), (435, 517), (505, 517), (575, 517)],
        [(10, 590), (80, 590), (150, 590), (222, 590), (292, 590), (365, 590), (435, 590), (505, 590), (575, 590)],
        [(10, 663), (80, 663), (150, 663), (222, 663), (292, 663), (365, 663), (435, 663), (505, 663), (575, 663)]]

def move(self, rect, row, col):
    self.rect = rect
    self.row = row
    self.col = col
    for i in self.enemies:
        if (self.rect == i.rect):
            i.kill()
            break

class indicator(pygame.sprite.Sprite):

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("image/grayCircle.png"))
        self.rect = rect

class pawn(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, surface, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redPawn.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackPawn.png"))
        self.rect = rect
        self.enemies = enemies
        self.surface = surface
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        if self.color == "red":
            if self.row + 1 < 10:
                moveRect.append(grid[self.row + 1][self.col])
                moveCoord.append((self.row + 1, self.col))
            if self.row > 4:
                if self.col - 1 > -1:
                    moveRect.append(grid[self.row][self.col - 1])
                    moveCoord.append((self.row, self.col - 1))
                if self.col + 1 < 9:
                    moveRect.append(grid[self.row][self.col + 1])
                    moveCoord.append((self.row, self.col + 1))
        else:
            if self.row - 1 > -1:
                moveRect.append(grid[self.row - 1][self.col])
                moveCoord.append((self.row - 1, self.col))
            if self.row < 5:
                if self.col - 1 > -1:
                    moveRect.append(grid[self.row][self.col - 1])
                    moveCoord.append((self.row, self.col - 1))
                if self.col + 1 < 9:
                    moveRect.append(grid[self.row][self.col + 1])
                    moveCoord.append((self.row, self.col + 1))
        while True:
            mouse = pygame.mouse.get_pos()
            ind = pygame.sprite.Group()
            for rect in moveRect:
                ind.add(indicator(rect))
            visual = pygame.sprite.RenderPlain(ind)
            visual.draw(self.display)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        for targets in ind:
                            targets.kill()
                        visual = pygame.sprite.RenderPlain(ind)
                        visual.draw(self.display)
                        pygame.display.flip()
                        return False
                if event.type == MOUSEBUTTONDOWN:
                    for i in range(len(moveRect)):
                        if mouse[0] > moveRect[i][0] and mouse[0] < moveRect[i][0] + self.image.get_width() and mouse[1] > moveRect[i][1] and mouse[1] < moveRect[i][1] + self.image.get_height():
                            move(self, moveRect[i], moveCoord[i][0], moveCoord[i][1])
                            for targets in ind:
                                targets.kill()
                            visual = pygame.sprite.RenderPlain(ind)
                            visual.draw(self.display)
                            pygame.display.flip()
                            return True
                    for targets in ind:
                        targets.kill()
                    visual = pygame.sprite.RenderPlain(ind)
                    visual.draw(self.display)
                    pygame.display.flip()
                    return False