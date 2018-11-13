import pygame
import sys
import random

pygame.init()
size = width,height =640,480
black = [0,0,0]
white = (255,255,255)
color_iter = [-0.25,0.25,-0.25]
col = [254,1,254]
game_over = False
b_in_game = 20
pygame.display.set_caption("Kill the bubbles")

class Object():
    ''' MAin class '''
    count = 0
    def __init__(self, coord = None):
        self.size = 10 * random.choice((5,2,8))
        self.x =coord [0] if coord else random.random() * (width-self.size)
        self.y =coord [1] if coord else random.random() * (height -self.size)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.__class__.count += 1


    def draw(self,screen):
        pygame.draw.rect(screen,self.color ,(self.x,self.y,self.size,self.size))

class Movable(Object):
    def __init__(self,coord=None):
        Object.__init__(self,coord)
        self.vector = [random.choice((-1,1)) * random.random(), random.choice((-1,1)) * random.random()]
    def move(self):
        self.x += self.vector[0]
        self.y += self.vector[1]
        if self.x <= 0 or self.x >= width - self.size: self.vector[0] *= -1
        if self.y <= 0 or self.y >= height - self.size: self.vector[1] *= -1

class Buble(Movable):
    def __init__(self):
        Movable.__init__(self)
        self.image = pygame.transform.scale( pygame.image.load('buble.png'), (self.size, self.size))
        self.alive = True

    def draw(self,screen):
        screen.blit(self.image, (self.x,self.y))

class Text():
    def __init__(self):
        self.text_color = white
        self.font = pygame.font.SysFont(None,30)

    def text_dr(self,screen,text,x,y):
        self.text = self.font.render(text,True,self.text_color)
        self.text_r = self.text.get_rect()
        self.text_r.x = x
        self.text_r.y = y
        screen.blit(self.text,self.text_r)


def color_changer(col,color_iter):
    if 0 < col[0] < 255:
        for i in xrange(3): col[i] += color_iter[i]
    else:
        for i in xrange(3):
            color_iter[i] *= -1
            col[i] += color_iter[i]
    return col,color_iter

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
m_bubls = [Buble() for i in xrange(b_in_game)]
m_clics = 0
info = Text()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_clics += 1
            mx , my = pygame.mouse.get_pos()
            for i in m_bubls:
                if (i.x <= mx < i.x + i.size) and (i.y <= my < i.y + i.size) and i.alive:
                    i.alive = False
                    Buble.count -= 1

    col,color_iter=color_changer(col,color_iter)

    screen.fill(col)
    info.text_dr(screen,'Bubbles left: ' + str(Buble.count) ,10,10)
    info.text_dr(screen,'Shots: ' + str(m_clics),10,40)

    for obj in m_bubls:
        if obj.alive:
            obj.move()
            obj.draw(screen)
    pygame.display.flip()
    clock.tick(60+(m_clics*5))
    if Buble.count == 0:
        game_over = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             sys.exit()
    screen.fill(black)
    info.text_dr(screen,'You did ' + str(m_clics) + ' shots for '
                                   + str(b_in_game) +
                                   ' bubbles.',width/2-140,height/2-50)
    if m_clics == b_in_game:
        info.text_dr(screen,'Good result',width/2-50,height/2-15)
    elif m_clics < b_in_game:
        info.text_dr(screen,'Excellent result',width/2-80,height/2-15)
    elif m_clics > b_in_game:
        info.text_dr(screen,'Bad result',width/2-50,height/2-15)
    pygame.display.flip()
