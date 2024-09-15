import pygame


test=[
[1,2,3,4,5,6,7,8,9],
[2,3,4,5,6,7,8,9,1],
[3,4,5,6,7,8,9,1,2],
[4,5,6,7,8,9,1,2,3],
[5,6,7,8,0,1,2,3,4],
[6,7,8,9,1,2,3,4,5],
[7,8,9,1,2,3,4,5,6],
[8,9,1,2,3,4,5,6,7],
[9,1,2,3,4,5,6,7,8]
]

size = width, height = 450, 600

pygame.init()
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
running = True

myfont = pygame.font.SysFont("monospace", 15)

clickcell= False
pos = (0,0)

while running:

    screen.fill("white")

    pygame.draw.rect(screen,"black", (145,0,10,450))
    pygame.draw.rect(screen,"black", (295,0,10,450))
    pygame.draw.rect(screen,"black", (0,145,450,10))
    pygame.draw.rect(screen,"black", (0,295,450,10))
    pygame.draw.rect(screen,"black", (0,445,450,10))
    pygame.draw.rect(screen,"black", (48,0,4,450))
    pygame.draw.rect(screen,"black", (98,0,4,450))
    pygame.draw.rect(screen,"black", (198,0,4,450))
    pygame.draw.rect(screen,"black", (248,0,4,450))
    pygame.draw.rect(screen,"black", (348,0,4,450))
    pygame.draw.rect(screen,"black", (398,0,4,450))
    pygame.draw.rect(screen,"black", (0,48,450,4))
    pygame.draw.rect(screen,"black", (0,98,450,4))
    pygame.draw.rect(screen,"black", (0,198,450,4))
    pygame.draw.rect(screen,"black", (0,248,450,4))
    pygame.draw.rect(screen,"black", (0,348,450,4))
    pygame.draw.rect(screen,"black", (0,398,450,4))

    if clickcell:
        pygame.draw.rect(screen,"blue", ((x*50)+2,(y*50)+2,46,46))


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            x=pos[0]//50
            y= pos[1]//50
            
            if x <9 and y <9:
                clickcell =True
            else:
                clickcell=False

        if event.type==pygame.KEYDOWN:
            if clickcell == True:
                if event.key==pygame.K_0:
                    test[x][y]=0
                if event.key==pygame.K_1:
                    test[x][y]=1
                if event.key==pygame.K_2:
                    test[x][y]=2
                if event.key==pygame.K_3:
                    test[x][y]=3
                if event.key==pygame.K_4:
                    test[x][y]=4
                if event.key==pygame.K_5:
                    test[x][y]=5
                if event.key==pygame.K_6:
                    test[x][y]=6
                if event.key==pygame.K_7:
                    test[x][y]=7
                if event.key==pygame.K_8:
                    test[x][y]=8
                if event.key==pygame.K_9:
                    test[x][y]=9
                
                if event.key == pygame.K_RETURN:
                    clickcell=False

                if event.key == pygame.K_BACKSPACE:
                    test[x][y]=0
                    

        if event.type == pygame.QUIT:
            running= False

    


    for i in range(0,len(test)):
        for j in range(0,len(test[i])):
            if test[i][j] != 0:
                label = myfont.render(str(test[i][j]), 50, (0,0,0))
                screen.blit(label, ((i*50)+18.75, (j*50)+18.75))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()


