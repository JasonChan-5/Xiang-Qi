import pygame
from pygame.locals import *
import os
from pieces import *

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

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((642, 720))
    pygame.display.set_caption("Xiang Qi")
    pygame.display.set_icon(pygame.image.load(os.path.join("image/blackGeneral.png")))

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    bg = pygame.image.load(os.path.join("image/chineseChessBG.png"))
    background.blit(bg, (0, 0))

    # Make Pieces
    redSide = pygame.sprite.Group()
    blackSide = pygame.sprite.Group()
    for i in range(len(grid[3])):
        if i % 2 == 0:
            redSide.add(pawn("red", grid[3][i], blackSide, 3, i, screen))
    redSide.add(general("red", grid[0][4], blackSide, 0, 4, screen))
    redSide.add(guard("red", grid[0][3], blackSide, 0, 3, screen))
    redSide.add(guard("red", grid[0][5], blackSide, 0, 5, screen))
    redSide.add(bishop("red", grid[0][2], blackSide, 0, 2, screen))
    redSide.add(bishop("red", grid[0][6], blackSide, 0, 6, screen))
    redSide.add(horse("red", grid[0][1], blackSide, 0, 1, screen))
    redSide.add(horse("red", grid[0][7], blackSide, 0, 7, screen))
    redSide.add(rook("red", grid[0][0], blackSide, 0, 0, screen))
    redSide.add(rook("red", grid[0][8], blackSide, 0, 8, screen))
    redSide.add(cannon("red", grid[2][1], blackSide, 2, 1, screen))
    redSide.add(cannon("red", grid[2][7], blackSide, 2, 7, screen))
    for i in range(len(grid[6])):
        if i % 2 == 0:
            blackSide.add(pawn("black", grid[6][i], redSide, 6, i, screen))
    blackSide.add(general("black", grid[9][4], redSide, 9, 4, screen))
    blackSide.add(guard("black", grid[9][3], redSide, 9, 3, screen))
    blackSide.add(guard("black", grid[9][5], redSide, 9, 5, screen))
    blackSide.add(bishop("black", grid[9][2], redSide, 9, 2, screen))
    blackSide.add(bishop("black", grid[9][6], redSide, 9, 6, screen))
    blackSide.add(horse("black", grid[9][1], redSide, 9, 1, screen))
    blackSide.add(horse("black", grid[9][7], redSide, 9, 7, screen))
    blackSide.add(rook("black", grid[9][0], redSide, 9, 0, screen))
    blackSide.add(rook("black", grid[9][8], redSide, 9, 8, screen))
    blackSide.add(cannon("black", grid[7][1], redSide, 7, 1, screen))
    blackSide.add(cannon("black", grid[7][7], redSide, 7, 7, screen))
    red = pygame.sprite.RenderPlain(redSide)
    black = pygame.sprite.RenderPlain(blackSide)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    turn = True #true = black/bottom false = red/top
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                if turn:
                    for i in blackSide:
                        if mouse[0] > i.rect[0] and mouse[0] < i.rect[0] + i.image.get_width() and mouse[1] > i.rect[1] and mouse[1] < i.rect[1] + i.image.get_height():
                            if i.displayMoves():
                                turn = False
                else:
                    for i in redSide:
                        if mouse[0] > i.rect[0] and mouse[0] < i.rect[0] + i.image.get_width() and mouse[1] > i.rect[1] and mouse[1] < i.rect[1] + i.image.get_height():
                            if i.displayMoves():
                                turn = True
        screen.blit(background, (0, 0))
        red.draw(screen)
        black.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()