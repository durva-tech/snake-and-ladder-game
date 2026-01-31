import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((830, 695))
pygame.display.set_caption("Snake And Ladder")

# background
bckimg = pygame.image.load("SandL.jpg")
arrow = pygame.image.load("arrow.png")

bx = 150
by = 5

# players
rl = pygame.image.load("locred.png")
bl = pygame.image.load("locblue.png")

rx = 100
ry = 292

blx = 96
bly = 410

button = pygame.Rect(1, 90, 40, 40)

font1 = pygame.font.SysFont("comicsansms", 25)
font2 = pygame.font.SysFont("comicsansms", 20)

def bck():
    screen.blit(bckimg, (bx, by))
    screen.blit(arrow, (0, 90))

def rplayer(x, y):
    screen.blit(rl, (x, y))

def bplayer(x, y):
    screen.blit(bl, (x, y))

def pickNumber():
    diceroll = random.randint(1, 6)
    if diceroll == 1:
        dice = pygame.image.load("one.png")
    elif diceroll == 2:
        dice = pygame.image.load("two.png")
    elif diceroll == 3:
        dice = pygame.image.load("three.png")
    elif diceroll == 4:
        dice = pygame.image.load("four.png")
    elif diceroll == 5:
        dice = pygame.image.load("five.png")
    elif diceroll == 6:
        dice = pygame.image.load("six.png")
    screen.blit(dice, (50, 150))
    pygame.display.update()
    time.sleep(1)
    return diceroll

def players():
    mag1 = font1.render("Player 1", True, (0,0,0))
    screen.blit(mag1, (5,300))
    mag1 = font1.render("Player 2", True, (0,0,0))
    screen.blit(mag1, (5,420))

def rollr():
    mag3 = font2.render("Your Turn", True, (0,0,0))
    screen.blit(mag3, (25,350))

def rollb():
    mag4 = font2.render("Your Turn", True, (0,0,0))
    screen.blit(mag4, (25,470))

# game loop
running = True
turn = 'red'
while running:
    screen.fill((0,255,195))
    bck()
    players()
    if turn == 'red':
        rollr()
    else:
        rollb()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice,diceroll=pickNumber()
                screen.blit(dice,(60,80))
                print(diceroll)

                #for player 1

                #1st row
                if pickNumber() and turn=='red':
                    turn='blue'
                    if diceroll==6 and rx==100 and ry==292:
                        rx=175
                        ry=605
                        turn='red'
                    elif rx in range(175,560) and diceroll!=6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*diceroll)
                        turn='red'
                    elif rx in range(175,560) and diceroll!=6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*diceroll)
                        turn='red'

                    elif rx==560 and diceroll==6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*diceroll)
                    elif rx==560 and diceroll==6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*4)
                        ry=ry-55
                        turn='red'
                    elif rx==560 and diceroll==4 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165): #7
                        rx=rx+(55*diceroll)
                    elif rx==560 and diceroll==4 and diceroll!=6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*4)-(55*(diceroll-5))
                        ry=ry-55
                        turn='red'
                    elif rx==615 and diceroll==3 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165): #8
                        rx=rx+(55*diceroll)
                    elif rx==615 and diceroll==3 and diceroll!=6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*3)
                        ry=ry-55
                        turn='red'
                    elif rx==615 and diceroll==6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*3)-(55*(diceroll-4))
                        ry=ry-55
                        turn='red'
                    elif rx==680 and diceroll==2 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165): #9
                        rx=rx+(55*diceroll)
                    elif rx==680 and diceroll==2 and diceroll!=6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*2)
                        ry=ry-55
                        turn='red'
                    elif rx==615 and diceroll==6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*2)-(55*(diceroll-3))
                        ry=ry-55
                        turn='red'
                    elif rx==730 and diceroll==1 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165): #10
                        rx=rx+(55*diceroll)
                    elif rx==730 and diceroll==1 and diceroll!=6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*1)
                        ry=ry-55
                        turn='red'
                    elif rx==730 and diceroll==6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx+(55*1)-(55*(diceroll-2))
                        ry=ry-55
                        turn='red'
                    elif rx==780 and diceroll==1 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx-(55*(diceroll-1))
                    elif rx==780 and diceroll==6 and (ry==605 or ry==495 or ry==385 or ry==275 or ry==165):
                        rx=rx-(55*4)
                        ry=ry-55
                        turn='red'

    #row 2

                    elif rx>560 and rx<780 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll!=6:
                        rx=rx-(55*diceroll)
                    elif rx>560 and rx<780 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-(55*5)
                        ry=ry-55
                    elif rx==615 and rx<780 and diceroll==6 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160):
                        rx=rx-(55*diceroll)
                    elif rx==615 and rx<780 and diceroll==6 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160):
                        rx=rx-(55*diceroll)
                        turn='red'
                    elif rx==615 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-(55*diceroll)
                    elif rx==615 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-(55*5)
                        ry=ry-55
                        turn='red'
                    elif rx==560 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll<5:
                        rx=rx-(55*diceroll)
                    elif rx==560 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==5:
                        rx=rx-(55*4)+(55*(diceroll-5))
                        ry=ry-55
                    elif rx==560 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-(55*4)+(55*(diceroll-4))
                        ry=ry-55
                        turn='red'

                    elif rx==505 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll<4:
                        rx=rx-(55*diceroll)
                    elif rx==505 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll>=4 and diceroll!=6:
                        rx=rx-(55*3)+(55*(diceroll-4))
                        ry=ry-55
                    elif rx==505 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-(55*3)+(55*(diceroll-4))
                        ry=ry-55
                        turn='red'

                    elif rx==450 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll<3:
                        rx=rx-(55*diceroll)
                    elif rx==450 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll>=3 and diceroll!=6:
                        rx=rx-(55*2)+(55*(diceroll-3))
                        ry=ry-55
                    elif rx==450 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-(55*2)+(55*(diceroll-3))
                        ry=ry-55
                        turn='red'

                    elif rx==395 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll<2:
                        rx=rx-(55*diceroll)
                    elif rx==395 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll!=6 and diceroll>=2:
                        rx=rx-55+(55*(diceroll-2))
                        ry=ry-55
                    elif rx==395 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx-55+(55*(diceroll-2))
                        ry=ry-55
                        turn='red'
                    elif rx==340 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll!=6:
                        rx=rx+(55*diceroll-1)
                        ry=ry-55
                    elif rx==340 and (ry==600 or ry==490 or ry==380 or ry==270 or ry==160) and diceroll==6:
                        rx=rx+(55*(diceroll-1))
                        ry=ry-55
                        turn='red'

#for player 2
                    elif pickNumber() and turn=='blue':
                        turn='red'
    if diceroll==6 and blx==96 and bly==410:
        blx=185
        bly=605
        turn='blue'
    elif blx in range(185,605) and diceroll!=6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*diceroll)
    elif blx in range(185,560) and diceroll==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*diceroll)
        turn='blue'

    elif blx==560 and diceroll!=6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*diceroll)
        bly=bly-55
    elif blx==560 and diceroll==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*5)
        bly=bly-55
        turn='blue'

    elif blx==560 and diceroll!=4 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165): #7
        blx=blx+(55*diceroll)
        bly=bly-55
    elif blx==560 and diceroll==4 and diceroll!=6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*4)
        bly=bly-55
    elif blx==560 and diceroll==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*4)-(55*(diceroll-5))
        bly=bly-55
        turn='blue'

    elif blx==615 and diceroll1==3 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165): #8
        blx=blx+(55*diceroll1)
    elif blx==615 and diceroll1==3 and diceroll1!=6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*3)
        bly=bly-55
        turn='blue'
    elif blx==615 and diceroll1==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*3)-(55*(diceroll1-4))
        bly=bly-55
        turn='blue'

    elif blx==680 and diceroll1<=2 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165): #9
        blx=blx+(55*diceroll1)
    elif blx==680 and diceroll1==2 and diceroll1!=6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*2)
        bly=bly-55
        turn='blue'
    elif blx==680 and diceroll1==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*2)-(55*(diceroll1-3))
        bly=bly-55
        turn='blue'

    elif blx==730 and diceroll1==1 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165): #10
        blx=blx+(55*diceroll1)
    elif blx==730 and diceroll1==1 and diceroll1!=6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*1)
        bly=bly-55
        turn='blue'
    elif blx==730 and diceroll1==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx+(55*1)-(55*(diceroll1-2))
        bly=bly-55
        turn='blue'

    elif blx==780 and diceroll1==6 and (bly==605 or bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx-(55*(diceroll1-1))
        bly=bly-55
        turn='blue'

    elif blx==780 and diceroll==6 and (bly==495 or bly==385 or bly==275 or bly==165):
        blx=blx-(55*(diceroll-1))
        bly=bly-55
        turn='blue'

#row 2

    elif blx==560 and blx==780 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*diceroll)
    elif blx==560 and blx==780 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*5)
        bly=bly-55

    elif blx==615 and blx==780 and diceroll==6 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160):
        blx=blx-(55*diceroll)
    elif blx==615 and blx==780 and diceroll==6 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160):
        blx=blx-(55*(diceroll-1))
        bly=bly-55
        turn='blue'

    elif blx==615 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*diceroll)
    elif blx==615 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*5)
        bly=bly-55
        turn='blue'

    elif blx==560 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll<5:
        blx=blx-(55*diceroll)
    elif blx==560 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==5:
        blx=blx-(55*4)+(55*(diceroll-5))
        bly=bly-55
        turn='blue'

    elif blx==560 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*4)+(55*(diceroll-5))
        bly=bly-55
        turn='blue'

    elif blx==505 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll<4:
        blx=blx-(55*diceroll)
        bly=bly-55
    elif blx==560 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==4 and diceroll!=6:
        blx=blx-(55*3)+(55*(diceroll-4))
        bly=bly-55
    elif blx==560 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*3)+(55*(diceroll-4))
        bly=bly-55
        turn='blue'

    elif blx==505 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll<4:
        blx=blx-(55*diceroll)
        bly=bly-55
    elif blx==505 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==4 and diceroll!=6:
        blx=blx-(55*3)+(55*(diceroll-4))
        bly=bly-55
    elif blx==505 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*3)+(55*(diceroll-4))
        bly=bly-55
        turn='blue'

    elif blx==430 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll<3:
        blx=blx-(55*diceroll)
        bly=bly-55
    elif blx==430 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==3 and diceroll!=6:
        blx=blx-(55*2)+(55*(diceroll-3))
        bly=bly-55
    elif blx==430 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx-(55*2)+(55*(diceroll-3))
        bly=bly-55
        turn='blue'


    elif blx==395 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll<2:
        blx=blx-(55*diceroll)
        bly=bly-55
    elif blx==395 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6 and diceroll>=2:
        blx=blx+55+(55*(diceroll-2))
        bly=bly-55
    elif blx==395 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx+55+(55*(diceroll-2))
        bly=bly-55
        turn='blue'

    elif blx==340 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx+(55*(diceroll-1))
        bly=bly-55
    elif blx==340 and (bly==600 or bly==490 or bly==380 or bly==270 or bly==160) and diceroll==6:
        blx=blx+(55*(diceroll-1))
        bly=bly-55
        turn='blue'


rplayer(rx,ry)
bpplayer(blx,bly)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
