"""

Projekt na zalicznie

Asteroids – gra komputerowa stworzona przez firmę Atari, wydana została w roku 1979 na automaty do gry oraz konsolę Atari 2600. W roku 1981 została wydana na komputer Atari 800. Firma Atari wydała jeszcze oficjalne wersje na konsole Atari 5200 i Atari 7800 oraz na komputery Acorn BBC Micro i Atari ST. 

Status: w trakcie budowy :)

"""

import pygame as pg
import math
import random
import time

# constants
# 1080p
WINSIZE = [1280, 720]
WINCENTER = [320, 240]
NUMSTARS = 150

fElapsedTime = 0.016  # Przykładowa wartość czasu trwania jednej klatki (~60 FPS)

bDead = False
clock = None
screen = None
font = None

class SpaceObject:
    def __init__(self, nSize, x, y, dx, dy, angle):
        self.nSize = nSize
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.angle = angle

vecAsteroids = []
vecBullets = []
player = SpaceObject(0, 0.0, 0.0, 0.0, 0.0, 0.0)
bDead = False
nScore = 0

vecModelShip = []
vecModelAsteroid = []

# Model statku jako prosty trójkąt równoramienny
vecModelShip = [
    (0.0, -5.0),
    (-2.5, 2.5),
    (2.5, 2.5)
]

def screen_width():
    return WINSIZE[0]  # Przykładowa szerokość ekranu, dostosuj do faktycznych wymiarów

def screen_height():
    return WINSIZE[1]  # Przykładowa wysokość ekranu, dostosuj do faktycznych wymiarów

def reset_game():
    global bDead, nScore, player, vecBullets, vecAsteroids

    # Inicjalizacja pozycji gracza
    player.x = screen_width() / 2.0
    player.y = screen_height() / 2.0
    player.dx = 0.0
    player.dy = 0.0
    player.angle = 0.0

    # Metody clear() służą do opróżniania list.
    vecBullets.clear()
    vecAsteroids.clear()

    # Dodanie dwóch asteroid
    # Używamy klasy SpaceObject do tworzenia obiektów asteroid i dodajemy je do listy vecAsteroids.
    vecAsteroids.append(SpaceObject(nSize=50, x=screen_width()-150, y=screen_height()-150, dx=8.0, dy=-6.0, angle=0.0))
    vecAsteroids.append(SpaceObject(nSize=50, x=150.0, y=200.0, dx=-5.0, dy=3.0, angle=0.0))
    vecAsteroids.append(SpaceObject(nSize=50, x=screen_width()-200, y=200, dx=5.0, dy=-3.0, angle=0.0))

    # Resetowanie stanu gry
    bDead = False
    nScore = 0 

# Tworzenie "postrzępionego" koła dla asteroidy
def OnCreate():

    global clock, screen, font
    # initialize and prepare screen
    pg.init()

    screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("pygame: Asteroids ")
    white = 255, 240, 200
    black = 20, 20, 40
    screen.fill(black)

    # Inicjalizacja czcionki
    pg.font.init()
    font = pg.font.Font(None, 36)

    clock = pg.time.Clock()

    verts = 20
    for i in range(verts):
        noise = random.uniform(0.8, 1.2)  # Losowa wartość między 0.8 a 1.2
        angle = (i / verts) * 2 * math.pi  # Obliczenie kąta w radianach
        vecModelAsteroid.append((noise * math.sin(angle), noise * math.cos(angle)))

    # funkcji reset_game - zerujemy liczniki na start :)
    reset_game()

def create_asteroid():

    new_asteroid = SpaceObject(
        nSize=random.randint(1, 10),
        x=random.uniform(0, 800),
        y=random.uniform(0, 600),
        dx=random.uniform(-1.0, 1.0),
        dy=random.uniform(-1.0, 1.0),
        angle=0.0
    )

    vecAsteroids.append(new_asteroid)

def update_asteroids():

    for a in vecAsteroids:
        a.x += a.dx
        a.y += a.dy

        # Wrap around screen
        if a.x < 0:
            a.x += 800
        if a.x >= 800:
            a.x -= 800
        if a.y < 0:
            a.y += 600
        if a.y >= 600:
            a.y -= 600


# Funkcja do toroidalnego mapowania współrzędnych
def wrap_coordinates(ix, iy, screen_width, screen_height):
    ox = ix
    oy = iy
    if ix < 0.0:
        ox = ix + screen_width
    if ix >= screen_width:
        ox = ix - screen_width
    if iy < 0.0:
        oy = iy + screen_height
    if iy >= screen_height:
        oy = iy - screen_height
    return ox, oy

def draw_wireframe_model(surface, model_coordinates, x, y, r=0.0, s=1.0, color=(255, 255, 255)):
    # model_coordinates to lista par (x, y)
    
    # Stworzenie wektora przekształconych współrzędnych
    transformed_coordinates = []
    verts = len(model_coordinates)

    # Rotacja
    for coord in model_coordinates:
        transformed_x = coord[0] * math.cos(r) - coord[1] * math.sin(r)
        transformed_y = coord[0] * math.sin(r) + coord[1] * math.cos(r)
        transformed_coordinates.append((transformed_x, transformed_y))

    # Skalowanie
    for i in range(verts):
        transformed_coordinates[i] = (transformed_coordinates[i][0] * s, transformed_coordinates[i][1] * s)

    # Translacja
    for i in range(verts):
        transformed_coordinates[i] = (transformed_coordinates[i][0] + x, transformed_coordinates[i][1] + y)

    # Rysowanie zamkniętego wielokąta
    for i in range(verts):
        j = (i + 1) % verts
        pg.draw.line(surface, color, transformed_coordinates[i], transformed_coordinates[j], 1)

# Funkcja sprawdzająca, czy punkt znajduje się wewnątrz koła
def is_point_inside_circle(cx, cy, radius, px, py):
    return (px - cx) ** 2 + (py - cy) ** 2 < radius ** 2

def OnUserUpdate():

    global fElapsedTime, bDead, vecBullets
    #fElapsedTime = 0.016  # Przykładowa wartość czasu trwania jednej klatki (~60 FPS)

    for a in vecAsteroids:
        # Zmiana pozycji asteroidy
        a.x += a.dx * fElapsedTime * 3
        a.y += a.dy * fElapsedTime * 3
        a.angle += 0.5 * fElapsedTime * 2 # Dodanie rotacji

        a.x, a.y = wrap_coordinates(a.x, a.y, screen_width(), screen_height())
    
        # Rysowanie modelu asteroid
        draw_wireframe_model(screen, vecModelAsteroid, a.x, a.y, a.angle, 50, (255, 255, 0))
        # test
        pg.draw.circle(screen, (255,0, 0), (a.x, a.y), a.nSize)

	# VELOCITY changes POSITION (with respect to time)
    player.x += player.dx * fElapsedTime
    player.y += player.dy * fElapsedTime

    player.x, player.y = wrap_coordinates(player.x, player.y, screen_width(), screen_height())

    # Sprawdzenie kolizji statku z asteroidami
    for a in vecAsteroids:
        if is_point_inside_circle(a.x, a.y, a.nSize, player.x, player.y):
            bDead = True

    # Aktualizacja pozycji i rysowanie pocisków
    for bullet in vecBullets:
        bullet.x += bullet.dx * fElapsedTime
        bullet.y += bullet.dy * fElapsedTime

        # 
        bullet.x, bullet.y = wrap_coordinates(bullet.x, bullet.y, screen_width(), screen_height())

        # Rysowanie pocisków
        pg.draw.circle(screen, (255, 255, 255), (int(bullet.x), int(bullet.y)), 2)

    # Usuwanie pocisków z poza ekranem - tworzy nową listę w której znajdują się tylko te elem które są na scenie
    vecBullets = [bullet for bullet in vecBullets if 1 <= bullet.x < screen_width() - 1 and 1 <= bullet.y < screen_height() - 1]

    # Narysuj Shipa
    draw_wireframe_model(screen, vecModelShip, player.x, player.y, player.angle)


def fill_screen(color):

    screen.fill(color)
    #pg.display.flip()

def main():

    print("Asteroids..")

    global fElapsedTime, bDead, nScore, font

    OnCreate()

    running = True
    nScore = 0

    while running:

        fill_screen((0, 0, 0))  # Wypełnia ekran kolorem czarnym (RGB: 0, 0, 0)

        OnUserUpdate()

        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                running = False
                #break

            # Obsługa klawiszy
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    player.angle -= 5.0 * fElapsedTime * 5
                if e.key == pg.K_RIGHT:
                    player.angle += 5.0 * fElapsedTime * 5
                if e.key == pg.K_UP:
                    player.dx += math.sin(player.angle) * 50.0 * fElapsedTime * 5
                    player.dy += -math.cos(player.angle) * 50.0 * fElapsedTime * 5
                    print("key UP")
                if e.key == pg.K_SPACE:
                    vecBullets.append(SpaceObject(0, player.x, player.y, 50.0 * math.sin(player.angle), -50.0 * math.cos(player.angle), 0.0))


        player_pos_text = font.render(f'Player pos.x: {player.x:.2f}, {player.y:.2f}', True, (255, 255, 255))
        screen.blit(player_pos_text, (2, screen_height()-25))
       
        # Rysowanie wyniku
        score_text = font.render(f'SCORE: {nScore}', True, (255, 255, 255))
        screen.blit(score_text, (2, 2))

        # Sprawdzenie, czy gracz jest martwy
        if bDead:
            print("Player is dead!")

            # game_over_text = font.render(f'Game Over', True, (255, 0, 0))
            # screen.blit(game_over_text, (screen_width()/2, screen_height()/2))
            # time.sleep(1)

            reset_game() # zaczynamy od nowa
        
        pg.display.update()
        clock.tick(50)


    pg.quit()   



if __name__ == "__main__":
    
    main()

# https://chatgpt.com/c/2cb83072-ae3d-4225-ad70-2e085dfb7d5a
# https://github.com/pygame/pygame/blob/main/examples/stars.py
# https://github.com/OneLoneCoder/Javidx9/blob/master/ConsoleGameEngine/SmallerProjects/OneLoneCoder_Asteroids.cpp

# https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/