import pygame
import sys
import os
from button import Button
import run

pygame.init()

pygame.mixer.music.load("Assets/Music/backsound.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

logo_ccb = pygame.image.load(os.path.join("Assets/Design","logo.png"))
pygame.display.set_icon(logo_ccb)

SCREEN = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load(os.path.join("Assets/Design", "menu.png"))

def get_font(size):
    return pygame.font.Font(os.path.join("Assets/Other",'PressStart2P-Regular.ttf'), size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        QUIT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        PLAY_TEXT = get_font(30).render("Apakah kamu siap?", True, "#b68f40")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(550, 180))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(315, 275), text_input="Siap!", font=get_font(55), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        QUIT_BACK = Button(image=None, pos=(790, 275), text_input="Belom!", font=get_font(55), base_color="White", hovering_color="Red")

        QUIT_BACK.changeColor(QUIT_MOUSE_POS)
        QUIT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    change()
                if QUIT_BACK.checkForInput(QUIT_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def change():
    while True:
        LANANG_MOUSE_POS = pygame.mouse.get_pos()
        WEDOK_MOUSE_POS = pygame.mouse.get_pos()
        MAINMENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG,(0,0))

        CHANGE_TEXT = get_font(25).render("Silahkan pilih       karakter mu!", True, "#b68f40")
        CHANGE_RECT = CHANGE_TEXT.get_rect(center=(530, 130))
        SCREEN.blit(CHANGE_TEXT, CHANGE_RECT)

        LANANG_IMAGE = pygame.image.load(os.path.join("Assets/Design", "lanang1.png"))
        SCREEN.blit(LANANG_IMAGE, (290, 175))

        WEDOK_IMAGE = pygame.image.load(os.path.join("Assets/Design", "wedok1.png"))
        SCREEN.blit(WEDOK_IMAGE, (762, 175))


        LANANG_BACK = Button(image=None, pos=(315, 335), text_input="Lanang", font=get_font(25), base_color="White", hovering_color="Green")

        LANANG_BACK.changeColor(LANANG_MOUSE_POS)
        LANANG_BACK.update(SCREEN)

        WEDOK_BACK = Button(image=None, pos=(790, 335), text_input="Wedok", font=get_font(25), base_color="White", hovering_color="Pink")

        WEDOK_BACK.changeColor(WEDOK_MOUSE_POS)
        WEDOK_BACK.update(SCREEN)

        MAINMENU_BACK = Button(image=None, pos=(1000, 158), text_input="<- main menu", font=get_font(10), base_color="White", hovering_color="Red")

        MAINMENU_BACK.changeColor(MAINMENU_MOUSE_POS)
        MAINMENU_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LANANG_BACK.checkForInput(LANANG_MOUSE_POS):
                    run.lanang()
                if WEDOK_BACK.checkForInput(WEDOK_MOUSE_POS):
                    run.wedok()
                if MAINMENU_BACK.checkForInput(MAINMENU_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(60).render("MAIN   MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(552, 150))

        PLAY_BUTTON = Button(image=None, pos=(315, 275), text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")

        QUIT_BUTTON = Button(image=None, pos=(790, 275), text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
if __name__ == "__main__":
    main_menu()
    
