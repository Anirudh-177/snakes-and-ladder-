import pygame
import random
import time
pygame.init()
display_screen = pygame.display.set_mode((650,500))
pygame.display.set_caption("Snakes And Ladders")
logo=pygame.image.load("gameintro.jpg")
pygame.display.set_icon(logo)
board= pygame.image.load("Game_Board.jpg")
background = pygame.image.load("background.webp")
clickimg = pygame.image.load("click.jpg")
bx = 150
by = 5
blueplayer = pygame.image.load("blueimage.jpg")
redplayer = pygame.image.load("redplayer.png")
rx = 100
ry = 251
blx = 100
bly = 362
button = pygame.Rect(10,50,40,40)
score_font = pygame.font.SysFont("comicsansms", 35)
font1=pygame.font.SysFont("comicsansms",25)
font2=pygame.font.SysFont("comicsansms",20)
clock = pygame.time.Clock()
def pickNumber():
    diceroll = random.randint(1,6)
    if diceroll == 1:
        dice = pygame.image.load("dice1.jpg")
    elif diceroll == 2:
        dice = pygame.image.load("dice2.png")
    elif diceroll == 3:
        dice = pygame.image.load("dice3.png")
    elif diceroll == 4:
        dice = pygame.image.load("dice4.png")
    elif diceroll == 5:
        dice = pygame.image.load("dice5.png")
    elif diceroll == 6:
        dice = pygame.image.load("dice6.png")
    return(dice,diceroll)
def players():
    msg1=font1.render("Player 1", True,(255,0,0))
    display_screen.blit(msg1,[5,251])
    msg2=font1.render("Player 2", True,(0,0,255))
    display_screen.blit(msg2,[5,362])
def redTurn():
    msg3 = font2.render("Your Turn",True,(255,255,255))
    display_screen.blit(msg3,[25,290])
def blueTurn():
    msg3 = font2.render("Your Turn",True,(255,255,255))
    display_screen.blit(msg3,[ 25,400])
def screen():
    display_screen.blit(background,(0,0))
    display_screen.blit(board,(bx,by))
    display_screen.blit(clickimg,(10,50))
def redPlayer(x,y):
    display_screen.blit(redplayer, (x,y))
def bluePlayer(x,y):
    display_screen.blit(blueplayer, (x,y))
running = True
turn = 'red'
    while running:
        display_screen.fill((0,255,195))
        screen()
        players()
        if turn=='red':
            redTurn()
        else:
            blueTurn()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.collidepoint(mouse_pos):
                    pickNumber()
                    dice,diceroll = pickNumber()
                    display_screen.blit(dice,(50,60))
                    print(diceroll)
                #FOR PLAYER 1
                if pickNumber() and turn == 'red':
                turn = 'blue'
                if diceroll == 6 and rx < 162 and ry == 251:
                    rx = rx + 62
                    ry = 447
                    turn = 'red'
                elif rx >= 162 and rx < 358 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55) and diceroll != 6:
                    rx = rx+(49*diceroll)
                    if rx == 309 and ry == 447:
                        rx = 358
                        ry = 349
                    elif rx == 456 and ry == 349:
                        rx = 358
                        ry = 447
                    elif rx == 211 and ry == 251:
                        rx = 260
                        ry = 153
                    elif rx == 211 and ry == 153:
                        rx = 162
                        ry = 55
                    elif rx == 260 and ry == 251:
                        rx = 260
                        ry = 398
                    elif rx == 603 and ry == 251:
                        rx = 554
                        ry = 153
                    elif rx == 407 and ry == 153:
                        rx = 358
                        ry = 251
                    elif rx == 554 and ry == 55:
                        rx = 505
                        ry = 202
                elif rx >= 162 and rx < 358 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55) and diceroll == 6:
                    rx = rx+(49*diceroll)
                    if rx == 309 and ry == 447:
                        rx = 358
                        ry = 349
                    elif rx == 456 and ry == 349:
                        rx = 358
                        ry = 447
                    elif rx == 211 and ry == 251:
                        rx = 260
                        ry = 153
                    elif rx == 211 and ry == 153:
                        rx = 162
                        ry = 55
                    elif rx == 260 and ry == 251:
                        rx = 260
                        ry = 398
                    elif rx == 603 and ry == 251:
                        rx = 554
                        ry = 153
                    elif rx == 407 and ry == 153:
                        rx = 358
                        ry = 251
                    elif rx == 554 and ry == 55:
                        rx = 505
                        ry = 202
                    turn = 'red'
                elif rx >= 358 and rx < 407 and diceroll != 6 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*diceroll)
                    if rx == 456 and ry == 349:
                        rx = 358
                        ry = 447
                    elif rx == 603 and ry == 251:
                        rx = 554
                        ry = 153
                    elif rx == 407 and ry == 153:
                        rx = 358
                        ry = 251
                    elif rx == 554 and ry == 55 and diceroll == 4:
                        rx = 505
                        ry = 202
                elif rx >= 358 and rx < 407 and diceroll == 6 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*5)-(49*(diceroll-6))
                    ry = ry-49
                    turn = 'red'
                elif rx >= 407 and rx < 456 and diceroll <= 4 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*diceroll)
                    if rx == 456 and ry == 349:
                        rx = 358
                        ry = 447
                    elif rx == 603 and ry == 251:
                        rx = 554
                        ry = 153
                    elif rx == 554 and ry == 55 and diceroll == 3:
                        rx = 505
                        ry = 202
                elif rx >= 407 and rx < 456 and diceroll > 4 and diceroll != 6 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*4)-(49*(diceroll-5))
                    ry = ry-49
                elif rx >= 407 and rx < 456 and diceroll == 6 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*4)-(49*(diceroll-5))
                    ry = ry-49
                    turn = 'red'
                elif rx >= 456 and rx < 505 and diceroll <= 3 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*diceroll)
                    if rx == 603 and ry == 251:
                        rx = 554
                        ry = 153
                    elif rx == 554 and ry == 55 and diceroll == 2:
                        rx = 505
                        ry = 202
                elif rx >= 456 and rx < 505 and diceroll > 3 and diceroll != 6 and (ry == 447 or ry == 349 or ry == 251 or ry == 153 or ry == 55):
                    rx = rx+(49*3)-(49*(diceroll-4))
                    ry = ry-49
                    if rx == 505 and ry == 398:
                        rx = 407
                        ry = 251
                    elif rx == 505 and ry == 300:
                        rx=554
                        ry=251
                elif rx >= 456 and rx < 505 and diceroll == 6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*3)-(49*(diceroll-4))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                        turn = 'red'
                elif rx>=505 and rx<554 and diceroll<=2 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) : 
                    rx=rx+(49*diceroll)
                    if rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==554 and ry==55 and diceroll==1:
                        rx=505
                        ry=202
                elif rx>=505 and rx<554 and diceroll>2 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) :
                    rx=rx+(49*2)-(49*(diceroll-3))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                elif rx>=505 and rx<554 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) :
                    rx=rx+(49*2)-(49*(diceroll-3))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    turn='red'
                elif rx>=554 and rx<603 and diceroll==1 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) : #10
                    rx=rx+(49*diceroll)
                    if rx==603 and ry==251:
                        rx=554
                        ry=153
                elif rx>=554 and rx<603 and diceroll>1 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) :
                    rx=rx+(49*1)-(49*(diceroll-2))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                elif rx>=554 and rx<603 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) :
                    rx=rx+(49*1)-(49*(diceroll-2))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    turn='red'
                elif rx>=603 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) and diceroll!=6:
                    rx=rx-(49*(diceroll-1))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251  
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    elif rx==358 and ry==104:
                        rx=260
                        ry=202
                elif rx>=603 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55) and diceroll==6:
                    rx=rx-(49*(diceroll-1))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    elif rx ==358 and ry == 104:
                        rx = 260
                        ry = 202
                    turn='red'
                elif rx>358 and rx<=603 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6) and diceroll !=6:
                    rx=rx-(49*diceroll)
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    elif rx==162 and ry==300:
                        rx=260
                        ry=447
                    elif rx==358 and ry==104:
                        rx=260
                        ry=202
                elif rx>407 and rx<=603 and diceroll != 6 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6):
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6:
                        rx=162
                        ry=251
                    elif rx==162 and ry==300:
                        rx=260
                        ry=447
                    elif rx==211 and ry==6:
                        rx=162
                        ry=251
                elif rx>407 and rx<=603 and diceroll==6 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6) :
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6:
                        rx=162
                        ry=251
                    elif rx==162 and ry==300:
                        rx=260
                        ry=447
                    elif rx==211 and ry==6:
                        rx=162
                        ry=251
                    turn='red'
                elif rx==407 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll!=6 :
                    rx=rx-(49*diceroll)
                    if rx==358 and ry==104:
                        rx=260
                        ry=202
                    elif rx==211 and ry==6:
                        rx=162
                        ry=251
                elif rx==407 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll==6: #8
                    rx=rx-(49*5)
                    ry=ry-49
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                    turn='red'
                elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll<5 :
                    rx=rx-(49*diceroll)    
                    if rx==162 and ry==300:
                        rx=260
                        ry=477
                elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==5 :
                    rx=rx-(49*4)+(49*(diceroll-5))  
                    ry=ry-49  
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    turn='red'
                elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll<4 :
                    rx=rx-(49*(diceroll))  
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll>=4 and diceroll!=6 :
                    rx=rx-(49*3)+(49*(diceroll-4))  
                    ry=ry-49  
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6 :
                    rx=rx-(49*3)+(49*(diceroll-4))  
                    ry=ry-49  
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    turn='red'
                elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll<3:
                    rx=rx-(49*diceroll)
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll!=6 and diceroll>=3:
                    rx=rx-(49*2)+(49*(diceroll-3))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6 :
                    rx=rx-(49*2)+(49*(diceroll-3))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    turn='red'
                elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll<2:
                    rx=rx-(49*diceroll)
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll!=6 and diceroll>=2:
                    rx=rx-49+(49*(diceroll-2))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6 :
                    rx=rx-49+(49*(diceroll-2))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    turn='red'
                elif rx==162 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll!=6 :
                    rx=rx+(49*(diceroll-1))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                elif rx==162 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6 :
                    rx=rx+(49*(diceroll-1))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                    turn='red'
                elif ry==6 and (rx==554 or rx==603) and diceroll!=6:
                    rx=rx-(49*diceroll)
                elif ry==6 and (rx==554 or rx==603) and diceroll==6:
                    rx=rx-(49*diceroll)
                    turn='red'
                elif ry==6 and rx==456 and diceroll<5:
                    rx=rx-(49*diceroll)
                elif ry==6 and rx==456 and diceroll==5:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==5:
                        rx=162
                        ry=251
                elif ry==6 and rx==456 and diceroll==6:
                    rx=rx
                elif ry==6 and rx==505 and diceroll!=6:
                    rx=rx-(49*diceroll)
                elif ry==6 and  rx==505 and diceroll==6:
                    rx=rx-(49*diceroll)
                    if rx==211  and ry==6 and diceroll==6:
                        rx=162
                        ry=251
                elif ry==6 and rx==407 and diceroll<6:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==4:
                        rx=162
                        ry=251
                elif ry==6 and rx==407 and rx>=162 and diceroll==6:
                    rx=rx
                elif ry==6 and rx==358 and rx>=162 and diceroll>=5:
                    rx=rx
                elif ry==6 and rx==358 and rx>=162 and diceroll<5:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==3:
                        rx=162
                        ry=251
                elif ry==6 and rx==309 and rx>=162 and diceroll>=4:
                    rx=rx
                elif ry==6 and rx==309 and rx>=162 and diceroll<4:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==2:
                        rx=162
                        ry=251
                elif ry==6 and rx==260 and rx>=162 and diceroll>=3:
                    rx=rx
                elif ry==6 and rx==260 and rx>=162 and diceroll<3:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==1:
                        rx=162
                        ry=251
                elif ry==6 and rx==211 and rx>162 and diceroll>=2:
                    rx=rx
                # FOR PLAYER 2
                elif pickNumber() and turn == 'blue':
                turn = 'red'
                if diceroll == 6 and blx < 162 and bly == 362:
                    blx = blx + 62
                    bly = 447
                    turn = 'blue'
                elif blx >= 162 and blx < 358 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55) and diceroll != 6:
                    blx = blx+(49*diceroll)
                    if blx == 309 and bly == 447:
                        blx = 358
                        bly = 349
                    elif blx == 456 and bly == 349:
                        blx = 358
                        bly = 447
                    elif blx == 211 and bly == 251:
                        blx = 260
                        bly = 153
                    elif blx == 211 and bly == 153:
                        blx = 162
                        bly = 55
                    elif blx == 260 and bly == 251:
                        blx = 260
                        bly = 398
                    elif blx == 603 and bly == 251:
                        blx = 554
                        bly = 153
                    elif blx == 407 and bly == 153:
                        blx = 358
                        bly = 251
                    elif blx == 554 and bly == 55:
                        blx = 505
                        bly = 202

                elif blx >= 162 and blx < 358 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55) and diceroll == 6:
                    blx = blx+(49*diceroll)
                    if blx == 309 and bly == 447:
                        blx = 358
                        bly = 349
                    elif blx == 456 and bly == 349:
                        blx = 358
                        bly = 447
                    elif blx == 211 and bly == 251:
                        blx = 260
                        bly = 153
                    elif blx == 211 and bly == 153:
                        blx = 162
                        bly = 55
                    elif blx == 260 and bly == 251:
                        blx = 260
                        bly = 398
                    elif blx == 603 and bly == 251:
                        blx = 554
                        bly = 153
                    elif blx == 407 and bly == 153:
                        blx = 358
                        bly = 251
                    elif blx == 554 and bly == 55:
                        blx = 505
                        bly = 202
                    turn = 'blue'
                elif blx >= 358 and blx < 407 and diceroll != 6 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*diceroll)
                    if blx == 456 and bly == 349:
                        blx = 358
                        bly = 447
                    elif blx == 603 and bly == 251:
                        blx = 554
                        bly = 153
                    elif blx == 407 and bly == 153:
                        blx = 358
                        bly = 251
                    elif blx == 554 and bly == 55 and diceroll == 4:
                        blx = 505
                        bly = 202
                elif blx >= 358 and blx < 407 and diceroll == 6 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*5)-(49*(diceroll-6))
                    bly = bly-49
                    turn = 'blue'
                elif blx >= 407 and blx < 456 and diceroll <= 4 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*diceroll)
                    if blx == 456 and bly == 349:
                        blx = 358
                        bly = 447
                    elif blx == 603 and bly == 251:
                        blx = 554
                        bly = 153
                    elif blx == 554 and bly == 55 and diceroll == 3:
                        blx = 505
                        bly = 202
                elif blx >= 407 and blx < 456 and diceroll > 4 and diceroll != 6 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*4)-(49*(diceroll-5))
                    bly = bly-49
                elif blx >= 407 and blx < 456 and diceroll == 6 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*4)-(49*(diceroll-5))
                    bly = bly-49
                    turn = 'blue'

                elif blx >= 456 and blx < 505 and diceroll <= 3 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*diceroll)
                    if blx == 603 and bly == 251:
                        blx = 554
                        bly = 153
                    elif blx == 554 and bly == 55 and diceroll == 2:
                        blx = 505
                        bly = 202
                elif blx >= 456 and blx < 505 and diceroll > 3 and diceroll != 6 and (bly == 447 or bly == 349 or bly == 251 or bly == 153 or bly == 55):
                    blx = blx+(49*3)-(49*(diceroll-4))
                    bly = bly-49
                    if blx == 505 and bly == 398:
                        blx = 407
                        bly = 251
                    elif blx == 505 and bly == 300:
                        blx=554
                        bly=251
                elif blx >= 456 and blx < 505 and diceroll == 6 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55):
                    blx=blx+(49*3)-(49*(diceroll-4))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                        turn = 'blue'
                elif blx>=505 and blx<554 and diceroll<=2 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) : 
                    blx=blx+(49*diceroll)
                    if blx==603 and bly==251:
                        blx=554
                        bly=153
                    elif blx==554 and bly==55 and diceroll==1:
                        blx=505
                        bly=202
                elif blx>=505 and blx<554 and diceroll>2 and diceroll!=6 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) :
                    blx=blx+(49*2)-(49*(diceroll-3))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                elif blx>=505 and blx<554 and diceroll==6 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) :
                    blx=blx+(49*2)-(49*(diceroll-3))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                    turn='blue'
                elif blx>=554 and blx<603 and diceroll==1 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) : #10
                    blx=blx+(49*diceroll)
                    if blx==603 and bly==251:
                        blx=554
                        bly=153
                elif blx>=554 and blx<603 and diceroll>1 and diceroll!=6 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) :
                    blx=blx+(49*1)-(49*(diceroll-2))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                elif blx>=554 and blx<603 and diceroll==6 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) :
                    blx=blx+(49*1)-(49*(diceroll-2))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                    turn='blue'
                elif blx>=603 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) and diceroll!=6:
                    blx=blx-(49*(diceroll-1))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251  
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                    elif blx==358 and bly==104:
                        blx=260
                        bly=202
                elif blx>=603 and (bly==447 or bly==349 or bly==251 or bly==153 or bly==55) and diceroll==6:
                    blx=blx-(49*(diceroll-1))
                    bly=bly-49
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                    elif blx ==358 and bly == 104:
                        blx = 260
                        bly = 202
                    turn='blue'
                elif blx>358 and blx<=603 and (bly==398 or bly==300 or bly==202 or bly==104 or bly==6) and diceroll !=6:
                    blx=blx-(49*diceroll)
                    if blx==505 and bly==398:
                        blx=407
                        bly=251
                    elif blx==505 and bly==300:
                        blx=554
                        bly=251
                    elif blx==456 and bly==202:
                        blx=603
                        bly=300
                    elif blx==456 and bly==104:
                        blx=554
                        bly=6
                    elif blx==162 and bly==300:
                        blx=260
                        bly=447
                    elif blx==358 and bly==104:
                        blx=260
                        bly=202
                elif blx>407 and blx<=603 and diceroll != 6 and (bly==398 or bly==300 or bly==202 or bly==104 or bly==6):
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6:
                        blx=162
                        bly=251
                    elif blx==162 and bly==300:
                        blx=260
                        bly=447
                    elif blx==211 and bly==6:
                        blx=162
                        bly=251
                elif blx>407 and blx<=603 and diceroll==6 and (bly==398 or bly==300 or bly==202 or bly==104 or bly==6) :
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6:
                        blx=162
                        bly=251
                    elif blx==162 and bly==300:
                        blx=260
                        bly=447
                    elif blx==211 and bly==6:
                        blx=162
                        bly=251
                    turn='blue'
                elif blx==407 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll!=6 :
                    blx=blx-(49*diceroll)
                    if blx==358 and bly==104:
                        blx=260
                        bly=202
                    elif blx==211 and bly==6:
                        blx=162
                        bly=251
                elif blx==407 and (bly==398 or bly==300 or bly==202 or bly==104 ) and diceroll==6: #8
                    blx=blx-(49*5)
                    bly=bly-49
                    if blx==162 and bly==300:
                        blx=260
                        bly=447
                    turn='blue'
                elif blx==358 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll<5 :
                    blx=blx-(49*diceroll)    
                    if blx==162 and bly==300:
                        blx=260
                        bly=477
                elif blx==358 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll==5 :
                    blx=blx-(49*4)+(49*(diceroll-5))  
                    bly=bly-49  
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    turn='blue'
                elif blx==309 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll<4 :
                    blx=blx-(49*(diceroll))  
                    if blx==162 and bly==300:
                        blx=260
                        bly=447
                elif blx==309 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll>=4 and diceroll!=6 :
                    blx=blx-(49*3)+(49*(diceroll-4))  
                    bly=bly-49  
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                elif blx==309 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll==6 :
                    blx=blx-(49*3)+(49*(diceroll-4))  
                    bly=bly-49  
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                    turn='blue'
                elif blx==260 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll<3:
                    blx=blx-(49*diceroll)
                    if blx==162 and bly==300:
                        blx=260
                        bly=447
                elif blx==260 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll!=6 and diceroll>=3:
                    blx=blx-(49*2)+(49*(diceroll-3))
                    bly=bly-49
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                elif blx==260 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll==6 :
                    blx=blx-(49*2)+(49*(diceroll-3))
                    bly=bly-49
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                    turn='blue'
                elif blx==211 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll<2:
                    blx=blx-(49*diceroll)
                    if blx==162 and bly==300:
                        blx=260
                        bly=447
                elif blx==211 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll!=6 and diceroll>=2:
                    blx=blx-49+(49*(diceroll-2))
                    bly=bly-49
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                elif blx==211 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll==6 :
                    blx=blx-49+(49*(diceroll-2))
                    bly=bly-49
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                    turn='blue'
                elif blx==162 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll!=6 :
                    blx=blx+(49*(diceroll-1))
                    bly=bly-49
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                    elif blx==407 and bly==153:
                        blx=358
                        bly=251
                elif blx==162 and (bly==398 or bly==300 or bly==202 or bly==104) and diceroll==6 :
                    blx=blx+(49*(diceroll-1))
                    bly=bly-49
                    if blx==211 and bly==251:
                        blx=260
                        bly=153
                    elif blx==211 and bly==153:
                        blx=162
                        bly=55
                    elif blx==260 and bly==251:
                        blx=260
                        bly=398
                    elif blx==407 and bly==153:
                        blx=358
                        bly=251
                    turn='blue'
                elif bly==9 and (blx==554 or blx==603) and diceroll!=6:
                    blx=blx-(49*diceroll)
                elif bly==9 and (blx==554 or blx==603) and diceroll==6:
                    blx=blx-(49*diceroll)
                    turn='blue'
                elif bly==9 and blx==456 and diceroll<5:
                    blx=blx-(49*diceroll)
                elif bly==9 and blx==456 and diceroll==5:
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6 and diceroll==5:
                        blx=162
                        bly=254
                elif bly==9 and blx==456 and diceroll==6:
                    blx=blx
                elif bly==9 and blx==505 and diceroll!=6:
                    blx=blx-(49*diceroll)
                elif bly==9 and  blx==505 and diceroll==6:
                    blx=blx-(49*diceroll)
                    if blx==211  and bly==6 and diceroll==6:
                        blx=162
                        bly=254
                elif bly==6 and blx==407 and diceroll<6:
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6 and diceroll==4:
                        blx=162
                        bly=251
                elif bly==6 and blx==407 and blx>=162 and diceroll==6:
                    blx=blx
                elif bly==6 and blx==358 and blx>=162 and diceroll>=5:
                    blx=blx
                elif bly==6 and blx==358 and blx>=162 and diceroll<5:
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6 and diceroll==3:
                        blx=162
                        bly=251
                elif bly==6 and blx==309 and blx>=162 and diceroll>=4:
                    blx=blx
                elif bly==6 and blx==309 and blx>=162 and diceroll<4:
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6 and diceroll==2:
                        blx=162
                        bly=251
                elif bly==6 and blx==260 and blx>=162 and diceroll>=3:
                    blx=blx
                elif bly==6 and blx==260 and blx>=162 and diceroll<3:
                    blx=blx-(49*diceroll)
                    if blx==211 and bly==6 and diceroll==1:
                        blx=162
                        bly=251
                elif bly==6 and blx==211 and blx>162 and diceroll>=2:
                    blx=blx        
        redPlayer(rx,ry)
        bluePlayer(blx,bly)
        pygame.display.update()
        if rx ==162 and ry ==6:
            display_screen.fill((150,153,213))
            value = score_font.render("Red won",True,(255,255,102))
            display_screen.blit(value,[5,104])
            running = False
        if blx ==162 and bly ==6:
            display_screen.fill((50,153,213))
            value = score_font.render("Blue won",True,(255,255,102))
            display_screen.blit(value,[5,104])
            running = False
        time.sleep(5)
pygame.display.update()
clock.tick(40)
pygame.quit()
quit()

