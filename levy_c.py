import pygame
import math
from color import get_rgb, HEIGHT, WIDTH
import time

LEVY_C_INSERT = [1, 0, -1, -1, 0, 1]
LEVY_C_SQUARE = [-1, 0, -1, -1, 0, -1, -1, 0, -1, -1, 0, -1]


class LevyC:
    def __init__(self, iter=0):
        self.iter = iter
        self.instructions = LEVY_C_SQUARE.copy()
        self.instructions = self.fractal_array(iter)
        self.length = HEIGHT / (2.0 * math.pow(2, (iter) / 2))
        self.starting_point = ((WIDTH / 2.0), (3.0 * HEIGHT / 4.0))
        self.next_point = self.starting_point
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.angle = 0.0
        pygame.display.set_caption('Levy C')

    def fractal_array(self, x=1):
        if x == 0:
            return self.instructions
        output = []
        for i in self.instructions:
            if i == 0:
                output.extend(LEVY_C_INSERT)
            else:
                output.append(i)
        self.instructions.clear()
        self.instructions = output
        return self.fractal_array(x - 1)

    def draw(self, gradient=0, color_scheme=0, color_values=((0, HEIGHT), (200, 0), (200, 0), (0, 255))):
        for i in self.instructions:
            if i != 0:
                self.angle += (float(i) * math.pi) / 4.0
            else:
                sx, sy = self.next_point
                rgb = get_rgb(self.next_point, gradient,
                              color_scheme, color_values)
                nx = sx + (self.length * math.cos(self.angle))
                ny = sy + (self.length * math.sin(self.angle))
                self.next_point = (nx, ny)
                pygame.draw.line(
                    self.window, rgb, (sx, sy), self.next_point, 1)
        self.next_point = self.starting_point

    def run(self):
        #font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 18)
        #text = font.render('GeeksForGeeks', True, (255, 255, 255))
        #textRect = text.get_rect()
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Levy C')
        done = False
        j = self.iter
        self.length = HEIGHT / (2.0 * math.pow(2, (self.iter + 1) / 2))
        self.starting_point = ((WIDTH / 2.0), (3.0 * HEIGHT / 4.0))
        color_scheme = 0
        gradient = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            keys = pygame.key.get_pressed()
            pygame.time.delay(10)
            self.draw(gradient, color_scheme)
            if keys[pygame.K_KP_ENTER]:
                window.fill((0, 0, 0))
                #pygame.draw.line(window, (255, 255, 255), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
                #pygame.draw.line(window, (255, 255, 255), (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))
                j += 1
                self.angle = 0
                '''
                textRect = (10, 10)
                text = font.render('Length of Array: ' + str(len(array)), True, (255, 255, 255))
                window.blit(text, textRect)
                textRect = (10, 30)
                text = font.render('Iteration: ' + str(j), True, (255, 255, 255))
                window.blit(text, textRect)
                '''
                self.length = HEIGHT / (2.0 * math.pow(2, (j + 1) / 2)) - .01
                self.starting_point = ((WIDTH / 2.0), (3.0 * HEIGHT / 4.0))
                self.fractal_array(1)
                print('Iteration: ' + str(j) +
                      '\n# of directions: ' + str(len(self.instructions)))
                pygame.time.delay(100)
            elif keys[pygame.K_KP_PERIOD]:
                window.fill((0, 0, 0))
                #pygame.draw.line(window, (255, 255, 255), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
                #pygame.draw.line(window, (255, 255, 255), (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))
                j = 0
                self.angle = 0
                '''
                textRect = (10, 10)
                text = font.render('Length of Array: ' + str(len(array)), True, (255, 255, 255))
                window.blit(text, textRect)
                textRect = (10, 30)
                text = font.render('Iteration: ' + str(j), True, (255, 255, 255))
                window.blit(text, textRect)
                '''
                self.length = HEIGHT / (2.0 * math.pow(2, (j + 1) / 2))
                self.starting_point = ((WIDTH / 2.0), (3.0 * HEIGHT / 4.0))
                self.instructions = LEVY_C_SQUARE.copy()
                print('Iteration: ' + str(j) +
                      '\n# of directions: ' + str(len(self.instructions)))
            elif keys[pygame.K_ESCAPE]:
                pygame.image.save(window, 'LevySquareScreenshot2.jpeg')
                done = True
            elif keys[pygame.K_KP0]:
                color_scheme = 0
            elif keys[pygame.K_KP1]:
                color_scheme = 1
            elif keys[pygame.K_KP2]:
                color_scheme = 2
            elif keys[pygame.K_KP3]:
                color_scheme = 3
            elif keys[pygame.K_KP4]:
                color_scheme = 4
            elif keys[pygame.K_KP5]:
                color_scheme = 5
            elif keys[pygame.K_KP6]:
                color_scheme = 6
            elif keys[pygame.K_KP7]:
                color_scheme = 7
            elif keys[pygame.K_KP8]:
                color_scheme = 8
            elif keys[pygame.K_KP9]:
                color_scheme = 9
            elif keys[pygame.K_0]:
                gradient = 0
            elif keys[pygame.K_1]:
                gradient = 1
            elif keys[pygame.K_2]:
                gradient = 2
            elif keys[pygame.K_3]:
                gradient = 3
            elif keys[pygame.K_4]:
                gradient = 4
            elif keys[pygame.K_5]:
                gradient = 5
            elif keys[pygame.K_6]:
                gradient = 6
            elif keys[pygame.K_7]:
                gradient = 7
            elif keys[pygame.K_8]:
                gradient = 8
            elif keys[pygame.K_9]:
                gradient = 9
            pygame.display.update()


x = int(input("How Many Iterations (Recommended 15 or less):\n"))
levy = LevyC(x)
levy.run()
