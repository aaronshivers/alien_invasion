import pygame


class Ship:

    def __init__(self, ai_game):
        # initialize the ship and its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom corner of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
