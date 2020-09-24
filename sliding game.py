import pygame
import random
from pygame.locals import *
pygame.init()
width=720
height=480
bwidth=120
bheight=120
columns=3
rows=3
box=[False,False,False,False,False,False,False,False]
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption("Sliding Game")
image=pygame.image.load("1.jpg")
image=pygame.transform.scale(image,(360,360))
black=pygame.image.load("black.png")
black=pygame.transform.scale(black,(120,120))
start=False
showing_solution = False
rectcolor=(255,255,255)
rectcolor2=(255,255,255)
recwidth=2
click=[]
display =[False,False,False,False,False,False,False,False,False]
#a=[random.randint(1,3),random.randint(0,7),random.randint(0,7),random.randint(0,7),random.randint(0,7),random.randint(0,7),random.randint(0,7),random.randint(0,7),random.randint(0,7)]
a=[2,3,6,7,0,5,4,1]
coord=[(0,0,120,120),(120,0,120,120),(240,0,120,120),(0,120,120,120),(120,120,120,120),(240,120,120,120),(0,240,120,120),(120,240,120,120),(240,240,120,120)]
b=screen.blit(image, (180,50),coord[2])
v=120
tiles ={}
class Slidingi():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def draw(self):
        screen.set_at((1,0), (0, 0, 1, 255))
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.w,self.h),recwidth)
class player():
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
    def draw(self):
        X=self.x
        Y=self.y
        X1=self.x+120
        X2=self.x+240
        Y1=self.y+120
        Y2=self.y+240
        if(start==False):
            screen.blit(image, (X,Y),coord[0])
            pygame.draw.rect(screen,rectcolor,(X,Y,self.w,self.h),recwidth)
            screen.blit(image, (X1,Y),coord[1])
            pygame.draw.rect(screen,rectcolor,(X1,Y,self.w,self.h),recwidth)
            screen.blit(image, (X2,Y),coord[2])
            pygame.draw.rect(screen,rectcolor,(X2,Y,self.w,self.h),recwidth)
            screen.blit(image, (X,Y1),coord[3])
            pygame.draw.rect(screen,rectcolor,(X,Y1,self.w,self.h),recwidth)
            screen.blit(image, (X1,Y1),coord[4])
            pygame.draw.rect(screen,rectcolor,(X1,Y1,self.w,self.h),recwidth)
            screen.blit(image, (X2,Y1),coord[5])
            pygame.draw.rect(screen,rectcolor,(X2,Y1,self.w,self.h),recwidth)
            screen.blit(image, (X,Y2),coord[6])
            pygame.draw.rect(screen,rectcolor,(X,Y2,self.w,self.h),recwidth)
            screen.blit(image, (X1,Y2),coord[7])
            pygame.draw.rect(screen,rectcolor,(X1,Y2,self.w,self.h),recwidth)
            screen.blit(black, (X2,Y2))
            pygame.draw.rect(screen,rectcolor2,(X2,Y2,self.w,self.h),recwidth)
        else:
            if(display[0]==True):
                screen.blit(black, (X,Y))
                pygame.draw.rect(screen,rectcolor2,(X,Y,self.w,self.h),recwidth)
            elif(display[0]==False):
                if(display[1]==True):
                    screen.blit(image, (X,Y),coord[a[1]])
                elif(display[3]==True):
                    screen.blit(image, (X,Y),coord[a[3]])
                else:
                    screen.blit(image,(X,Y),coord[a[0]])
                pygame.draw.rect(screen,rectcolor,(X,Y,self.w,self.h),recwidth)
            if(display[1]==True):
                screen.blit(black, (X1,Y))   
                pygame.draw.rect(screen,rectcolor2,(X1,Y,self.w,self.h),recwidth)
            elif(display[1]==False):
                if(display[0]==True):
                    screen.blit(image, (X1,Y),coord[a[0]])
                elif(display[2]==True):
                    screen.blit(image, (X1,Y),coord[a[2]])
                elif(display[4]==True):
                    screen.blit(image, (X1,Y),coord[a[4]])
                else:
                    screen.blit(image, (X1,Y),coord[a[1]])
                pygame.draw.rect(screen,rectcolor,(X1,Y,self.w,self.h),recwidth)
            if(display[2]==True):
                screen.blit(black, (X2,Y))
                pygame.draw.rect(screen,rectcolor2,(X2,Y,self.w,self.h),recwidth)
            elif(display[2]==False):
                if(display[5]==True):
                    screen.blit(image, (X2,Y),coord[a[5]])
                elif(display[1]==True):
                    screen.blit(image, (X2,Y),coord[a[1]])
                else:
                    screen.blit(image, (X2,Y),coord[a[2]])
                pygame.draw.rect(screen,rectcolor,(X2,Y,self.w,self.h),recwidth)
            if(display[3]==True):
                screen.blit(black, (X,Y1))
                pygame.draw.rect(screen,rectcolor2,(X,Y1,self.w,self.h),recwidth)
            elif(display[3]==False):
                if(display[0]==True):
                    screen.blit(image, (X,Y1),coord[a[0]])
                elif(display[4]==True):
                    screen.blit(image, (X,Y1),coord[a[4]])
                elif(display[6]==True):
                    screen.blit(image, (X,Y1),coord[a[6]])
                else:
                    screen.blit(image, (X,Y1),coord[a[3]])
                pygame.draw.rect(screen,rectcolor,(X,Y1,self.w,self.h),recwidth)
            if(display[4]==True):
                screen.blit(black, (X1,Y1))
                pygame.draw.rect(screen,rectcolor2,(X1,Y1,self.w,self.h),recwidth)
            elif(display[4]==False):
                if(display[5]==True):
                    screen.blit(image, (X1,Y1),coord[a[5]])
                elif(display[7]==True):
                    screen.blit(image, (X1,Y1),coord[a[7]])
                elif(display[1]==True):
                    screen.blit(image, (X1,Y1),coord[a[1]])
                elif(display[3]==True):
                    screen.blit(image, (X1,Y1),coord[a[3]])
                else:
                    screen.blit(image, (X1,Y1),coord[a[4]])
                pygame.draw.rect(screen,rectcolor,(X1,Y1,self.w,self.h),recwidth)
            if(display[5]==True):
                screen.blit(black, (X2,Y1))
                pygame.draw.rect(screen,rectcolor2,(X2,Y1,self.w,self.h),recwidth)
            elif(display[5]==False):
                if(display[2]==True):
                    screen.blit(image, (X2,Y1),coord[a[2]])
                elif(display[4]==True):
                    screen.blit(image, (X2,Y1),coord[a[4]])
                elif(display[8]==True):
                    screen.blit(image, (X2,Y1),coord[a[5]])
                else:
                    screen.blit(image, (X2,Y1),coord[a[5]])
                pygame.draw.rect(screen,rectcolor,(X2,Y1,self.w,self.h),recwidth)
            if(display[6]==True):
                screen.blit(black, (X,Y2))
                pygame.draw.rect(screen,rectcolor2,(X,Y2,self.w,self.h),recwidth)
            elif(display[6]==False):
                if(display[7]==True):
                    screen.blit(image, (X,Y2),coord[a[7]])
                elif(display[3]==True):
                    screen.blit(image, (X,Y2),coord[a[3]])
                else:
                    screen.blit(image, (X,Y2),coord[a[6]])
                pygame.draw.rect(screen,rectcolor,(X,Y2,self.w,self.h),recwidth)
            if(display[7]==True):
                screen.blit(black, (X1,Y2))
                pygame.draw.rect(screen,rectcolor2,(X1,Y2,self.w,self.h),recwidth)
            elif(display[7]==False):
                if(display[8]==True):
                    screen.blit(image, (X1,Y2),coord[a[7]])
                elif(display[4]==True):
                    screen.blit(image, (X1,Y2),coord[a[4]])
                elif(display[6]==True):
                    screen.blit(image, (X1,Y2),coord[a[6]])
                else:
                    screen.blit(image, (X1,Y2),coord[a[7]])
                pygame.draw.rect(screen,rectcolor,(X1,Y2,self.w,self.h),recwidth)
            if(display[8]==True):
                screen.blit(black, (X2,Y2))
                pygame.draw.rect(screen,rectcolor2,(X2,Y2,self.w,self.h),recwidth)
            elif(display[8]==False):
                if(display[5]==True):
                    if(box[0]==True):
                        screen.blit(image, (X2,Y2),coord[a[0]])
                    elif(box[1]==True):
                        screen.blit(image, (X2,Y2),coord[a[1]])
                    elif(box[2]==True):
                        screen.blit(image, (X2,Y2),coord[a[2]])
                    elif(box[3]==True):
                        screen.blit(image, (X2,Y2),coord[a[3]])
                    elif(box[4]==True):
                        screen.blit(image, (X2,Y2),coord[a[4]])
                    elif(box[5]==True):
                        screen.blit(image, (X2,Y2),coord[a[5]])
                    elif(box[6]==True):
                        screen.blit(image, (X2,Y2),coord[a[6]])
                    elif(box[7]==True):
                        screen.blit(image, (X2,Y2),coord[a[7]])
                elif(display[7]==True):
                    screen.blit(image, (X2,Y2),coord[a[7]])
                pygame.draw.rect(screen,rectcolor,(X2,Y2,self.w,self.h),recwidth)

def redraw():
    pla.draw()
    bg.draw()
    pygame.display.update()
pla = player(180,50,120,120)
bg = Slidingi(180,50,360,360)
run=1
while run:
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            run=0
        if(start==True):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                saved_image = screen.copy()
                screen.blit(image, (180,50))
                screen.blit(black, (420,290))
                pygame.draw.rect(screen,(255,255,255),(180,50,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(300,50,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(420,50,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(180,170,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(300,170,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(420,170,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(180,290,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(300,290,120,120),2)
                pygame.draw.rect(screen,(255,255,255),(420,290,120,120),2)
                pygame.display.flip()
                pygame.time.delay(150)
                showing_solution = True
        elif showing_solution and (event.type == pygame.MOUSEBUTTONUP):
            screen.blit (saved_image, (180,50))
            screen.blit(black, (420,290))
            pygame.draw.rect(screen,(255,255,255),(180,50,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(300,50,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(420,50,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(180,170,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(300,170,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(420,170,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(180,290,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(300,290,120,120),2)
            pygame.draw.rect(screen,(255,255,255),(420,290,120,120),2)
            pygame.display.flip()
            showing_solution = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx,my=pygame.mouse.get_pos()
            for i in range(0, 1):
                    x, y = event.pos
            if(start):
                if((display[1]==True or display[3]==True) and display[0]==False):
                    if mx>180 and mx < 300:#0
                        if my>50 and my<170:
                            display[1]=False
                            display[3]=False
                            display[0]=True
                            click.append([x, y])
                if((display[0]==True or display[2]==True or display[4]==True) and display[1]==False):
                    if mx>300 and mx < 420:#1
                        if my>500 and my<1700:
                            display[0]=False
                            display[2]=False
                            display[4]=False
                            display[1]=True
                            click.append([x, y])
                if((display[1]==True or display[5]==True) and display[2]==False):
                    if mx>420 and mx < 540:#2
                        if my>50 and my<170:
                            display[1]=False
                            display[5]=False
                            display[2]=True
                            click.append([x, y])
                if((display[0]==True or display[3]==True) and (display[3]==False)):
                    if mx>180 and mx < 300:#3
                        if my>170 and my<290:
                            display[0]=False
                            display[3]=False
                            display[3]=True
                            click.append([x, y])
                if((display[1]==True or display[3]==True or display[5]==True or display[7]==True) and (display[4]==False)):
                    if mx>300 and mx < 420:#4
                        if my>170 and my<290:
                            display[1]=False
                            display[3]=False
                            display[7]=False
                            display[4]=True
                            click.append([x, y])
                if((display[2]==True or display[8]==True) and display[5]==False):
                    if mx>420 and mx < 540:#5
                        if my>170 and my<290:
                            display[2]=False
                            display[8]=False
                            display[5]=True
                            click.append([x, y])
                if((display[3]==True or display[7]==True) and display[6]==False):
                    if mx>180 and mx < 300:#6
                        if my>290 and my<410:
                            display[3]=False
                            display[7]=False
                            display[6]=True
                            click.append([x, y])
                if((display[6]==True or display[4]==True or display[8]==True) and display[7]==False):
                    if mx>300 and mx < 420:#7
                        if my>290 and my<410:
                            display[4]=False
                            display[6]=False
                            display[8]=False
                            display[7]=True
                            click.append([x, y])
                if((display[7]==True or display[5]==True) and display[8]==False):
                    if mx>420 and mx < 540:#8
                        if my>290 and my<410:
                            display[7]=False
                            display[5]=False
                            display[8]=True
                            click.append([x, y])
            if mx>180 and mx<560:
                if my>50 and my<410:
                    display[8]=True
                    start=True
            
        #if event.type == pygame.KEYDOWN:
         #   if event.key ==pygame.K_RETURN:
          #      display[8]=True
           #     start=True
           
                        
    redraw()
pygame.quit()
   
    
