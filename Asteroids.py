import pygame
import random
import os 
ANCHO = 1200
ALTO = 600
FPS = 50

# COLORES
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255,255,0)

#carpetas utiles
game_folder = os.path.dirname(__file__)
img_folder  =os.path.join(game_folder,"Imagenes")
snd_folder = os.path.join(os.path.dirname(__file__),"Sonidos")

POWERUP_TIME = 10000
nombrefuente = pygame.font.match_font("arial")
def draw_text(superficie, texto, tamaño,x ,y):
    font = pygame.font.Font(nombrefuente, tamaño)
    text_surface = font.render(texto,True,BLANCO)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    superficie.blit(text_surface,text_rect)
def draw_shieldbar(surf ,x,y,porcentaje):
    if porcentaje < 0:
        porcentaje = 0
    Largobarra = 100
    Altobarra = 10
    fill = (porcentaje /100) * (Largobarra)
    marco = pygame.Rect(x,y,Largobarra,Altobarra)
    fill_rect = pygame.Rect(x,y,fill,Altobarra)
    pygame.draw.rect(surf,VERDE,fill_rect)
    pygame.draw.rect(surf,BLANCO,marco,2)

        
class Player(pygame.sprite.Sprite):
    #Sprite de jugador
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(jugador_img,(50,38))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center=(25,300)
        self.shield = 100
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        #tiempo powerup
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power = 1
            self.power_time = pygame.time.get_ticks
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 8
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 8
        if keystate[pygame.K_UP]:
            self.rect.y -= 8
        if keystate[pygame.K_DOWN]:
            self.rect.y += 8
        if self.rect.bottom < 0:
            self.rect.top = ALTO
        if self.rect.top > ALTO:
            self.rect.bottom = 0
        if self.rect.left <=0:
            self.rect.left = 0
    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()
    def disparar(self):
        if self.power == 1:
            misil = Misil(self.rect.right,self.rect.centery)
            sprites.add(misil)
            misiles.add(misil)
        if self.power >= 2:
            misil = Misil(self.rect.right,self.rect.centery-13)
            misil2 = Misil(self.rect.right,self.rect.centery+13)
            sprites.add(misil)
            sprites.add(misil2)
            misiles.add(misil)
            misiles.add(misil2)
        shoot_snd.play()
        

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"Astpequeño.png")).convert()
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1250,1300,50)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        #self.rect.x = random.randrange(ANCHO - self.rect.width)
        #self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(-3,3)
        self.speedx = random.randrange(1,10)
    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right<-10:
            self.rect.x = random.randrange(1250,1300,50)
            self.rect.y = random.randrange(ALTO - self.rect.height)
            self.speedx = random.randrange(5,20)
        #if self.rect.left > ANCHO:
         #   self.rect.right = 0
        #if self.rect.right < 0:
         #   self.rect.left = ANCHO
        if self.rect.bottom < 0:
            self.rect.top = ALTO
        if self.rect.top > ALTO:
            self.rect.bottom = 0

class Alienrojo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(alienrojo_img,(34,34))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1250,1300,50)
        self.rect.y = random.randrange(ALTO - self.rect.height)

        self.speedy = random.randrange(-7,7)
        self.speedx = random.randrange(13,20)
    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right<-10:
            self.rect.x = random.randrange(1250,1300,50)
            self.rect.y = random.randrange(ALTO - self.rect.height)
            self.speedx = random.randrange(13,20)
        if self.rect.right < 0:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > ALTO:
            self.kill()
class Alienamarillo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(alienamarillo_img,(34,34))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1250,1300,50)
        self.rect.y = random.randrange(ALTO - self.rect.height)

        self.speedy = random.randrange(-7,7)
        self.speedx = random.randrange(13,20)
    def update(self):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.right<-10:
            self.rect.x = random.randrange(1250,1300,50)
            self.rect.y = random.randrange(ALTO - self.rect.height)
            self.speedx = random.randrange(13,20)
        if self.rect.right < 0:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > ALTO:
            self.kill()

class Misil(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(misil_img,(26,6))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speedx = 15
    def update(self):
        self.rect.x += self.speedx
        #muere si se va de la parte derecha de la pantalla
        if self.rect.left > 1200:
            self.kill()
class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75


    def update(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.last_update > self.frame_rate:
            self.last_update = ahora
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                
class Powershield(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pow_shield_img,(20,20))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = -4
        self.speedy = random.randrange(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #muere si se va de la parte derecha de la pantalla
        if self.rect.right < 0:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top>ALTO:
            self.kill()
class Powergun(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pow_gun_img,(20,20))
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = -4
        self.speedy = random.randrange(-3,3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        #muere si se va de la parte derecha de la pantalla
        if self.rect.right < 0:
            self.kill()
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top>ALTO:
            self.kill()
def gameoverscreen():
    win.blit(fondo,fondo_rect)
    draw_text(win, "ASTEROIDS",64,ANCHO/2,ALTO/4)
    draw_text(win,"Flechas para moverse || espacio para disparar",22,ANCHO/2,ALTO/2)
    draw_text(win,"Presiona una tecla para comenzar",18,ANCHO/2,ALTO*3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                



# iniciar y crear juego
pygame.init()
pygame.mixer.init()
##PANTALLA
win = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()


#HIGHSCORE
#######################
#CARGAR SPRITES
fondo  = pygame.image.load(os.path.join(img_folder,"scs.png")).convert()
fondo_rect = fondo.get_rect()

jugador_img = pygame.image.load(os.path.join(img_folder,"playerShip3_blue.png")).convert()
meteoro_img = pygame.image.load(os.path.join(img_folder,"Astpequeño.png")).convert()
misil_img = pygame.image.load(os.path.join(img_folder,"laserBlue16.png")).convert()
alienrojo_img = pygame.image.load(os.path.join(img_folder,"ufoRed.png")).convert()
alienamarillo_img = pygame.image.load(os.path.join(img_folder,"ufoYellow.png")).convert()
explosion_anim = {}
explosion_anim["lg"] = []
explosion_anim["player"] = []
for i in range(9):
    filename = "regularExplosion0{}.png".format(i)
    img = pygame.image.load(os.path.join(img_folder,filename)).convert()
    img.set_colorkey(NEGRO)
    img_sz = pygame.transform.scale(img,(40,40))
    filename = "sonicExplosion0{}.png".format(i)
    img = pygame.image.load(os.path.join(img_folder,filename)).convert()
    img.set_colorkey(NEGRO)
    explosion_anim["player"].append(img)
    
    explosion_anim["lg"].append(img_sz)
pow_shield_img = pygame.image.load(os.path.join(img_folder,"shield_gold.png"))
pow_gun_img = pygame.image.load(os.path.join(img_folder,"bolt_gold.png"))
#Sonidos
playerexp_snd = pygame.mixer.Sound(os.path.join(snd_folder,"rumble1.ogg"))
shoot_snd = pygame.mixer.Sound(os.path.join(snd_folder,"Laser_Shoot7.wav"))
alien_snd = pygame.mixer.Sound(os.path.join(snd_folder,"Randomize2.wav"))
shield_snd = pygame.mixer.Sound(os.path.join(snd_folder,"Powerup8.wav"))
gun_snd = pygame.mixer.Sound(os.path.join(snd_folder,"Powerup9.wav"))
expl_snd = []
for snd in ["Explosion18.wav","Explosion38.wav"]:
    expl_snd.append(pygame.mixer.Sound(os.path.join(snd_folder,snd)))

pygame.mixer.music.load(os.path.join(snd_folder,"tgfcoder-FrozenJam-SeamlessLoop.ogg"))
pygame.mixer.music.set_volume(4)
#GRUPOS

pygame.mixer.music.play(loops=-1)
#####################################################
#####################################################
# LOOP DEL JUEGO
gameover = True
running = True
while running:
    if gameover:
        gameoverscreen()
        gameover = False
        misiles = pygame.sprite.Group()
        sprites = pygame.sprite.Group()
        guns = pygame.sprite.Group()
        shields = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        Aliensred = pygame.sprite.Group()
        Aliensama = pygame.sprite.Group()
        JUGADOR = Player()
        sprites.add(JUGADOR)

        for i in range(15):
            m = Mob()
            sprites.add(m)
            mobs.add(m)
        score = 0
    clock.tick(FPS)
    # EVENTOS
    
    for event in pygame.event.get():
        # CERRAR
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score -= 10
                JUGADOR.disparar()                
    #POSIBILIDAD DE SPAWNEAR ALIEN ROJO
    randomnumber = random.randrange(1,5000)
    if 1<= randomnumber and randomnumber <= 10:
        a = Alienrojo()
        sprites.add(a)
        Aliensred.add(a)
    #POSIBILIDAD DE SPAWNEAR ALIEN AMARILLO
    randomnumberr = random.randrange(1,5000)
    if 1<= randomnumberr and randomnumberr <= 10:
        o = Alienamarillo()
        sprites.add(o)
        Aliensama.add(o)
    #CHEQUEAR SI UN ALIEN AMARILLO COLISIONA CON EL JUGADOR
    hits = pygame.sprite.spritecollide(JUGADOR,Aliensama,True)
    for hit in hits:
        JUGADOR.shield -= 50
        expl = Explosion(hit.rect.center,"lg")
        sprites.add(expl)
        if JUGADOR.shield > 0:
            alien_snd.play()
        if JUGADOR.shield <= 0:
            JUGADOR.kill()
            explosionmuerte = Explosion(JUGADOR.rect.center,"player")
            sprites.add(explosionmuerte)
            playerexp_snd.play()
    #CHEQUEAR SI UN ALIEN ROJO COLISIONA CON EL JUGADOR
    hits = pygame.sprite.spritecollide(JUGADOR,Aliensred,True)
    for hit in hits:
        JUGADOR.shield -= 50
        expl = Explosion(hit.rect.center,"lg")
        sprites.add(expl)
        if JUGADOR.shield > 0:
            alien_snd.play()
        if JUGADOR.shield <= 0:
            JUGADOR.kill()
            explosionmuerte = Explosion(JUGADOR.rect.center,"player")
            sprites.add(explosionmuerte)
            playerexp_snd.play()
    # Actualizar sprites
    sprites.update()
    #CHEQUEAR SI UN ALIEN AMARILLO COLISIONA CON EL MISIL
    hits = pygame.sprite.groupcollide(Aliensama,misiles,True,True)
    for hit in hits:
        power = Powershield(hit.rect.center)
        sprites.add(power)
        shields.add(power)
        alien_snd.play()
        score+=60
        expl = Explosion(hit.rect.center,"lg")
        sprites.add(expl)
    #CHEQUEAR SI EL JUGADOR COLISIONA CON EL SHIELD
    hits = pygame.sprite.spritecollide(JUGADOR,shields,True)
    for hit in hits:
        shield_snd.play()
        JUGADOR.shield += random.randrange(10,50)
        if JUGADOR.shield > 100:
            JUGADOR.shield = 100
    #CHEQUEAR SI EL JUGADOR COLISIONA CON EL POWERGUN
    hits = pygame.sprite.spritecollide(JUGADOR,guns,True)
    for hit in hits:
        gun_snd.play()
        JUGADOR.powerup()
        
    #CHEQUEAR SI UN ALIEN ROJO COLISIONA CON EL MISIL
    hits = pygame.sprite.groupcollide(Aliensred,misiles,True,True)
    for hit in hits:
        power = Powergun(hit.rect.center)
        sprites.add(power)
        guns.add(power)
        alien_snd.play()
        score+=60
        expl = Explosion(hit.rect.center,"lg")
        sprites.add(expl)
    #Chequear si un enemigo colisiona con el misil
    hits = pygame.sprite.groupcollide(mobs,misiles,True,True)
    for hit in hits:
        random.choice(expl_snd).play()
        score+= 20
        m = Mob()
        sprites.add(m)
        mobs.add(m)
        expl = Explosion(hit.rect.center,"lg")
        sprites.add(expl)
    #Chequear si un enemigo colisiona con el jugador
        
    hits = pygame.sprite.spritecollide(JUGADOR,mobs,True)
    for hit in hits:
        JUGADOR.shield -= 25
        expl = Explosion(hit.rect.center,"lg")
        sprites.add(expl)
        m = Mob()
        sprites.add(m)
        mobs.add(m)
        if JUGADOR.shield > 0:
            random.choice(expl_snd).play()
        #PONER SONIDO DE GOLPE
        if JUGADOR.shield <= 0:
            JUGADOR.kill()
            explosionmuerte = Explosion(JUGADOR.rect.center,"player")
            sprites.add(explosionmuerte)
            playerexp_snd.play()
    #CUANDO EL JUGADOR MUERA Y LA EXPLOSION TERMINE
    if not JUGADOR.alive() and not explosionmuerte.alive():
        gameover = True
    #DIBUJAR
    win.fill(NEGRO)
    win.blit(fondo,fondo_rect)
    sprites.draw(win)
    draw_text(win,str(score),18,ANCHO/2,10)
    draw_shieldbar(win,5,5,JUGADOR.shield)
    pygame.display.flip()

pygame.quit()
