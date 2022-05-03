import pygame
from pygame.locals import *
import os
import sys

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

def isValid(self, rect): #1 for rook, 2 for cannon, 0 for everything else
    for i in self.groups()[0]:
        if i.rect == rect:
            return False
    return True

def isValidEnemy(self, rect):
    for i in self.enemies:
        if i.rect == rect:
            return True
    return False

def moving(self, moveRect, moveCoord):
    while True:
            mouse = pygame.mouse.get_pos()
            ind = pygame.sprite.Group()
            for rect in moveRect:
                ind.add(indicator(rect))
            visual = pygame.sprite.RenderPlain(ind)
            visual.draw(self.display)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
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

    def __init__(self, color, rect, enemies, row, col, display):
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
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        if self.color == "red":
            if self.row + 1 < 10:
                if isValid(self, grid[self.row + 1][self.col]):
                    moveRect.append(grid[self.row + 1][self.col])
                    moveCoord.append((self.row + 1, self.col))
            if self.row > 4:
                if self.col - 1 > -1:
                    if isValid(self, grid[self.row][self.col - 1]):
                        moveRect.append(grid[self.row][self.col - 1])
                        moveCoord.append((self.row, self.col - 1))
                if self.col + 1 < 9:
                    if isValid(self, grid[self.row][self.col + 1]):
                        moveRect.append(grid[self.row][self.col + 1])
                        moveCoord.append((self.row, self.col + 1))
        else:
            if self.row - 1 > -1:
                if isValid(self, grid[self.row - 1][self.col]):
                    moveRect.append(grid[self.row - 1][self.col])
                    moveCoord.append((self.row - 1, self.col))
            if self.row < 5:
                if self.col - 1 > -1:
                    if isValid(self, grid[self.row][self.col - 1]):
                        moveRect.append(grid[self.row][self.col - 1])
                        moveCoord.append((self.row, self.col - 1))
                if self.col + 1 < 9:
                    if isValid(self, grid[self.row][self.col + 1]):
                        moveRect.append(grid[self.row][self.col + 1])
                        moveCoord.append((self.row, self.col + 1))
        return moving(self, moveRect, moveCoord)

class general(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redGeneral.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackGeneral.png"))
        self.rect = rect
        self.enemies = enemies
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        if self.color == "red":
            if self.row > 0:
                if isValid(self, grid[self.row - 1][self.col]):
                    moveRect.append(grid[self.row - 1][self.col])
                    moveCoord.append((self.row - 1, self.col))
            if self.row < 2:
                if isValid(self, grid[self.row + 1][self.col]):
                    moveRect.append(grid[self.row + 1][self.col])
                    moveCoord.append((self.row + 1, self.col))
        else:
            if self.row > 7:
                if isValid(self, grid[self.row - 1][self.col]):
                    moveRect.append(grid[self.row - 1][self.col])
                    moveCoord.append((self.row - 1, self.col))
            if self.row < 9:
                if isValid(self, grid[self.row + 1][self.col]):
                    moveRect.append(grid[self.row + 1][self.col])
                    moveCoord.append((self.row + 1, self.col))
        if self.col > 3:
            if isValid(self, grid[self.row][self.col - 1]):
                moveRect.append(grid[self.row][self.col - 1])
                moveCoord.append((self.row, self.col - 1))
        if self.col < 5:
            if isValid(self, grid[self.row][self.col + 1]):
                moveRect.append(grid[self.row][self.col + 1])
                moveCoord.append((self.row, self.col + 1))
        return moving(self, moveRect, moveCoord)

class guard(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redGuard.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackGuard.png"))
        self.rect = rect
        self.enemies = enemies
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        if self.color == "red":
            if self.row == 1 and self.col == 4:
                if isValid(self, grid[self.row - 1][self.col - 1]):
                    moveRect.append(grid[self.row - 1][self.col - 1])
                    moveCoord.append((self.row - 1, self.col - 1))
                if isValid(self, grid[self.row - 1][self.col + 1]):
                    moveRect.append(grid[self.row - 1][self.col + 1])
                    moveCoord.append((self.row - 1, self.col + 1))
                if isValid(self, grid[self.row + 1][self.col - 1]):
                    moveRect.append(grid[self.row + 1][self.col - 1])
                    moveCoord.append((self.row + 1, self.col - 1))
                if isValid(self, grid[self.row + 1][self.col + 1]):
                    moveRect.append(grid[self.row + 1][self.col + 1])
                    moveCoord.append((self.row + 1, self.col + 1))
            else:
                if isValid(self, grid[1][4]):
                    moveRect.append(grid[1][4])
                    moveCoord.append((1, 4))
        else:
            if self.row == 8 and self.col == 4:
                if isValid(self, grid[self.row - 1][self.col - 1]):
                    moveRect.append(grid[self.row - 1][self.col - 1])
                    moveCoord.append((self.row - 1, self.col - 1))
                if isValid(self, grid[self.row - 1][self.col + 1]):
                    moveRect.append(grid[self.row - 1][self.col + 1])
                    moveCoord.append((self.row - 1, self.col + 1))
                if isValid(self, grid[self.row + 1][self.col - 1]):
                    moveRect.append(grid[self.row + 1][self.col - 1])
                    moveCoord.append((self.row + 1, self.col - 1))
                if isValid(self, grid[self.row + 1][self.col + 1]):
                    moveRect.append(grid[self.row + 1][self.col + 1])
                    moveCoord.append((self.row + 1, self.col + 1))
            else:
                if isValid(self, grid[8][4]):
                    moveRect.append(grid[8][4])
                    moveCoord.append((8, 4))
        return moving(self, moveRect, moveCoord)

class bishop(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redBishop.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackBishop.png"))
        self.rect = rect
        self.enemies = enemies
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        if self.col == 0:
            if isValid(self, grid[self.row - 2][self.col + 2]) and isValid(self, grid[self.row - 1][self.col + 1]):
                moveRect.append(grid[self.row - 2][self.col + 2])
                moveCoord.append((self.row - 2, self.col + 2))
            if isValid(self, grid[self.row + 2][self.col + 2]) and isValid(self, grid[self.row + 1][self.col + 1]):
                moveRect.append(grid[self.row + 2][self.col + 2])
                moveCoord.append((self.row + 2, self.col + 2))
        if self.col == 8:
            if isValid(self, grid[self.row - 2][self.col - 2]) and isValid(self, grid[self.row - 1][self.col - 1]):
                moveRect.append(grid[self.row - 2][self.col - 2])
                moveCoord.append((self.row - 2, self.col - 2))
            if isValid(self, grid[self.row + 2][self.col - 2]) and isValid(self, grid[self.row + 1][self.col - 1]):
                moveRect.append(grid[self.row + 2][self.col - 2])
                moveCoord.append((self.row + 2, self.col - 2))
        if self.col == 2 or self.col == 6:
            if self.color == "red":
                if self.col == 2:
                    if isValid(self, grid[2][0]):
                        if self.row == 0:
                            if isValid(self, grid[1][1]):
                                moveRect.append(grid[2][0])
                                moveCoord.append((2, 0))
                        else:
                            if isValid(self, grid[3][1]):
                                moveRect.append(grid[2][0])
                                moveCoord.append((2, 0))
                    if isValid(self, grid[2][4]):
                        if self.row == 0:
                            if isValid(self, grid[1][3]):
                                moveRect.append(grid[2][4])
                                moveCoord.append((2, 4))
                        else:
                            if isValid(self, grid[3][3]):
                                moveRect.append(grid[2][4])
                                moveCoord.append((2, 4))
                else:
                    if isValid(self, grid[2][8]):
                        if self.row == 0:
                            if isValid(self, grid[1][7]):
                                moveRect.append(grid[2][8])
                                moveCoord.append((2, 8))
                        else:
                            if isValid(self, grid[3][7]):
                                moveRect.append(grid[2][8])
                                moveCoord.append((2, 8))
                    if isValid(self, grid[2][4]):
                        if self.row == 0:
                            if isValid(self, grid[1][5]):
                                moveRect.append(grid[2][4])
                                moveCoord.append((2, 4))
                        else:
                            if isValid(self, grid[3][5]):
                                moveRect.append(grid[2][4])
                                moveCoord.append((2, 4))
            else:
                if self.col == 2:
                    if isValid(self, grid[7][0]):
                        if self.row == 9:
                            if isValid(self, grid[8][1]):
                                moveRect.append(grid[7][0])
                                moveCoord.append((7, 0))
                        else:
                            if isValid(self, grid[6][1]):
                                moveRect.append(grid[7][0])
                                moveCoord.append((7, 0))
                    if isValid(self, grid[7][4]):
                        if self.row == 9:
                            if isValid(self, grid[8][3]):
                                moveRect.append(grid[7][4])
                                moveCoord.append((7, 4))
                        else:
                            if isValid(self, grid[6][3]):
                                moveRect.append(grid[7][4])
                                moveCoord.append((7, 4))
                else:
                    if isValid(self, grid[7][8]):
                        if self.row == 9:
                            if isValid(self, grid[8][7]):
                                moveRect.append(grid[7][8])
                                moveCoord.append((7, 8))
                        else:
                            if isValid(self, grid[6][7]):
                                moveRect.append(grid[7][8])
                                moveCoord.append((7, 8))
                    if isValid(self, grid[7][4]):
                        if self.row == 9:
                            if isValid(self, grid[8][5]):
                                moveRect.append(grid[7][4])
                                moveCoord.append((7, 4))
                        else:
                            if isValid(self, grid[6][5]):
                                moveRect.append(grid[7][4])
                                moveCoord.append((7, 4))
        if self.col == 4:
            if isValid(self, grid[self.row - 2][self.col - 2]) and isValid(self, grid[self.row - 1][self.col - 1]):
                moveRect.append(grid[self.row - 2][self.col - 2])
                moveCoord.append((self.row - 2, self.col - 2))
            if isValid(self, grid[self.row + 2][self.col - 2]) and isValid(self, grid[self.row + 1][self.col - 1]):
                moveRect.append(grid[self.row + 2][self.col - 2])
                moveCoord.append((self.row + 2, self.col - 2))
            if isValid(self, grid[self.row - 2][self.col + 2]) and isValid(self, grid[self.row - 1][self.col + 1]):
                moveRect.append(grid[self.row - 2][self.col + 2])
                moveCoord.append((self.row - 2, self.col + 2))
            if isValid(self, grid[self.row + 2][self.col + 2]) and isValid(self, grid[self.row + 1][self.col + 1]):
                moveRect.append(grid[self.row + 2][self.col + 2])
                moveCoord.append((self.row + 2, self.col + 2))
        return moving(self, moveRect, moveCoord)

class horse(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redHorse.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackHorse.png"))
        self.rect = rect
        self.enemies = enemies
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        if self.row - 2 > -1:
            if isValid(self, grid[self.row - 1][self.col]):
                if self.col - 1 > -1:
                    if isValid(self, grid[self.row - 2][self.col - 1]):
                        moveRect.append(grid[self.row - 2][self.col - 1])
                        moveCoord.append((self.row - 2, self.col - 1))
                if self.col + 1 < 9:
                    if isValid(self, grid[self.row - 2][self.col + 1]):
                        moveRect.append(grid[self.row - 2][self.col + 1])
                        moveCoord.append((self.row - 2, self.col + 1))
        if self.row + 2 < 10:
            if isValid(self, grid[self.row + 1][self.col]):
                if self.col - 1 > -1:
                    if isValid(self, grid[self.row + 2][self.col - 1]):
                        moveRect.append(grid[self.row + 2][self.col - 1])
                        moveCoord.append((self.row + 2, self.col - 1))
                if self.col + 1 < 9:
                    if isValid(self, grid[self.row + 2][self.col + 1]):
                        moveRect.append(grid[self.row + 2][self.col + 1])
                        moveCoord.append((self.row + 2, self.col + 1))
        if self.col - 2 > -1:
            if isValid(self, grid[self.row][self.col - 1]):
                if self.row - 1 > -1:
                    if isValid(self, grid[self.row - 1][self.col - 2]):
                        moveRect.append(grid[self.row - 1][self.col - 2])
                        moveCoord.append((self.row - 1, self.col - 2))
                if self.row + 1 < 10:
                    if isValid(self, grid[self.row + 1][self.col - 2]):
                        moveRect.append(grid[self.row + 1][self.col - 2])
                        moveCoord.append((self.row + 1, self.col - 2))
        if self.col + 2 < 9:
            if isValid(self, grid[self.row][self.col + 1]):
                if self.row - 1 > -1:
                    if isValid(self, grid[self.row - 1][self.col + 2]):
                        moveRect.append(grid[self.row - 1][self.col + 2])
                        moveCoord.append((self.row - 1, self.col + 2))
                if self.row + 1 < 10:
                    if isValid(self, grid[self.row + 1][self.col + 2]):
                        moveRect.append(grid[self.row + 1][self.col + 2])
                        moveCoord.append((self.row + 1, self.col + 2))
        return moving(self, moveRect, moveCoord)

class rook(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redRook.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackRook.png"))
        self.rect = rect
        self.enemies = enemies
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        look = self.row - 1
        while look > -1:
            if isValidEnemy(self, grid[look][self.col]):
                moveRect.append(grid[look][self.col])
                moveCoord.append((look, self.col))
                break
            elif isValid(self, grid[look][self.col]):
                moveRect.append(grid[look][self.col])
                moveCoord.append((look, self.col))
            else:
                break
            look -= 1
        look = self.row + 1
        while look < 10:
            if isValidEnemy(self, grid[look][self.col]):
                moveRect.append(grid[look][self.col])
                moveCoord.append((look, self.col))
                break
            elif isValid(self, grid[look][self.col]):
                moveRect.append(grid[look][self.col])
                moveCoord.append((look, self.col))
            else:
                break
            look += 1
        look = self.col - 1
        while look > -1:
            if isValidEnemy(self, grid[self.row][look]):
                moveRect.append(grid[self.row][look])
                moveCoord.append((self.row, look))
                break
            elif isValid(self, grid[self.row][look]):
                moveRect.append(grid[self.row][look])
                moveCoord.append((self.row, look))
            else:
                break
            look -= 1
        look = self.col + 1
        while look < 9:
            if isValidEnemy(self, grid[self.row][look]):
                moveRect.append(grid[self.row][look])
                moveCoord.append((self.row, look))
                break
            elif isValid(self, grid[self.row][look]):
                moveRect.append(grid[self.row][look])
                moveCoord.append((self.row, look))
            else:
                break
            look += 1
        return moving(self, moveRect, moveCoord)

class cannon(pygame.sprite.Sprite):

    def __init__(self, color, rect, enemies, row, col, display):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.row = row
        self.col = col
        if (color == "red"):
            self.image = pygame.image.load(os.path.join("image/redCannon.png"))
        else:
            self.image = pygame.image.load(os.path.join("image/blackCannon.png"))
        self.rect = rect
        self.enemies = enemies
        self.display = display
    
    def displayMoves(self):
        moveRect = []
        moveCoord = []
        look = self.row - 1
        while look > -1:
            if isValid(self, grid[look][self.col]) and not isValidEnemy(self, grid[look][self.col]):
                moveRect.append(grid[look][self.col])
                moveCoord.append((look, self.col))
                look -= 1
            elif isValidEnemy(self, grid[look][self.col]) or not isValid(self, grid[look][self.col]):
                look -= 1
                while look > -1:
                    if isValidEnemy(self, grid[look][self.col]):
                        moveRect.append(grid[look][self.col])
                        moveCoord.append((look, self.col))
                        break
                    look -= 1
                break
        look = self.row + 1
        while look < 10:
            if isValid(self, grid[look][self.col]) and not isValidEnemy(self, grid[look][self.col]):
                moveRect.append(grid[look][self.col])
                moveCoord.append((look, self.col))
                look += 1
            elif isValidEnemy(self, grid[look][self.col]) or not isValid(self, grid[look][self.col]):
                look += 1
                while look < 10:
                    if isValidEnemy(self, grid[look][self.col]):
                        moveRect.append(grid[look][self.col])
                        moveCoord.append((look, self.col))
                        break
                    look += 1
                break
        look = self.col - 1
        while look > -1:
            if isValid(self, grid[self.row][look]) and not isValidEnemy(self, grid[self.row][look]):
                moveRect.append(grid[self.row][look])
                moveCoord.append((self.row, look))
                look -= 1
            elif isValidEnemy(self, grid[self.row][look]) or not isValid(self, grid[self.row][look]):
                look -= 1
                while look > -1:
                    if isValidEnemy(self, grid[self.row][look]):
                        moveRect.append(grid[self.row][look])
                        moveCoord.append((self.row, look))
                        break
                    look -= 1
                break
        look = self.col + 1
        while look < 9:
            if isValid(self, grid[self.row][look]) and not isValidEnemy(self, grid[self.row][look]):
                moveRect.append(grid[self.row][look])
                moveCoord.append((self.row, look))
                look += 1
            elif isValidEnemy(self, grid[self.row][look]) or not isValid(self, grid[self.row][look]):
                look += 1
                while look < 9:
                    if isValidEnemy(self, grid[self.row][look]):
                        moveRect.append(grid[self.row][look])
                        moveCoord.append((self.row, look))
                        break
                    look += 1
                break
        return moving(self, moveRect, moveCoord)