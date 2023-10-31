import pygame

class Tiktekto:
    def __init__(self):
        pygame.init()
        
        self.size = width, height = 640, 320
        self.background = (224, 241, 244)
        self.color_game = (0, 55, 61)
        self.screen = pygame.display.set_mode(self.size)
        print("Hello")