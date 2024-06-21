import pygame
import time
from pygame.gfxdraw import pixel
import random
from math import pow,sqrt
class Solar_System():
    window = None
    starlist = []
    planetlist = []
    planetpos = [0,1,2,3,4,5,6,7]
    Sunlist = [150]
    axislist = [(643,470),(611,470),(571,470),(536,470),(496,470),(441,470),[392,470],(351,470)]
    radiuslist = [92,124,164,199,239,294,343,384]
    recordlist = [0,0,0,0,0,0,0,0]
    earth = True
    huo = True
    shui = True
    images = [
        ['./images/Mercury.gif',[735,378],[15,15]],
        ['./images/Venus.gif',[611,470],[30,30]],
        ['./images/Earth.gif',[735,306],[30,30]],
        ['./images/Mars.gif',[536,470],[20,20]],
        ['./images/Saturn.jpg',[496,470],[40,35]],
        ['./images/Venus.gif',[441,470],[50,50]],
        ['./images/Jupiter.gif',[392,470],[38,38]],
        ['./images/Neptune.gif',[351,470],[34,34]]
    ]
    def __init__(self):
        pass
    def start(self):
        pygame.init()
        pygame.display.init()
        Solar_System.window=pygame.display.set_mode([1550,900])
        bgr = background()
        while True:
            self.creatstar()
            self.event()
            self.creatplanet()
            bgr.display()
            Sun().display()
            self.blitstar()
            self.blitlplanet()
            time.sleep(0.01)
            self.disapper()
            pygame.display.update()

    def event(self):
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
    def creatstar(self):
        for i in range(20):
            x = random.randint(1,1550)
            y = random.randint(1,900)
            startstar=star(x,y)
            Solar_System.starlist.append(startstar)


    def creatplanet(self):
        for i in Solar_System.planetpos:
            if  175 <= Solar_System.Sunlist[0] < 198 and Solar_System.shui:
                Solar_System.planetpos.remove(0)
                #不清楚为什么移除之后会出现卡顿问题
                Solar_System.shui = False
            if  198 <= Solar_System.Sunlist[0] < 278 and Solar_System.huo:
                Solar_System.planetpos.remove(1)
                Solar_System.huo = False
            if  Solar_System.Sunlist[0] >= 278 and Solar_System.earth:
                Solar_System.planetpos.remove(2)
                Solar_System.earth= False
            Solar_System.planetlist.append(
                Planet(Solar_System.images[i][0], move(i).posistion(), Solar_System.images[i][2])
            )
    def blitlplanet(self):
        for planet in Solar_System.planetlist:
           #print(planet)
            if planet.live:
                    planet.display()
                    planet.live =False
            else:
                Solar_System.planetlist.remove(planet)


    def blitstar(self):
        for star in Solar_System.starlist:
            star.display()

    def disapper(self):
        for i in Solar_System.starlist:
            Solar_System.starlist.remove(i)



class Sun():
    def __init__(self):
        self.x = Solar_System.Sunlist[0]
        if Solar_System.Sunlist[0] < 358:
            Solar_System.Sunlist[0] += 0.1
            self.image = pygame.image.load('./images/Sun.gif')
        else:
            self.image = pygame.image.load('./images/white_dwarf.jpg')
        self.image_scaler=pygame.transform.scale(self.image,[self.x,self.x])#150 150
        self.rect = self.image_scaler.get_rect()
    def display(self):
        rect = self.calculate()
        Solar_System.window.blit(self.image_scaler, rect)#670 400

    def calculate(self):
        if Solar_System.Sunlist[0] < 198:
            planet_width = 7
        else:
            planet_width = 15
        width = self.rect.width
        pos_x = 735 - width/2
        pos_y = 470 - width/2 + planet_width
        return (pos_x,pos_y)



class background():
    def __init__(self):
        pass
    def display(self):
        bgr = pygame.transform.scale(pygame.image.load('./images/starry sky.jpg'), [1550, 900])
        Solar_System.window.blit(bgr, [0, 0])

class star():
    def __init__(self,x,y):
       self.x = x
       self.y = y
    def display(self):
        pixel(Solar_System.window,self.x,self.y,pygame.Color(255,255,255))
class Planet():
    def __init__(self,image,pos,scaler):
        self.image=pygame.image.load(image)
        self.image_scaler = pygame.transform.scale(self.image, scaler)
        self.rect = self.image_scaler.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
        self.live = True
    def display(self):
          #print(self.rect.left,self.rect.top)
          Solar_System.window.blit(self.image_scaler,self.rect)
class move():
     def __init__(self,temp):
         self.temp = temp
         self.x,self.y = Solar_System.axislist[temp]
         self.speed = 1
         self.r = Solar_System.radiuslist[temp]

     def col(self):
         y = sqrt(self.r**2-pow(abs(self.x-735),2))
         return y

     def posistion(self):
         if Solar_System.recordlist[self.temp]>= self.r * 4:
             Solar_System.recordlist[self.temp] = 0
         if 0<=Solar_System.recordlist[self.temp] < self.r:
             self.x += self.speed
             self.y = 470 - self.col()
         if self.r <= Solar_System.recordlist[self.temp]<self.r*2:
             self.x+=self.speed
             self.y = 470 - self.col()
         if self.r*2<= Solar_System.recordlist[self.temp]<self.r*3:
             self.x-= self.speed
             self.y = 470 + self.col()
         if self.r*3<=Solar_System.recordlist[self.temp]<self.r*4:
             self.x -= self.speed
             self.y = 470 + self.col()
         #print("record值是：", Solar_System.recordlist[self.temp])
         Solar_System.recordlist[self.temp] += 1
         Solar_System.axislist[self.temp] = (self.x,self.y)
         return (self.x,self.y)


if __name__ == '__main__':
    Solar_System().start()


