import pygame
import time
import random
import os
import sys

class Setup:
    def __init__(self):

        pygame.init()

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (200, 0, 0)
        self.brightRed = (255, 0, 0)
        self.green = (0, 200, 0)
        self.brightGreen = (0, 255, 0)
        self.blue = (0, 0, 200)
        self.brightBlue = (0, 0, 255)
        self.orange = (255, 69, 0)
        self.brightOrange = (255, 127, 80)

        self.WIDTH = 800
        self.HEIGHT = 600

        self.textbox = pygame.font.SysFont("Arial", 40)
        self.selections = pygame.font.SysFont("Arial", 20)
        self.ENOURMOUS = pygame.font.SysFont("Arial", 100)

        self.gameDisplay = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        pygame.display.set_caption('inProgress')

        def custom_message(self, textType, msg, colour, theX, theY):  # this function is used to put messages on the screen
            screen_text = textType.render(msg, True, colour)  # sets what the display will look like
            self.gameDisplay.blit(screen_text, [theX, theY])  # puts the text on the screen with the given coordinates

        def textStuff(self, text, font):
            textSurface = font.render(text, True, self.black)
            return textSurface, textSurface.get_rect()

        def buttonify(self, msg, theX, theY, theW, theH, theI, theA, Action=None):  # this function setus up buttons on the screen
            mouse = pygame.mouse.get_pos()  # gets the mouse position
            click = pygame.mouse.get_pressed()  # gets whether the mouse is clicked

            if theX + theW > mouse[0] > theX and theY + theH > mouse[
                1] > theY:  # checks if the mouse is colliding with the button
                pygame.draw.rect(self.gameDisplay, theA, (theX, theY, theW, theH))
                if click[0] == 1 and Action != None:  # checks if the mouse is clicked and what to trigger
                    None

            else:
                pygame.draw.rect(self.gameDisplay, theI, (theX, theY, theW, theH))

            smallText = pygame.font.SysFont("Arial", 20)
            textSurf, textRect = Setup.self.textStuff(msg, smallText)
            textRect.center = ((theX + (theW / 2)), (theY + (theH / 2)))
            self.gameDisplay.blit(textSurf, textRect)


gameComponents = Setup()
