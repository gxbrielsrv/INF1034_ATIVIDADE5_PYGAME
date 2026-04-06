from pygame import *
import sys 
init()

newton_img = image.load("newton.png")
newton_img = transform.scale(newton_img,(250,250))

newton_font = font.Font("fonte_newton", 30, True, False)

# newton_music.load("newton_music.mp3")
# mixer_music.play(-1)




window = display.set_mode((1280,720))
window.fill((151, 209, 250))


while True:
    for ev in event.get():
        if  ev.type == QUIT:
            quit()
            sys.exit()

    #Desenhar aqui:
    draw.rect(window,(72, 157, 37),(0,580,1280,220))
    draw.circle(window,(255, 255, 255,), (800, 100), 50)
    draw.circle(window,(255, 255, 255,), (865, 100), 50)
    draw.circle(window,(255, 255, 255,), (930, 100), 50)
    draw.circle(window,(255, 255, 255,), (995, 100), 50)
    draw.rect(window,(100, 100, 100),(250, 330, 250,250))

    #Desenhar qualquer poligono:
    draw.polygon(window,(140, 72, 4),((250,330),(375,200),(500,330)))

    #Desenhar linhas:
    draw.line(window,(0, 0, 0),(250,330),(500,330),5)
    draw.line(window,(0, 0, 0),(375,200),(250,330),5)
    draw.line(window,(0, 0, 0),(375,200),(500,330),5)
    
    #Sol
    draw.line(window,(255, 196, 0),(160,120),(250,200),8)
    draw.line(window,(255, 196, 0),(160,120),(100,230),8)
    draw.line(window,(255, 196, 0),(160,120),(170,230),8)
    draw.line(window,(255, 196, 0),(160,120),(230,290),8)
    
    
    
    draw.circle(window,(255, 196, 0),(160,120),50)

    #Arvore
    draw.rect(window,(99, 60, 15),(1000, 420, 50,160))
    draw.circle(window,(12, 107, 20),(1025,380), 100)
    
    #Desenhar imagem:
    window.blit(newton_img,(740,400))
    
    #Desenhar texto:
    newton_text = newton_font.render("I am Newton", True, (0,0,0))
    window.blit(newton_text,(750, 650))


    #Colocar som:
    

    
    display.update()