import pygame
from pygame.locals import *
import sys
import time
import random
import pyjokes
pygame.init()
pygame.display.set_caption('Rocket Type Tester')
screen = pygame.display.set_mode((1280, 700), 0, 32)

#  background music:
music = pygame.mixer.music.load('Efence%20-%20Spaceflight.mp3')
pygame.mixer.music.play(-1)

#  class for the main menu:
class MainMenu():
    def __init__(self):
        self.width = 1280
        self.height = 700
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.font = pygame.font.SysFont(None, 50)
        self.main_menu_image = pygame.image.load('images/Rocket Type tester made by klein cafa.png')
        self.main_menu_image = pygame.transform.scale(self.main_menu_image, (self.width, self.height))
        self.easteregg2_image = pygame.image.load('images/IMG_1435.png')
        self.easteregg2_image = pygame.transform.scale(self.easteregg2_image, (self.width, self.height))

    #  function for drawing text onto the screen:
    def draw_text(self, text, font, fsize, color, surface, x, y):
        self.font = pygame.font.SysFont(None, fsize)
        self.textobj = font.render(text, 1, color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (x, y)
        self.screen.blit(self.textobj, self.textrect)

    click = False

    #  function for the main menu showing onto the screen:
    def main_menu(self):
        while True:
            screen.fill((0, 0, 0))
            self.screen.blit(self.main_menu_image, (0, 0))
            #self.screen.fill((0, 0, 0), (200, 400, 170, 160))

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(485, 231, 312, 69)
            button_2 = pygame.Rect(485, 340, 312, 69)
            button_3 = pygame.Rect(485, 450, 312, 69)
            button_4 = pygame.Rect(485, 560, 312, 69)
            easteregg1 = pygame.Rect(80, 200, 140, 120)
            easteregg2 = pygame.Rect(200, 400, 170, 160)
            if button_1.collidepoint((mx, my)):
                if click:
                    print('game')
                    Game().run()
            if button_2.collidepoint((mx, my)):
                if click:
                    print('tutorial')
                    Tutorial4().tutorialMenu()
            if button_3.collidepoint((mx, my)):
                if click:
                    print('credits')
                    self.credits()
                    return
            if button_4.collidepoint((mx, my)):
                if click:
                    print('exit')
                    pygame.quit()
                    sys.exit()
            if easteregg1.collidepoint((mx, my)):
                if click:
                    self.easteregg1()
                    return

            if easteregg2.collidepoint((mx, my)):
                if click:
                    self.easteregg2()
                    return

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.mainClock.tick(60)

    def easteregg1(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            self.draw_text('Mr. Slater is an awesome teacher!', self.font, 50, (0, 0, 0), self.screen, 580, 360)
            pygame.display.update()
            self.mainClock.tick(60)

    def easteregg2(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.easteregg2_image, (0, 0))
            self.draw_text('the best squad in ICS3U :-D', self.font, 50, (0, 0, 0), self.screen, 580, 300)
            pygame.display.update()
            self.mainClock.tick(60)

    def credits(self):
        running = True
        while running:
            self.screen.fill((51, 153, 255))
            #self.screen.blit(self.main_menu_image, (0, 0))
            self.draw_text('Credits', self.font, 50, (255, 255, 255), self.screen, 580, 0)
            self.draw_text('Created by Klein Cafa', self.font, 30, (255, 255, 255), self.screen, 20, 60)
            self.draw_text('Thank you to the following!', self.font, 30, (255, 255, 255), self.screen, 20, 120)
            self.draw_text('- Charlotte Selda', self.font, 30, (255, 255, 255), self.screen, 20, 180)
            self.draw_text('- Evan Tordorf', self.font, 30, (255, 255, 255), self.screen, 20, 240)
            self.draw_text('- Landon Roberts', self.font, 30, (255, 255, 255), self.screen, 20, 300)
            self.draw_text('- Mr. Hofstatter', self.font, 30, (255, 255, 255), self.screen, 20, 360)
            self.draw_text('Click SPACE to start the game!', self.font, 50, (255, 255, 255), self.screen, 20, 500)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        Game().run()
            pygame.display.update()
            self.mainClock.tick(60)

#  class for the game:
class Game():
    def __init__(self):
        self.w = 1280
        self.h = 700
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time: 0 Accuracy: 0% WPM: 0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)

        pygame.init()

        self.open_img = pygame.image.load('images/jfkAU4tM8XMUAPZDm4h5Nh-1200-80.jpeg')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))

        self.bg = pygame.image.load('images/background.png')
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))

        self.screen = pygame.display.set_mode((self.w, self.h))

    #  function for drawing text onto the screen:
    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    #  function for getting a sentence from the module, pygames:
    def get_sentence(self):
        sentence = pyjokes.get_joke()
        if len(sentence) <= 75:
            return sentence

    #  function for calculating and blitting a restart button:
    def show_results(self, screen):
        if(not self.end):

            #  calculate time:
            self.total_time = time.time() - self.time_start

            #  calculate accuracy:
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)*100

            #  calculate words per minute:
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)

            self.results = 'Time: '+str(round(self.total_time)) + " seconds  |  Accuracy: " + str(
                round(self.accuracy)) + "%" + '  |  Words per Minute: ' + str(round(self.wpm)) + " WPM"

            # draw icon image
            self.time_img = pygame.image.load('images/restart.png')
            self.time_img = pygame.transform.scale(self.time_img, (307, 180))

            #screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (480, 525)) #ORIGINAL
            #screen.blit(self.time_img, (71, 528))
            #self.draw_text(screen, "Go to Leaderboard", self.h - 70, 26, (100, 100, 100))

            print(self.results)
            pygame.display.update()

    #  the main function, which is running the entire game class:
    def run(self):
        self.reset_game()

        self.running = True
        while(self.running):
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (230, 400, 820, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (230, 400, 820, 50), 2)

            # updating the user input:
            self.draw_text(self.screen, self.input_text, 425, 26, (250, 250, 250))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # position of the input box:
                    if(x >= 230 and x <= 820 and y >= 395 and y <= 450):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                     # position of reset box:
                    if(x >= 510 and x <= 751 and y >= 580 and y <= 650):
                        self.reset_game()
                        519, 587, 232, 60
                        x, y = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass

            pygame.display.update()

        clock.tick(60)

    # function for resetting the game as soon as 'start' is pressed, as well as when 'restart' is pressed:
    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))
        self.draw_text(self.screen, 'Loading...', self.h/2, 60, self.HEAD_C)
        self.draw_text(self.screen, self.get_sentence(), 400, 30, (255, 255, 255))
        pygame.display.update()
        time.sleep(2)
        self.reset = False
        self.end = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # getting a random sentence from the get_sentence function:
        self.word = self.get_sentence()
        if (not self.word):
            self.reset_game()

        # blitting the loading image:
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))

        # drawing the rectangle for the input box:
        pygame.draw.rect(self.screen, (255, 192, 25), (230, 400, 820, 50), 2)

        # drawing the sequence (sentence) string:
        self.draw_text(self.screen, self.word, 300, 30, self.TEXT_C)
        print(self.word)

        pygame.display.update()

# class for the tutorial:
class Tutorial4():
    def __init__(self):
        self.width = 1280
        self.height = 700
        self.RESULT_C = (255, 70, 70)
        self.results = 'Time:0 Accuracy:0% WPM:0'
        self.mainClock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.font = pygame.font.SysFont(None, 50)
        self.main_menu_image = pygame.image.load('images/Rocket Type tester made by klein cafa.png')
        self.main_menu_image = pygame.transform.scale(self.main_menu_image, (self.width, self.height))

        self.tutorial_1 = pygame.image.load('images/tutorial1.png')
        self.tutorial_1 = pygame.transform.scale(self.tutorial_1, (self.width, self.height))

        self.tutorial_2 = pygame.image.load('images/tutorial2.png')
        self.tutorial_2 = pygame.transform.scale(self.tutorial_2, (self.width, self.height))

        self.tutorial_3 = pygame.image.load('images/tutorial3.png')
        self.tutorial_3 = pygame.transform.scale(self.tutorial_3, (self.width, self.height))

        self.tutorial_4 = pygame.image.load('images/tutorial4.png')
        self.tutorial_4 = pygame.transform.scale(self.tutorial_4, (self.width, self.height))

        self.tutorial_5 = pygame.image.load('images/tutorial5.png')
        self.tutorial_5 = pygame.transform.scale(self.tutorial_5, (self.width, self.height))

        self.tutorial_6 = pygame.image.load('images/tutorial6.png')
        self.tutorial_6 = pygame.transform.scale(self.tutorial_6, (self.width, self.height))

        self.tutorial_7 = pygame.image.load('images/tutorial7.png')
        self.tutorial_7 = pygame.transform.scale(self.tutorial_7, (self.width, self.height))

        self.tutorial_8 = pygame.image.load('images/tutorial8.png')
        self.tutorial_8 = pygame.transform.scale(self.tutorial_8, (self.width, self.height))

        self.tutorial_9 = pygame.image.load('images/tutorial9.png')
        self.tutorial_9 = pygame.transform.scale(self.tutorial_9, (self.width, self.height))

        self.tutorial_10 = pygame.image.load('images/tutorial10.png')
        self.tutorial_10 = pygame.transform.scale(self.tutorial_10, (self.width, self.height))

        self.tutorial_11 = pygame.image.load('images/tutorial11.png')
        self.tutorial_11 = pygame.transform.scale(self.tutorial_11, (self.width, self.height))

        self.tutorial_12 = pygame.image.load('images/tutorial12.png')
        self.tutorial_12 = pygame.transform.scale(self.tutorial_12, (self.width, self.height))

        self.tutorial_13 = pygame.image.load('images/tutorial13.png')
        self.tutorial_13 = pygame.transform.scale(self.tutorial_13, (self.width, self.height))

        self.tutorial_14 = pygame.image.load('images/tutorial14.png')
        self.tutorial_14 = pygame.transform.scale(self.tutorial_14, (self.width, self.height))

        self.tutorial_15 = pygame.image.load('images/tutorial15.png')
        self.tutorial_15 = pygame.transform.scale(self.tutorial_15, (self.width, self.height))

        self.tutorial_16 = pygame.image.load('images/tutorial16.png')
        self.tutorial_16 = pygame.transform.scale(self.tutorial_16, (self.width, self.height))

        self.tutorial_17 = pygame.image.load('images/tutorial17.png')
        self.tutorial_17 = pygame.transform.scale(self.tutorial_17, (self.width, self.height))

        self.sequence = pyjokes.get_joke(language='en', category='neutral')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.width / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    # here is a function where after each tutorial function, it will return back to this menu and go to the next
    # function stated below the completed function:
    def tutorialMenu(self):
        self.tutorial()
        self.tutorial2()
        self.tutorial3()
        self.tutorial4()
        self.tutorial5()
        self.tutorial6()
        self.tutorial7()
        self.tutorial8()
        self.tutorial9()
        self.tutorial10()
        self.tutorial11()
        self.tutorial12()
        self.tutorial13()
        self.tutorial14()
        self.tutorial15()
        self.tutorial16()
        self.tutorial17()
        return


    def tutorial(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_1, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial2(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_2, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial3(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_3, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial4(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_4, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial5(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_5, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial6(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_6, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial7(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_7, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial8(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_8, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial9(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_9, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial10(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_10, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial11(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_11, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial12(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_12, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial13(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_13, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial14(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_14, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial15(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_15, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial16(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_16, (0, 0))
        self.time_img = pygame.image.load('images/restart.png')
        self.time_img = pygame.transform.scale(self.time_img, (307, 180))
        screen.blit(self.time_img, (480, 525))  # ORIGINAL
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

    def tutorial17(self):
        running = True
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.tutorial_17, (0, 0))
        pygame.display.update()
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_SPACE:
                        return
            self.mainClock.tick(60)

MainMenu().main_menu()