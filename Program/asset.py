import pygame
import os
import random
import sys

pygame.init()

judul = "Balap Kelereng"
logo_ccb = pygame.image.load(os.path.join("Assets/Design","logo.png"))

pygame.display.set_caption(judul)
pygame.display.set_icon(logo_ccb)

pygame.mixer.music.load("Assets/Music/backsound.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# Asset
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUN = pygame.image.load(os.path.join("Assets/Design", "k_run.png"))

JUMP = pygame.image.load(os.path.join("Assets/Design", "k_run.png"))

DUCK = pygame.image.load(os.path.join("Assets/Design", "k_duck.png"))

DRUM_BERGERAK = pygame.image.load(os.path.join("Assets/Design", "drum_gerak.png"))

DRUM_DIAM = pygame.image.load(os.path.join("Assets/Design", "drum_diam.png"))

PESAWAT = pygame.image.load(os.path.join("Assets/Design", "pesawat.png"))

BALON_UDARA = pygame.image.load(os.path.join("Assets/Design", "balon_udara1.png"))

AIRSHIP = pygame.image.load(os.path.join("Assets/Design", "airship.png"))

FONT = pygame.font.Font(os.path.join("Assets/Other",'PressStart2P-Regular.ttf'), 20)

BG = pygame.image.load(os.path.join("Assets/Design", "bg.png"))

MENU = pygame.image.load(os.path.join("Assets/Design", "menu.png"))

class Karakter:
    k_jump_value = 7.5

    def __init__(self):
        self.duck_img = DUCK
        self.run_img = RUN
        self.jump_img = JUMP

        self.k_duck = False
        self.k_run = True
        self.k_jump = False

        self.step_index = 0
        self.jump_vel = self.k_jump_value
        self.image = self.run_img
        self.k_rect = self.image.get_rect()
        self.k_rect.x = 80
        self.k_rect.y = 390
        self.k_jump_sound = pygame.mixer.Sound(os.path.abspath('Assets/Music/jump.mp3'))
        self.k_duck_sound = pygame.mixer.Sound(os.path.abspath('Assets/Music/duck.mp3'))
        self.gravity = 2

    def update(self, userInput):
        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.k_jump:
            self.k_duck = False
            self.k_run = False
            self.k_jump = True
            self.k_jump_sound.play()
        elif userInput[pygame.K_DOWN] and not self.k_jump:
            self.k_duck = True
            self.k_run = False
            self.k_jump = False
            self.k_duck_sound.play()
            self.k_duck_sound.set_volume(0.4)
        elif not (self.k_jump or userInput[pygame.K_DOWN]):
            self.k_duck = False
            self.k_run = True
            self.k_jump = False

        if self.k_duck:
            self.duck()
        elif self.k_run:
            self.run()
        elif self.k_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

    def duck(self):
        self.image = self.duck_img
        self.k_rect = self.image.get_rect()
        self.k_rect.x = 80
        self.k_rect.y = 410
        self.step_index += 1

    def run(self):
        self.image = self.run_img
        self.k_rect = self.image.get_rect()
        self.k_rect.x = 80
        self.k_rect.y = 390
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.k_jump:
            self.k_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.k_jump_value:
            self.k_jump = False
            self.jump_vel = self.k_jump_value

        if self.k_rect.y < 390:
            self.k_rect.y += self.gravity

        if self.k_rect.y >= 390:
            self.k_rect.y = 390

    def draw_hitbox(self, SCREEN):
        SCREEN.blit(self.image, (self.k_rect.x, self.k_rect.y))
        pygame.draw.rect(SCREEN, (255, 0, 0), self.k_rect, 2)

game_speed = 15
obstacles = []

class BalonUdara():
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(10, 50)
        self.image = BALON_UDARA
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw_hitbox(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Airship():
    def __init__(self):
        self.x = -random.randint(800, 1000)  
        self.y = random.randint(10, 50)
        self.image = AIRSHIP
        self.width = self.image.get_width()
        self.speed = 1  

    def update(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -random.randint(800, 1000) 
            self.y = random.randint(50, 100)

    def draw_hitbox(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw_hitbox(self, SCREEN):
        SCREEN.blit(self.image, self.rect)
        pygame.draw.rect(SCREEN, (255, 0, 0), self.rect, 2)


class Drum_Bergerak(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 445
    def update(self):
        self.rect.x -= game_speed * 2  
        if self.rect.x < -self.rect.width:
            obstacles.pop()


class Drum_Diam(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 420


class Pesawat(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 350
        self.index = 0

    def draw_hitbox(self, SCREEN):
        pygame.draw.rect(SCREEN, (255, 0, 0), self.rect, 2)
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image, self.rect)
        self.index += 1

