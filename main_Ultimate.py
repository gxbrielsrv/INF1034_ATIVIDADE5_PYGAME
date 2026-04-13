from pygame import *
import sys 
init()


#imagens
newton_img = image.load("newton.png")
newton_img = transform.scale(newton_img,(250,250))
maca_img = image.load("maca.png")
maca_img = transform.scale(maca_img,(50,50))

#texto
newton_font = font.Font("contrast.ttf", 30)
newton_text = newton_font.render("I am Newton", True, (0,0,0))

#musica
mixer_music.load("newton_music.mp3")
mixer_music.play(-1)
music = mixer.Sound("newton_music.mp3")
music.set_volume(0.1)


window = display.set_mode((1280,720))
window.fill((151, 209, 250))
running = True
clock = time.Clock()








#nuvem andando
nuvem_x = 800
velocidade = 5

timer = 0

while running:
    clock.tick(60)
    for ev in event.get():
        if  ev.type == QUIT:
            running = False
    dt = clock.get_time()/1000
    timer = timer + dt
    print(dt)



    #nuvem andando
    window.fill((151, 209, 250))
    nuvem_x += velocidade
    if nuvem_x > 1280:
        nuvem_x = 800
    

    #desenhar aqui:
    draw.rect(window,(72, 157, 37),(0,580,1280,220))
    draw.rect(window,(100, 100, 100),(250, 330, 490,250))
    draw.rect(window,(140, 72, 4),(375, 200, 365,130))
    draw.rect(window,(41, 22, 1),(325,370,100,210))
    draw.circle(window, (0,0,0), (350, 485),8)
    draw.rect(window,(4, 191, 182),(500, 385, 200, 100))

    #desenhar qualquer poligono:
    draw.polygon(window,(140, 72, 4),((250,330),(375,200),(500,330)))

    #desenhar linhas:
    draw.line(window,(0, 0, 0),(250,330),(500,330),5)
    draw.line(window,(0, 0, 0),(375,200),(250,330),5)
    draw.line(window,(0, 0, 0),(375,200),(500,330),5)
    
    #sol
    draw.line(window,(255, 196, 0),(160,120),(250,200),8)
    draw.line(window,(255, 196, 0),(160,120),(100,230),8)
    draw.line(window,(255, 196, 0),(160,120),(180,230),8)
    draw.line(window,(255, 196, 0),(160,120),(230,260),8)
    draw.line(window,(255, 196, 0),(160,120),(230,10),8)
    draw.line(window,(255, 196, 0),(160,120),(250,50),8)
    draw.line(window,(255, 196, 0),(160,120),(270,105),8)
    draw.line(window,(255, 196, 0),(160,120),(290,145),8)
    draw.line(window,(255, 196, 0),(160,120),(25,185),8)
    draw.line(window,(255, 196, 0),(160,120),(33,120),8)
    draw.line(window,(255, 196, 0),(160,120),(25,60),8)
    draw.line(window,(255, 196, 0),(160,120),(45,10),8)
    draw.line(window,(255, 196, 0),(160,120),(120,10),8)
    draw.line(window,(255, 196, 0),(160,120),(180,10),8)
    draw.circle(window,(255, 196, 0),(160,120),50)

    #nuvem parada
    # draw.circle(window,(255, 255, 255,), (800, 100), 50)
    # draw.circle(window,(255, 255, 255,), (865, 100), 50)
    # draw.circle(window,(255, 255, 255,), (930, 100), 50)
    # draw.circle(window,(255, 255, 255,), (995, 100), 50)

    #nuvem andando
    draw.circle(window,(255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 65, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 130, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 195, 100), 50)

    #arvore
    draw.rect(window,(99, 60, 15),(1000, 420, 50,160))
    draw.circle(window,(12, 107, 20),(1025,380), 100)
    
    #desenhar imagem:
    window.blit(newton_img,(740,400))
    window.blit(maca_img,(1010, 390))
    window.blit(maca_img,(950, 320))
    window.blit(maca_img,(1050, 310))
    
    #desenhar texto:
    window.blit(newton_text,(750, 650))

    #colocar som:
    music.play()
    
    display.update()