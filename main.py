from pygame import *
import sys 
import random
init()

#background_color = '#97d1fa'

#sfx
manha_sfx = mixer.Sound('manha.wav')
tarde_sfx = mixer.Sound('tarde.wav')
noite_sfx = mixer.Sound('noite.wav')
manha_sfx.set_volume(0.2)
tarde_sfx.set_volume(0.2)
noite_sfx.set_volume(0.2)

#margem da tela = 
margem_left = 40
margem_right = 1040 
margem_top = 50
margem_bottom = 670

#sol variaveis
sol_x = 200
sol_y = 150
cor_manha = (151, 209, 250)
cor_tarde = (207, 114, 0)
cor_noite = (1, 17, 64)

#funcao ceu:
def corCeu(cor1, cor2, tempo):
    return (
        (cor1[0] + (cor2[0] - cor1[0]) * tempo),
        (cor1[1] + (cor2[1] - cor1[1]) * tempo),
        (cor1[2] + (cor2[2] - cor1[2]) * tempo)
    )
background_color = cor_manha


#imagens
newton_img = image.load("newton.png")
newton_img = transform.scale(newton_img,(250,250))
maca_img = image.load("maca.png")
maca_img = transform.scale(maca_img,(50,50))

#texto
newton_font = font.Font("contrast.ttf", 30)
newton_text = newton_font.render("I am Newton", True, (0,0,0))

#musica
# mixer_music.load("newton_music.mp3")
# mixer_music.play(-1)
# music = mixer.Sound("newton_music.mp3")
# music.set_volume(0.1)


window = display.set_mode((1280,720))
window.fill((151, 209, 250))
running = True
clock = time.Clock()



movimentosol = False




#nuvem andando
nuvem_x = 800
velocidade = 4
sol_x = 160
sol_y = 50








timer = 0

while running:
    clock.tick(60)
    for ev in event.get():
        if ev.type == QUIT:
            running = False

        if ev.type == KEYDOWN:
            if ev.key == K_m:
                movimentosol = not movimentosol

        if movimentosol:
            if ev.type == MOUSEMOTION:
                sol_x, sol_y = ev.pos

            if ev.type == MOUSEBUTTONUP:
                if ev.button == 1:
                    
                    manha_sfx.stop()
                    tarde_sfx.stop()
                    noite_sfx.stop()

                if sol_x < 400:
                    manha_sfx.play()
                elif sol_x > 800:
                    noite_sfx.play()
                else:
                    tarde_sfx.play()

    dt = clock.get_time()/1000
    keys = key.get_pressed()

#mov sol:
    if not movimentosol:
        if keys[K_d]:
            sol_x += 200 * dt
        if keys[K_a]:
            sol_x -= 200 * dt
        if keys[K_w]:
            sol_y -= 200 * dt
        if keys[K_s]:
            sol_y += 200 * dt
    
                
    

    #tempo de acordo com sol_x seco:
    # if sol_x < 427:
    #     background_color = '#97d1fa'
    # elif sol_x > 854:
    #     background_color = '#011140'
    # else:
    #     background_color = '#cf7200'

    #tempo de acordo com o sol_x continuo:
    tempo = (sol_x - 30) / (1230 - 30)
    tempo = max(0, min(1, tempo))
    if tempo < 0.5:
        tempo2 = tempo* 2
        background_color = corCeu(cor_manha, cor_tarde, tempo2)
    else:
        tempo2 = (tempo - 0.5) * 2
        background_color = corCeu(cor_tarde, cor_noite, tempo2)

        



    # limpar resto nuvem andando
    window.fill(background_color)
    
    if sol_x > 1070:
        draw.circle(window, (255,255,255), (100,100), 3)
        draw.circle(window, (255,255,255), (200,80), 3)
        draw.circle(window, (255,255,255), (350,120), 3)
        draw.circle(window, (255,255,255), (500,60), 3)
        draw.circle(window, (255,255,255), (700,90), 3)
        draw.circle(window, (255,255,255), (900,70), 3)

        draw.circle(window, (255,255,255), (150,50), 3)
        draw.circle(window, (255,255,255), (250,140), 3)
        draw.circle(window, (255,255,255), (400,30), 3)
        draw.circle(window, (255,255,255), (600,150), 3)
        draw.circle(window, (255,255,255), (750,40), 3)
        draw.circle(window, (255,255,255), (950,130), 3)

        draw.circle(window, (255,255,255), (50,120), 3)
        draw.circle(window, (255,255,255), (300,60), 3)
        draw.circle(window, (255,255,255), (450,140), 3)
        draw.circle(window, (255,255,255), (650,20), 3)
        draw.circle(window, (255,255,255), (850,110), 3)
        draw.circle(window, (255,255,255), (1100,80), 3)






    # sol
    draw.circle(window,(255,196,0),(sol_x,sol_y),50)
    draw.line(window,(255,196,0),(sol_x,sol_y-50),(sol_x,sol_y-100),8) 
    draw.line(window,(255,196,0),(sol_x,sol_y+50),(sol_x,sol_y+100),8) 
    draw.line(window,(255,196,0),(sol_x-50,sol_y),(sol_x-100,sol_y),8) 
    draw.line(window,(255,196,0),(sol_x+50,sol_y),(sol_x+100,sol_y),8) 
    draw.line(window,(255,196,0),(sol_x-35,sol_y-35),(sol_x-70,sol_y-70),8)
    draw.line(window,(255,196,0),(sol_x+35,sol_y-35),(sol_x+70,sol_y-70),8)
    draw.line(window,(255,196,0),(sol_x-35,sol_y+35),(sol_x-70,sol_y+70),8)
    draw.line(window,(255,196,0),(sol_x+35,sol_y+35),(sol_x+70,sol_y+70),8)

    #limite sol:
    sol_x = max(30, min(1230, sol_x))
    sol_y = max(70, min(630, sol_y))

    #nuvem rebater: 
    if nuvem_x > margem_right:
        velocidade = -4
    if nuvem_x < margem_left: 
        velocidade = 4
    nuvem_x += velocidade

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
    # music.play()
    

    display.update()