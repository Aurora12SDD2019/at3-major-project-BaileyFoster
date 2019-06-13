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


        else:
            pygame.draw.rect(self.gameDisplay, theI, (theX, theY, theW, theH))

        smallText = pygame.font.SysFont("Arial", 50)
        textSurf, textRect = self.textStuff(msg, smallText)
        textRect.center = ((theX + (theW / 2)), (theY + (theH / 2)))
        self.gameDisplay.blit(textSurf, textRect)


class Menu:
    def __init__(self):
        self.backGround1 = pygame.image.load(r'C:\at3-major-project-BaileyFoster\media\menuBackGround1.png')
        self.backGround2 = pygame.image.load(r'C:\at3-major-project-BaileyFoster\media\menuBackGround2.png')
        self.frames = 0

    def menuScreen(self):
        while not gameComponents.moveOn:
            if self.frames < 30:
                gameComponents.gameDisplay.blit(self.backGround1, (0, 0))
            else:
                gameComponents.gameDisplay.blit(self.backGround2, (0, 0))

            gameComponents.buttonify("play", 400, 150, 300, 100, gameComponents.green, gameComponents.brightGreen, "play")
            gameComponents.buttonify("help", 400, 275, 300, 100, gameComponents.blue, gameComponents.brightBlue, "help")
            gameComponents.buttonify("quit", 400, 400, 300, 100, gameComponents.red, gameComponents.brightRed, "quit")


            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameComponents.clock.tick(60)
            pygame.display.update()
            self.frames += 1
            if self.frames == 60:
                self.frames = 0

    def helpScreen(self):
        gameComponents.moveOn = False
        while not gameComponents.moveOn:
            gameComponents.gameDisplay.fill(gameComponents.black)



gameComponents = Setup()
menu = Menu()
menu.menuScreen()