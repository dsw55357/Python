"""

Projekt na zalicznie

Asteroids – gra komputerowa stworzona przez firmę Atari, wydana została w roku 1979 na automaty do gry oraz konsolę Atari 2600. W roku 1981 została wydana na komputer Atari 800. Firma Atari wydała jeszcze oficjalne wersje na konsole Atari 5200 i Atari 7800 oraz na komputery Acorn BBC Micro i Atari ST. 

Status: v.0.2

"""

import os
import pygame as pg
import math
import random
import time

# constants
# 1080p
# WINSIZE = [1280, 720]
WINSIZE = [800, 600]

fElapsedTime = 0.016  # Przykładowa wartość czasu trwania jednej klatki (~60 FPS)

class GameState:
    def __init__(self):
        self.nScore = 0
        self.bDead = False
        self.bPause = False
        self.bMenu  = True
        self.clock = None
        self.screen = None
        self.font = None
        self.boom_sound = None
        self.fire_sound = None
        self.thrust_sound = None

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
vecModelShip = []
vecModelAsteroid = []

player = SpaceObject(0, 0.0, 0.0, 0.0, 0.0, 0.0)
game_State = GameState()

# Model statku jako prosty trójkąt równoramienny
vecModelShip = [
    (0.0, -5.0),
    (-2.5, 2.5),
    (2.5, 2.5)
]

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_sound(file):
    """because pygame can be compiled without mixer."""
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print(f"Warning, unable to load, {file}")
    return None


def screen_width():
    return WINSIZE[0]  # Przykładowa szerokość ekranu, dostosuj do faktycznych wymiarów

def screen_height():
    return WINSIZE[1]  # Przykładowa wysokość ekranu, dostosuj do faktycznych wymiarów

def reset_game():
    global player, vecBullets, vecAsteroids

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
    game_State.bDead = False
    game_State.nScore = 0 

# Tworzenie "postrzępionego" koła dla asteroidy
def OnCreate():

    global font

    # initialize and prepare screen
    pg.init()

    game_State.screen = pg.display.set_mode(WINSIZE)
    pg.display.set_caption("pygame: Asteroids ")
    # white = 255, 240, 200
    black = 20, 20, 40
    game_State.screen.fill(black)

    # Inicjalizacja czcionki
    pg.font.init()

    font = pg.font.Font(None, 36)

    game_State.clock = pg.time.Clock()

    verts = 20
    for i in range(verts):
        noise = random.uniform(0.8, 1.2)  # Losowa wartość między 0.8 a 1.2
        angle = (i / verts) * 2 * math.pi  # Obliczenie kąta w radianach
        vecModelAsteroid.append((noise * math.sin(angle), noise * math.cos(angle)))

    # funkcji reset_game - zerujemy liczniki na start :)
    reset_game()

def create_asteroid():

    pass

def update_asteroids():

    pass

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

    global fElapsedTime, vecBullets, vecAsteroids
    #fElapsedTime = 0.016  # Przykładowa wartość czasu trwania jednej klatki (~60 FPS)

    for a in vecAsteroids:
        # Zmiana pozycji asteroidy
        a.x += a.dx * fElapsedTime * 3
        a.y += a.dy * fElapsedTime * 3
        a.angle += 0.5 * fElapsedTime * 2 # Dodanie rotacji

        a.x, a.y = wrap_coordinates(a.x, a.y, screen_width(), screen_height())
    
        # Rysowanie modelu asteroid
        draw_wireframe_model(game_State.screen, vecModelAsteroid, a.x, a.y, a.angle, a.nSize, (255, 255, 0))

        # test
        #pg.draw.circle(screen, (255,0, 0), (a.x, a.y), a.nSize)

    # VELOCITY changes POSITION (with respect to time)
    player.x += player.dx * fElapsedTime
    player.y += player.dy * fElapsedTime

    player.x, player.y = wrap_coordinates(player.x, player.y, screen_width(), screen_height())

    # Sprawdzenie kolizji statku z asteroidami
    for a in vecAsteroids:
        if is_point_inside_circle(a.x, a.y, a.nSize, player.x, player.y):
            if pg.mixer and game_State.boom_sound is not None:
                game_State.boom_sound.play()
            game_State.bDead = True

    newAsteroids = []

    # Aktualizacja pozycji i rysowanie pocisków
    for bullet in vecBullets:
        bullet.x += bullet.dx * fElapsedTime * 2
        bullet.y += bullet.dy * fElapsedTime * 2
        # 
        bullet.x, bullet.y = wrap_coordinates(bullet.x, bullet.y, screen_width(), screen_height())

        for a in vecAsteroids:
            if is_point_inside_circle(a.x, a.y, a.nSize, bullet.x, bullet.y):
                # Pocisk trafia asteroidę - usuwamy pocisk
                bullet.x = -100  # Pocisk poza ekranem, zostanie usunięty w algorytmie czyszczenia
                if pg.mixer and game_State.boom_sound is not None:
                    game_State.boom_sound.play()

                # Tworzenie mniejszych asteroid po zniszczeniu dużej
                if a.nSize > 6:
                    angle1 = random.uniform(0, 2 * math.pi)
                    angle2 = random.uniform(0, 2 * math.pi)
                    newAsteroids.append(SpaceObject(a.nSize // 2, a.x, a.y, 10.0 * math.sin(angle1), 10.0 * math.cos(angle1), 0.0))
                    newAsteroids.append(SpaceObject(a.nSize // 2, a.x, a.y, 10.0 * math.sin(angle2), 10.0 * math.cos(angle2), 0.0))

                # Usuwanie asteroidy
                a.x = -100  # Asteroida poza ekranem, zostanie usunięta w algorytmie czyszczenia
                game_State.nScore += 100  # Zwiększenie wyniku za trafienie asteroidy

        # Rysowanie pocisków
        pg.draw.circle(game_State.screen, (138,43,226), (int(bullet.x), int(bullet.y)), 2)

    # Dodanie nowych asteroid do listy
    vecAsteroids.extend(newAsteroids)

    # Usuwanie asteroid z poza ekranu - tych trafionych
    vecAsteroids = [asteroid for asteroid in vecAsteroids if asteroid.x >= 0]

    # Sprawdzenie, czy wszystkie asteroidy zostały zniszczone
    if not vecAsteroids:
        game_State.nScore += 1000  # Duży bonus za ukończenie poziomu
        vecBullets.clear()
        # Dodanie dwóch nowych asteroid
        vecAsteroids.append(SpaceObject(16, 30.0 * math.sin(player.angle - math.pi / 2) + player.x, 30.0 * math.cos(player.angle - math.pi / 2) + player.y, 10.0 * math.sin(player.angle), 10.0 * math.cos(player.angle), 0.0))
        vecAsteroids.append(SpaceObject(16, 30.0 * math.sin(player.angle + math.pi / 2) + player.x, 30.0 * math.cos(player.angle + math.pi / 2) + player.y, 10.0 * math.sin(-player.angle), 10.0 * math.cos(-player.angle), 0.0))


    # Usuwanie pocisków z poza ekranem - tworzy nową listę w której znajdują się tylko te elem które są na scenie
    vecBullets = [bullet for bullet in vecBullets if 1 <= bullet.x < screen_width() - 1 and 1 <= bullet.y < screen_height() - 1]

    # Narysuj Shipa
    draw_wireframe_model(game_State.screen, vecModelShip, player.x, player.y, player.angle, 2, (227,11,93))

def fill_screen(color):

    game_State.screen.fill(color)
    #pg.display.flip()


def main():

    print("Asteroids..")

    global fElapsedTime

    OnCreate()

    # load the sound effects
    game_State.boom_sound = load_sound("bangMedium.wav")
    game_State.fire_sound = load_sound("fire.wav")
    game_State.thrust_sound = load_sound("thrust.wav")

    font_game_over = pg.font.Font(None, 46)

    game_State.running = True
    game_State.nScore = 0

    while game_State.running:

        fill_screen((0, 0, 0))  # Wypełnia ekran kolorem czarnym (RGB: 0, 0, 0)

        OnUserUpdate()

        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYUP and e.key == pg.K_ESCAPE):
                running = False
                #break

            # Obsługa klawiszy
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_LEFT:
                    player.angle -= 5.0 * fElapsedTime * 4
                if e.key == pg.K_RIGHT:
                    player.angle += 5.0 * fElapsedTime * 4
                if e.key == pg.K_UP:
                    player.dx += math.sin(player.angle) * 50.0 * fElapsedTime * 5
                    player.dy += -math.cos(player.angle) * 50.0 * fElapsedTime * 5
                    if pg.mixer and game_State.thrust_sound is not None:
                        game_State.thrust_sound.play()
                if e.key == pg.K_SPACE:
                    vecBullets.append(SpaceObject(0, player.x, player.y, 50.0 * math.sin(player.angle), -50.0 * math.cos(player.angle), 0.0))
                    if pg.mixer and game_State.fire_sound is not None:
                        game_State.fire_sound.play()
                if e.key == pg.K_F8:
                    game_State.bDead = True # symulujemy kolizję statu z asteroidą
                if e.key == pg.K_p:
                    game_State.bPause = True
                if e.key == pg.K_m:
                    game_State.bMenu = True                    

        # player_pos_text = font.render(f'Player pos.x: {player.x:.2f}, {player.y:.2f}', True, (255, 255, 255))
        # screen.blit(player_pos_text, (2, screen_height()-25))
       
        # Rysowanie wyniku
        score_text = font.render(f'Score: {game_State.nScore}', True, (57,255,20))
        game_State.screen.blit(score_text, (4, 4))


        if game_State.bMenu:
            while game_State.bMenu:
                menu_text = font.render(f'Menu:', True, (0, 255, 255))
                game_State.screen.blit(menu_text, (screen_width()/2-90, screen_height()/2))
                start_text = font.render(f'Start, press s', True, (251,79,20))
                game_State.screen.blit(start_text, (screen_width()/2-90, screen_height()/2+40))
                end_game_text = font.render(f'Quit, press q or ESC', True, (139,0,139))
                game_State.screen.blit(end_game_text, (screen_width()/2-90, screen_height()/2+70))

                for e in pg.event.get():
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_s:
                            game_State.bMenu = False
                            break
                        if e.key == pg.K_ESCAPE or e.key == pg.K_q:
                            game_State.running = False
                            game_State.bMenu = False
                            break

                pg.display.update()
                game_State.clock.tick(50)  

        if game_State.bPause:
            print("Pause")
            while game_State.bPause:
                pause_text = font.render(f'Pause, press p to continue', True, (128,218,235))
                game_State.screen.blit(pause_text, (screen_width()/2-80, screen_height()/2))
                for e in pg.event.get():
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_p:
                            game_State.bPause = False
                            break
                
                pg.display.update()
                game_State.clock.tick(50)  

        # Sprawdzenie, czy gracz jest martwy
        if game_State.bDead:
            #print("Player is dead!")

            while game_State.bDead:
                game_over_text = font_game_over.render(f'Game Over', True, (255, 0, 0))
                game_State.screen.blit(game_over_text, (screen_width()/2-80, screen_height()/2))

                new_game_text = font.render(f'New game, press n', True, (251,79,20))
                game_State.screen.blit(new_game_text, (screen_width()/2-90, screen_height()/2+40))

                end_game_text = font.render(f'Quit, press q or ESC', True, (139,0,139))
                game_State.screen.blit(end_game_text, (screen_width()/2-90, screen_height()/2+70))

                for e in pg.event.get():
                    if e.type == pg.KEYDOWN:
                        if e.key == pg.K_n:
                            reset_game() # zaczynamy od nowa
                            break
                        if e.key == pg.K_ESCAPE or e.key == pg.K_q:
                            game_State.running = False
                            game_State.bDead = False
                            break

                pg.display.update()
                game_State.clock.tick(50)

            #reset_game() # zaczynamy od nowa
        
        pg.display.update()
        game_State.clock.tick(50)

    pg.quit()   

if __name__ == "__main__":
    
    main()