from asset import *

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
                sys.exit()

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

        if death_count > 0:
            run = False

def menu(death_count):
    global points
    run = True
    while run:
        if death_count == 0:
            SCREEN.blit(MENU,(0, 0))
            text = FONT.render("Press any Key to Start", True, ("White"))
        elif death_count > 0:
            bg = pygame.image.load(os.path.join("Assets/Design", "menu.png"))
            SCREEN.blit(bg, (0, 0))
            text = FONT.render("Press any Key to Restart", True, ("White"))
            score = FONT.render("Your Score: " + str(points), True, ("White"))
            score_rect = score.get_rect()
            score_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)
            SCREEN.blit(score, score_rect)
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 32)
        SCREEN.blit(text, text_rect)
        SCREEN.blit(RUN, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 130))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                run.Siap()

    pygame.display.update()

menu(death_count=0)
