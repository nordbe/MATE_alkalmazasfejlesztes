import pygame
import random
import math


#Játék beállításai

pygame.init()

#Program szintű változók, konstansok létrehozása
FPS = 60
#WIDTH, HEIGHT = 800, 800
BOARD_WIDTH, BOARD_HEIGHT = 800, 800
SCORE_PANEL_HEIGHT = 100
WIDTH = BOARD_WIDTH
HEIGHT = BOARD_HEIGHT + SCORE_PANEL_HEIGHT
ROWS = 4
COLS = 4

RECT_HEIGHT = BOARD_HEIGHT // ROWS
RECT_WIDTH = BOARD_WIDTH // COLS


OUTLINE_COLOR = (187, 170, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119,110,101)
BUTTON_COLOR = (205, 192, 180)
BUTTON_FONT_COLOR = (255,255,255)
NEW_GAME_BUTTON_RECT = pygame.Rect(30, BOARD_HEIGHT + 25 , 200, 50)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
SCORE_FONT = pygame.font.SysFont("comicsans", 35, bold=True)
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

    def set_pos(self, ceil = False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)



    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]



# Rács kirajzolása
def draw_grid(window):
     
     for row in range(1,ROWS):
          y = row * RECT_HEIGHT
          pygame.draw.line(window, OUTLINE_COLOR, (0,y),(BOARD_WIDTH,y), OUTLINE_THICKNESS)

     for row in range(1,COLS):
          x = row * RECT_WIDTH
          pygame.draw.line(window, OUTLINE_COLOR, (x,0),(x,BOARD_HEIGHT), OUTLINE_THICKNESS)
     
     pygame.draw.rect(window, OUTLINE_COLOR, (0,0, BOARD_WIDTH, BOARD_HEIGHT), OUTLINE_THICKNESS)


# Ablak frissítése éa kirajzolása
def draw(window, tiles, current_score, high_score):
     window.fill(BACKGROUND_COLOR)

     for tile in tiles.values():
         tile.draw(window)

     draw_grid(window)

     #Eredményjelző panel háttere
     score_panel_y = BOARD_HEIGHT
     pygame.draw.rect(window, OUTLINE_COLOR, (0, score_panel_y, WIDTH, SCORE_PANEL_HEIGHT))

     #"Új játék" gomb megrajzolása
     pygame.draw.rect(window, BUTTON_COLOR, NEW_GAME_BUTTON_RECT, border_radius=5)
     btn_text = SCORE_FONT.render("Új játék", 1, BUTTON_FONT_COLOR)
     window.blit(
         btn_text,
         (NEW_GAME_BUTTON_RECT.x + (NEW_GAME_BUTTON_RECT.width/2 - btn_text.get_width()/2),
          NEW_GAME_BUTTON_RECT.y + (NEW_GAME_BUTTON_RECT.height/2 - btn_text.get_height()/2))
     )


     #Pontszám kiíratása
     score_text = SCORE_FONT.render(f"Pontszám: {current_score}", 1, FONT_COLOR)
     high_score_text = SCORE_FONT.render(f"Rekord: {high_score}", 1, FONT_COLOR)

     window.blit(score_text, (WIDTH-score_text.get_width()-30, score_panel_y + 15))
     window.blit(high_score_text, (WIDTH-high_score_text.get_width()-30, score_panel_y + 55))



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
def move_tiles(window, tiles, clock, direction, current_score, high_score):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta =(-MOV_SPEED,0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col-1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOV_SPEED
        move_check = lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOV_SPEED
        ceil = True

    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (MOV_SPEED, 0)
        boundary_check = lambda tile: tile.col == COLS -1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOV_SPEED
        move_check = lambda tile, next_tile: tile.x + RECT_WIDTH + MOV_SPEED < next_tile.x
        ceil = False

    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -MOV_SPEED)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOV_SPEED
        move_check = (
            lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOV_SPEED
        )
        ceil = True

    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, MOV_SPEED)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOV_SPEED
        move_check = (
            lambda tile, next_tile: tile.y + RECT_HEIGHT + MOV_SPEED < next_tile.y
        )
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key = sort_func, reverse = reverse)
        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif (tile.value ==  next_tile.value
                  and tile not in blocks
                  and next_tile not in blocks):
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile, next_tile):
                tile.move(delta)
            else:
                continue

            tile.set_pos(ceil)
            updated = True

        update_tiles(window, tiles, sorted_tiles, current_score, high_score) #<-- Bővítés

    return end_tiles(tiles)

def end_tiles(tiles):
    if len(tiles) == 16:
        return "lost"

    row, col = get_rand_pos(tiles)
    tiles[f"{row}{col}"] = Tile(random.choice([2,4]), row, col)
    return "continue"


def update_tiles(window, tiles, sorted_tiles, current_score, high_score):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile

    draw(window,tiles, current_score, high_score) # <-- Bővítés


# Fő program
def main(window):
    clock = pygame.time.Clock()
    run = True

    #Példa, átmeneti - majd töröld b++++
    high_score = 0
    tiles = generate_tiles()

    while run:
            clock.tick(FPS)

            # «--- AKTUÁLIS PONTSZÁM- ÚJ SZEKCIÓ ---»

            current_score = 0
            if tiles:
                current_score = max(tile.value for tile in tiles.values())

            if current_score > high_score:
                high_score = current_score
            # «--- ÚJ SZEKCIÓ VÉGE ---»

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                # «--- ÚJ JÁTÉK GOMB ÉRZÉKELÉSE - ÚJ SZEKCIÓ ---»

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NEW_GAME_BUTTON_RECT.collidepoint(event.pos):
                        tiles = generate_tiles()

                # «--- ÚJ SZEKCIÓ VÉGE ---»

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        move_tiles(window, tiles, clock, "left", current_score, high_score )
                    if event.key == pygame.K_RIGHT:
                        move_tiles(window, tiles, clock, "right", current_score, high_score )
                    if event.key == pygame.K_UP:
                        move_tiles(window, tiles, clock, "up", current_score, high_score )
                    if event.key == pygame.K_DOWN:
                        move_tiles(window, tiles, clock, "down", current_score, high_score )

            draw(window, tiles, current_score, high_score)

    pygame.quit()


# Program indítása
if __name__ == "__main__":
    main(WINDOW)





