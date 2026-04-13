from pygame import *
import sys 
init()

background_color = '#97d1fa'

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
sol_x = 160
linha_1 = 250
linha_2 = 100
linha_3 = 180
linha_4 = 230







timer = 0

while running:
    clock.tick(60)
    for ev in event.get():
        if  ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (243, 126, 48)
                
                
    






    dt = clock.get_time()/1000
    keys = key.get_pressed()


    #se eu pressionar a tecla D, entao:
    

    timer = timer + dt
    if nuvem_x <= 1030:
        nuvem_x = nuvem_x +100* dt
    else:
        nuvem_x = nuvem_x - 100* dt
    
    




    # #nuvem andando
    window.fill(background_color)
    # if nuvem_x > 1280:
    #     nuvem_x = 800
    

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
    








    if keys[K_d]:
        sol_x = sol_x + 200 * dt
    elif keys[K_a]:
        sol_x = sol_x - 200* dt
    #sol
    draw.circle(window,(255, 196, 0),(sol_x,120),50)
    draw.line(window,(255, 196, 0),(sol_x,120),(linha_1, 200),8)
    draw.line(window,(255, 196, 0),(sol_x,120),(linha_2,230),8)
    draw.line(window,(255, 196, 0),(sol_x,120),(linha_3 ,230),8)
    draw.line(window,(255, 196, 0),(sol_x,120),(linha_4,260),8)
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