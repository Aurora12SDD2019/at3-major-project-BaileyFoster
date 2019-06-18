""" Interactive game for The Restaurant at the end of the Universe
A longer description of the module with details that may help the user or anybody
reviewing the code later. make sure you outline in detail what the module does and how it can be used.
"""

__author__ = "Bailey Foster"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "bailey.foster5@education.nsw.com.au"
__status__ = "Alpha"

# dependencies
import pygame
import math


class Setup:
    def __init__(self):

        pygame.init()  # starts the game engine

        # set variables for some colours RGB (0-255)
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
        self.purple = (102, 102, 255)

        # sets size of screen/window
        self.WIDTH = 800
        self.HEIGHT = 600

        self.moveOn = False

        self.textbox = pygame.font.SysFont("Arial", 40)
        self.selections = pygame.font.SysFont("Arial", 20)
        self.ENOURMOUS = pygame.font.SysFont("Arial", 100)

        self.gameDisplay = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) # creates window and game screen

        self.clock = pygame.time.Clock()

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
                if Action == "quit":
                    pygame.quit()
                    quit()
                if Action == "help":
                    gameComponents.moveOn = True
                if Action == "menu":
                    gameComponents.moveOn = True
                if Action == "nextMenu":
                    menu.menuScreenNo += 1



        else:
            pygame.draw.rect(self.gameDisplay, theI, (theX, theY, theW, theH))

        smallText = pygame.font.SysFont("Arial", 50)
        textSurf, textRect = self.textStuff(msg, smallText)
        textRect.center = ((theX + (theW / 2)), (theY + (theH / 2)))
        self.gameDisplay.blit(textSurf, textRect)

    def eventGetter(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    levelAccess.lead_x_change = -0.25
                    levelAccess.lead_y_change = 0
                    levelAccess.rotation = 2
                elif event.key == pygame.K_d:
                    levelAccess.lead_x_change = 0.25
                    levelAccess.lead_y_change = 0
                    levelAccess.rotation = 1
                elif event.key == pygame.K_w:
                    levelAccess.lead_y_change = -0.25
                    levelAccess.lead_x_change = 0
                    levelAccess.rotation = 3
                elif event.key == pygame.K_s:
                    levelAccess.lead_y_change = 0.25
                    levelAccess.lead_x_change = 0
                    levelAccess.rotation = 4

        levelAccess.positionx += levelAccess.lead_x_change
        levelAccess.positiony += levelAccess.lead_y_change
class Levels:
    def __init__(self):
        self.coin = pygame.image.load(r'media\coin.png')
        self.animation1_RIGHT = pygame.image.load(r'media\pacWoman1\pacWoman1_RIGHT.png')
        self.animation2_RIGHT = pygame.image.load(r'media\pacWoman2\pacWoman2_RIGHT.png')
        self.animation1_LEFT = pygame.image.load(r'media\pacWoman1\pacWoman1_LEFT.png')
        self.animation2_LEFT = pygame.image.load(r'media\pacWoman2\pacWoman2_LEFT.png')
        self.animation1_DOWN = pygame.image.load(r'media\pacWoman1\pacWoman1_DOWN.png')
        self.animation2_DOWN = pygame.image.load(r'media\pacWoman2\pacWoman2_DOWN.png')
        self.animation1_UP = pygame.image.load(r'media\pacWoman1\pacWoman1_UP.png')
        self.animation2_UP = pygame.image.load(r'media\pacWoman2\pacWoman2_UP.png')
        self.rotation = 0
        self.positionx = 100
        self.positiony = 109
        self.lead_y_change = 0
        self.lead_x_change = 0
        self.currentAnimation = self.animation1_RIGHT

    def helpLevel(self):
        gameComponents.gameDisplay.fill(gameComponents.black)
        pygame.draw.line(gameComponents.gameDisplay, gameComponents.purple, (100, 100), (700, 100), 10)
        pygame.draw.line(gameComponents.gameDisplay, gameComponents.purple, (100, 150), (375, 150), 10)
        pygame.draw.line(gameComponents.gameDisplay, gameComponents.purple, (425, 150), (700, 150), 10)
        pygame.draw.line(gameComponents.gameDisplay, gameComponents.purple, (375, 146), (375, 500), 10)
        pygame.draw.line(gameComponents.gameDisplay, gameComponents.purple, (425, 146), (425, 500), 10)

        gameComponents.gameDisplay.blit(self.coin, (200, 120))
        gameComponents.gameDisplay.blit(self.coin, (395, 120))
        gameComponents.gameDisplay.blit(self.coin, (600, 120))
        gameComponents.gameDisplay.blit(self.coin, (395, 300))
        gameComponents.gameDisplay.blit(self.coin, (395, 475))

        if menu.frames < 30:
            if levelAccess.rotation == 1:
                self.currentAnimation = self.animation1_RIGHT
            if levelAccess.rotation == 2:
                self.currentAnimation = self.animation1_LEFT
            if levelAccess.rotation == 3:
                self.currentAnimation = self.animation1_UP
            if levelAccess.rotation == 4:
                self.currentAnimation = self.animation1_DOWN
        else:
            if levelAccess.rotation == 1:
                self.currentAnimation = self.animation2_RIGHT
            if levelAccess.rotation == 2:
                self.currentAnimation = self.animation2_LEFT
            if levelAccess.rotation == 3:
                self.currentAnimation = self.animation2_UP
            if levelAccess.rotation == 4:
                self.currentAnimation = self.animation2_DOWN

        gameComponents.gameDisplay.blit(self.currentAnimation, (levelAccess.positionx, levelAccess.positiony))

        gameComponents.eventGetter()

        if levelAccess.positionx >= gameComponents.WIDTH:
            levelAccess.positionx = 10
        if levelAccess.positionx <= 0:
            levelAccess.positionx = gameComponents.WIDTH - 10
        if levelAccess.positiony >= gameComponents.HEIGHT:
            levelAccess.positiony = 10
        if levelAccess.positiony <= 0:
            levelAccess.positiony = gameComponents.HEIGHT - 10

class Menu:
    def __init__(self):
        self.backGround1 = pygame.image.load(r'media\menuBackGround1.png')
        self.backGround2 = pygame.image.load(r'media\menuBackGround2.png')
        self.helpScreen1 = pygame.image.load(r'media\HelpScreen1.png')
        self.menuScreenNo = 0
        self.frames = 0

    def menuScreen(self):
        gameComponents.moveOn = False
        while not gameComponents.moveOn:
            if self.frames < 30:
                gameComponents.gameDisplay.blit(self.backGround1, (0, 0))
            else:
                gameComponents.gameDisplay.blit(self.backGround2, (0, 0))

            gameComponents.buttonify("play", 400, 150, 300, 100, gameComponents.green, gameComponents.brightGreen, "play")
            gameComponents.buttonify("help", 400, 275, 300, 100, gameComponents.blue, gameComponents.brightBlue, "help")
            gameComponents.buttonify("quit", 400, 400, 300, 100, gameComponents.red, gameComponents.brightRed, "quit")

            gameComponents.eventGetter()

            gameComponents.clock.tick(60)
            pygame.display.update()
            self.frames += 1
            if self.frames == 60:
                self.frames = 0

        self.helpScreen()

    def helpScreen(self):
        gameComponents.moveOn = False
        while not gameComponents.moveOn:

            gameComponents.gameDisplay.fill(gameComponents.black)
            if menu.menuScreenNo == 0:
                gameComponents.gameDisplay.blit(self.helpScreen1, (25, 0))
                gameComponents.buttonify("Back to Menu", 50, 400, 300, 100, gameComponents.red, gameComponents.brightRed, "menu")
                gameComponents.buttonify("Next Page", 450, 400, 300, 100, gameComponents.green, gameComponents.brightGreen, "nextMenu")
            elif menu.menuScreenNo == 1:
                levelAccess.helpLevel()
                self.frames += 1
                if self.frames == 60:
                    self.frames = 0


            gameComponents.eventGetter()

            pygame.display.update()



gameComponents = Setup()
menu = Menu()
levelAccess = Levels()
while True:
    menu.menuScreen()