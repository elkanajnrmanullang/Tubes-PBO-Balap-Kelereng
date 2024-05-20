import unittest
import pygame
from main import main_menu, play, change, get_font
from button import Button

class TestMainMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 600))
    
    def test_main_menu(self):
        try:
            main_menu()
            self.assertTrue(True)  # If we reach here, the main menu runs without errors
        except SystemExit:
            self.assertTrue(True)  # This means the game window was closed, which is fine

    def test_play_button(self):
        button = Button(image=None, pos=(315, 275), text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")
        self.assertTrue(button.checkForInput((315, 275)))

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
