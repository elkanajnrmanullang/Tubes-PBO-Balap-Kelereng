import unittest
from unittest.mock import MagicMock
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        main.pygame.init()
        main.pygame.display.set_mode = MagicMock()

    def test_main_menu(self):
        main.main_menu()  # Simply check if main menu runs without errors

    def test_play_function(self):
        # Mocking pygame functions and methods
        main.pygame.mouse.get_pos = MagicMock(return_value=(0, 0))
        main.pygame.quit = MagicMock()
        main.sys.exit = MagicMock()
        main.change = MagicMock()
        main.main_menu = MagicMock()

        main.play()  # Simply check if play function runs without errors

if __name__ == '__main__':
    unittest.main()
