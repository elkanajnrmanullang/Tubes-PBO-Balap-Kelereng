def lanang():
   import lanang
   lanang.main()

def wedok():
   import wedok
   wedok.main()

def get_font(size):
   import pygame
   import os
   return pygame.font.Font(os.path.join("Assets/Other",'PressStart2P-Regular.ttf'), size)