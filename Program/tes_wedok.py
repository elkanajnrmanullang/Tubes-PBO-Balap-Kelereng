import unittest
import pygame
import random
import os
from wedok import KarakterWedok, BalonUdara, Airship, Drum_Bergerak, Drum_Diam, Pesawat

class TestKarakterWedok(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.wedok = KarakterWedok()

    def test_initial_state(self):
        self.assertFalse(self.wedok.k_duck)
        self.assertTrue(self.wedok.k_run)
        self.assertFalse(self.wedok.k_jump)
        self.assertEqual(self.wedok.k_rect.x, 80)
        self.assertEqual(self.wedok.k_rect.y, 390)

    def test_duck(self):
        self.wedok.k_duck = True
        self.wedok.k_run = False
        self.wedok.k_jump = False
        self.wedok.duck()
        self.assertEqual(self.wedok.k_rect.y, 410)

    def test_run(self):
        self.wedok.k_duck = False
        self.wedok.k_run = True
        self.wedok.k_jump = False
        self.wedok.run()
        self.assertEqual(self.wedok.k_rect.y, 390)

    def test_jump(self):
        self.wedok.k_jump = True
        initial_y = self.wedok.k_rect.y
        self.wedok.jump()
        self.assertLess(self.wedok.k_rect.y, initial_y)

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
        self.drum_bergerak = Drum_Bergerak(pygame.image.load(os.path.join("Assets/Design", "drum_gerak.png")).convert_alpha())
        self.drum_diam = Drum_Diam(pygame.image.load(os.path.join("Assets/Design", "drum_diam.png")).convert_alpha())
        self.pesawat = Pesawat(pygame.image.load(os.path.join("Assets/Design", "pesawat.png")).convert_alpha())

    def test_drum_bergerak_position(self):
        self.assertEqual(self.drum_bergerak.rect.y, 445)

    def test_drum_diam_position(self):
        self.assertEqual(self.drum_diam.rect.y, 420)

    def test_pesawat_position(self):
        self.assertEqual(self.pesawat.rect.y, 350)

if __name__ == "__main__":
    unittest.main()
