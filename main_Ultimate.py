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
# mixer_music.load("newton_music.mp3")
# mixer_music.play(-1)
# music = mixer.Sound("newton_music.mp3")
# music.set_volume(0.1)

# mixer_music.load("manha.mp3")
# mixer_music.play(0)
# manha = mixer.Sound("manha.mp3")
# music.set_volume(0.1)

# tarde = mixer.Sound("")


# noite = mixer.Sound("")


window = display.set_mode((1280,720))
window.fill((151, 209, 250))
running = True
clock = time.Clock()





#margem da tela para nuvem
margem_esquerda = 50
largura = 1030

#limite da tela para o sol
largura = 1280
altura =  720
raio = 50

#sol posicao

sol_x = 160
sol_y = 120


timer = 0

#nuvem posicao 
nuvem_x = 800
velocidade = 3

while running:
    clock.tick(60)
    for ev in event.get():
        if  ev.type == QUIT:
            running = False
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            
    dt = clock.get_time()/1000
    timer = timer + dt
    keys = key.get_pressed()

    #fundo:
    if sol_x < 427:
        background_color = '#97d1fa'
        mixer_music.load("manha.mp3")
        mixer_music.play(0)
        manha = mixer.Sound("manha.mp3")
        manha.set_volume(0.1)
        manha.play()
    elif sol_x > 427 and  sol_x < 854:
        background_color = '#f37e30'
        
    else:
        background_color = '#070c52'








    #desenhar aqui:

    #nuvem andando
    if nuvem_x > largura:
        velocidade = -3
    elif nuvem_x < margem_esquerda: 
        velocidade = 3
    nuvem_x += velocidade            
    window.fill(background_color)                
    
   
    
    #sol
    if keys[K_d]:
        sol_x += 200 * dt
    if keys[K_a]:
        sol_x -= 200 * dt
    if keys[K_w]:
        sol_y -= 200 * dt
    if keys[K_s]:
        sol_y += 200 * dt
    draw.circle(window,(255,196,0),(sol_x,sol_y),50)
    draw.line(window,(255,196,0),(sol_x,sol_y-50),(sol_x,sol_y-100),8)   
    draw.line(window,(255,196,0),(sol_x,sol_y+50),(sol_x,sol_y+100),8)   
    draw.line(window,(255,196,0),(sol_x-50,sol_y),(sol_x-100,sol_y),8)   
    draw.line(window,(255,196,0),(sol_x+50,sol_y),(sol_x+100,sol_y),8)   
    draw.line(window,(255,196,0),(sol_x-35,sol_y-35),(sol_x-70,sol_y-70),8)
    draw.line(window,(255,196,0),(sol_x+35,sol_y-35),(sol_x+70,sol_y-70),8)
    draw.line(window,(255,196,0),(sol_x-35,sol_y+35),(sol_x-70,sol_y+70),8)
    draw.line(window,(255,196,0),(sol_x+35,sol_y+35),(sol_x+70,sol_y+70),8)

    if sol_x < raio:
        sol_x = raio
    elif sol_x > largura - raio:
        sol_x = largura - raio
    elif sol_y < raio:
        sol_y = raio
    elif sol_y > altura - raio:
        sol_y = altura - raio

    #nuvem:
    draw.circle(window,(255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 65, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 130, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 195, 100), 50)

    #casa
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
    # manha.play()
    
    display.update()