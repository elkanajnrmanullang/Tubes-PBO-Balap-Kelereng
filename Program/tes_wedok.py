import unittest
import pygame
from wedok import KarakterWedok, BalonUdara, Airship

class TestKarakterWedok(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 600))
        self.wedok = KarakterWedok()
        self.balon_udara = BalonUdara()
        self.airship = Airship()

    def test_wedok_initial_position(self):
        self.assertEqual(self.wedok.wedok_rect.x, 80)
        self.assertEqual(self.wedok.wedok_rect.y, 390)

    def test_balon_udara_initial_position(self):
        self.assertTrue(self.balon_udara.x > 1100)
        self.assertTrue(10 <= self.balon_udara.y <= 50)

    def test_airship_initial_position(self):
        self.assertTrue(self.airship.x < 0)
        self.assertTrue(10 <= self.airship.y <= 50)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
