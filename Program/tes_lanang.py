import unittest
import pygame
import os
import random
from lanang import KarakterLanang, BalonUdara, Airship, Drum_Bergerak, Drum_Diam, Pesawat

class TestKarakterLanang(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.lanang = KarakterLanang()

    def test_initial_state(self):
        self.assertFalse(self.lanang.lanang_duck)
        self.assertTrue(self.lanang.lanang_run)
        self.assertFalse(self.lanang.lanang_jump)
        self.assertEqual(self.lanang.k_rect.x, 80)
        self.assertEqual(self.lanang.k_rect.y, 390)

    def test_duck(self):
        self.lanang.duck()
        self.assertEqual(self.lanang.k_rect.y, 410)

    def test_run(self):
        self.lanang.run()
        self.assertEqual(self.lanang.k_rect.y, 390)

    def test_jump(self):
        self.lanang.lanang_jump = True
        self.lanang.jump()
        self.assertLess(self.lanang.k_rect.y, 390)

class TestBalonUdara(unittest.TestCase):
    def setUp(self):
        self.balon = BalonUdara()

    def test_initial_position(self):
        self.assertGreaterEqual(self.balon.x, 1100 + 800)
        self.assertLessEqual(self.balon.y, 50)

    def test_update(self):
        initial_x = self.balon.x
        game_speed = 15
        self.balon.update(game_speed)
        self.assertLess(self.balon.x, initial_x)

class TestAirship(unittest.TestCase):
    def setUp(self):
        self.airship = Airship()

    def test_initial_position(self):
        self.assertLessEqual(self.airship.x, -800)
        self.assertLessEqual(self.airship.y, 50)

    def test_update(self):
        initial_x = self.airship.x
        game_speed = 15
        self.airship.update(game_speed)
        self.assertGreater(self.airship.x, initial_x)

class TestObstacles(unittest.TestCase):
    def setUp(self):
        self.drum_bergerak = Drum_Bergerak(pygame.image.load(os.path.join("Assets/Design", "drum_gerak.png")))
        self.drum_diam = Drum_Diam(pygame.image.load(os.path.join("Assets/Design", "drum_diam.png")))
        self.pesawat = Pesawat(pygame.image.load(os.path.join("Assets/Design", "pesawat.png")))

    def test_drum_bergerak_position(self):
        self.assertEqual(self.drum_bergerak.rect.y, 445)

    def test_drum_diam_position(self):
        self.assertEqual(self.drum_diam.rect.y, 420)

    def test_pesawat_position(self):
        self.assertEqual(self.pesawat.rect.y, 350)

if __name__ == "__main__":
    unittest.main()
