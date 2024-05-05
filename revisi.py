import pygame
import os
import random

pygame.init()

# el
# Asset
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUN = pygame.image.load(os.path.join("Assets/Design", "k_run.png"))

JUMP = pygame.image.load(os.path.join("Assets/Design", "k_run.png"))

DUCK = pygame.image.load(os.path.join("Assets/Design", "k_run.png"))

DRUM_BERGERAK = pygame.image.load(os.path.join("Assets/Design", "drum_gerak.png"))

DRUM_DIAM = pygame.image.load(os.path.join("Assets/Design", "drum_diam.png"))

PESAWAT = pygame.image.load(os.path.join("Assets/Design", "pesawat.png"))

BALON_UDARA = pygame.image.load(os.path.join("Assets/Design", "balon_udara1.png"))

AIRSHIP = pygame.image.load(os.path.join("Assets/Design", "airship.png"))

FONT = pygame.font.Font(os.path.join("Assets/Other",'PressStart2P-Regular.ttf'), 20)

BG = pygame.image.load(os.path.join("Assets/Design", "bg.png"))

class Karakter:
    # SCREEN_HEIGHT = 600
    # SCREEN_WIDTH = 1100
    k_posX = 80
    k_posY = 390
    k_posDuckY = 410
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
        self.k_rect.x = self.k_posX
        self.k_rect.y = self.k_posY
        self.k_jump_sound = pygame.mixer.Sound(os.path.abspath('Assets/Music/jump.mp3'))
        self.k_duck_sound = pygame.mixer.Sound(os.path.abspath('Assets/Music/duck.mp3'))


    def update(self, userInput):
        if userInput[pygame.K_UP] and not self.k_jump:
            self.k_duck = False
            self.k_run = False
            self.k_jump = True
            self.k_jump_sound.play()
        elif userInput[pygame.K_DOWN] and not self.k_jump:
            self.k_duck = True
            self.k_run = False
            self.k_jump = False
            self.k_duck_sound.play()
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
        # [self.step_index // 5]
        self.image = self.duck_img
        self.k_rect = self.image.get_rect()
        self.k_rect.x = self.k_posX
        self.k_rect.y = self.k_posDuckY
        self.step_index += 1

    def run(self):
        # [self.step_index // 5]
        self.image = self.run_img
        self.k_rect = self.image.get_rect()
        self.k_rect.x = self.k_posX
        self.k_rect.y = self.k_posY
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.k_jump:
            self.k_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.k_jump_value:
            self.k_jump = False
            self.jump_vel = self.k_jump_value

    # def dead(self):
    #     self.image = self.dead_img

    def draw_hitbox(self, SCREEN):
        SCREEN.blit(self.image, (self.k_rect.x, self.k_rect.y))

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
        self.x = -random.randint(800, 1000)  # Memulai dari luar layar sebelah kiri
        self.y = random.randint(10, 50)
        self.image = AIRSHIP
        self.width = self.image.get_width()
        self.speed = 1  # Kecepatan yang sangat lambat

    def update(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH:
            self.x = -random.randint(800, 1000)  # Kembali ke luar layar sebelah kiri
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
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image, self.rect)
        self.index += 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Karakter()
    balon_udara_property = BalonUdara()
    airship_property = Airship()
    game_speed = 15
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = FONT.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (950, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        background()

        player.draw_hitbox(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Drum_Bergerak(DRUM_BERGERAK))
            elif random.randint(0, 2) == 1:
                obstacles.append(Drum_Diam(DRUM_DIAM))
            elif random.randint(0, 2) == 2:
                obstacles.append(Pesawat(PESAWAT))

        for obstacle in obstacles:
            obstacle.draw_hitbox(SCREEN)
            obstacle.update()
            if player.k_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)


        balon_udara_property.draw_hitbox(SCREEN)
        balon_udara_property.update()

        airship_property.draw_hitbox(SCREEN)
        airship_property.update()

        score()

        clock.tick(30)
        pygame.display.update()

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))

        if death_count == 0:
            text = FONT.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = FONT.render("Press any Key to Restart", True, (0, 0, 0))
            score = FONT.render("Your Score: " + str(points), True, (0, 0, 0))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, score_rect)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(RUN, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 160))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)
