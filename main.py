import pygame
import random
import math


#Játék beállításai

pygame.init()

#Program szintű változók, konstansok létrehozása
FPS = 60
WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 170, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119,110,101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOV_SPEED = 20

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048 játék | Biró László Norbert  NKA19AE6")

#Játékmenet inicializálása, futtatása


# Rács kirajzolása
def draw_grid(window):
     
     for row in range(1,ROWS):
          y = row * RECT_HEIGHT
          pygame.draw.line(window, OUTLINE_COLOR, (0,y),(WIDTH,y), OUTLINE_THICKNESS)

     for row in range(1,COLS):
          x = row * RECT_WIDTH
          pygame.draw.line(window, OUTLINE_COLOR, (x,0),(x,HEIGHT), OUTLINE_THICKNESS)
    
     
     pygame.draw.rect(window, OUTLINE_COLOR, (0,0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

# Ablak frissítése éa kirajzolása
def draw(window):
     window.fill(BACKGROUND_COLOR)
     draw_grid(window)
     pygame.display.update()
     
# Fő program
def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                break
            
            draw(window)



    pygame.quit()


# Program indítása
if __name__ == "__main__":
    main(WINDOW)





