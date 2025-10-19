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

#Classok létrehozása

class Tile:

    COLORS = [
         (237, 229, 218),
         (238, 225, 201),
         (243, 178, 122),
         (246, 150, 101),
         (247, 124, 95),
         (247, 95, 59),
         (237, 208, 115),
         (237, 204, 99),
         (236, 202, 80),
     ]

    def __init__(self, value, row, col):
         self.value = value
         self.row = row
         self.col = col
         self.x = col * RECT_WIDTH
         self.y = row * RECT_HEIGHT

    def get_colors(self):
        color_index = int(math.log2(self.value))-1
        color = self.COLORS[color_index]
        return color

    def draw(self, window):
        color = self.get_colors()
        pygame.draw.rect(window, color,(self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        text = FONT.render(str(self.value),1,FONT_COLOR)
        window.blit(
            text,
            (self.x +(RECT_WIDTH/2 - text.get_width()/2),
             self.y +(RECT_HEIGHT/2 - text.get_height()/2))
             )

    def set_pos(self):
        pass

    def move(self, delta):
        pass



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
def draw(window, tiles):
     window.fill(BACKGROUND_COLOR)

     for tile in tiles.values():
         tile.draw(window)

     draw_grid(window)

     pygame.display.update()

#Csempék generálása
def get_rand_pos(tiles):
    row = None
    col = None

    while True:
        row = random.randrange(0,ROWS)
        col = random.randrange(0,COLS)

        if f"{row}{col}" not in tiles:
            break

    return row, col

def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_rand_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)

    return tiles

#Csempék mozgatás
def move_tiles(window, tiles, clock, direction):
    pass

# Fő program
def main(window):
    clock = pygame.time.Clock()
    run = True

    #Példa, átmeneti - majd töröld b++++
    tiles = generate_tiles()

    while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            draw(window, tiles)

    pygame.quit()


# Program indítása
if __name__ == "__main__":
    main(WINDOW)





