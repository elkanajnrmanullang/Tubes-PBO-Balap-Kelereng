import unittest
import pygame
from lanang import KarakterLanang, BalonUdara, Airship

class TestKarakterLanang(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 600))
        self.lanang = KarakterLanang()
        self.balon_udara = BalonUdara()
        self.airship = Airship()

    def test_lanang_initial_position(self):
        self.assertEqual(self.lanang.lanang_rect.x, 80)
        self.assertEqual(self.lanang.lanang_rect.y, 390)

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
