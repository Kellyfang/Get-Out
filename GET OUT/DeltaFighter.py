from gamelib import *

game = Game(800, 800, "Delta Fighter")
#Create graphics variables
bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)

title = Image("images\\logo.png",game)
title.y -= 200

story = Image("images\\story.png",game)
story.resizeBy(-40)
story.y += 100

howtoplay = Image("images\\howtoplay.png",game)
howtoplay.resizeBy(-40)
howtoplay.y += 150
play = Image("images\\play.png",game)
play.resizeBy(-40)
play.y += 200

hero = Image("images\\hero.gif",game)
explosion = Animation("images\\explosion1.png",22,game,1254/22,64)
explosion.visible = False#set the visiblity to false



asteroids = []#empty list
for index in range(100):#use a loop to add items
    asteroids.append( Animation( "images\\asteroid1t.gif",41,game, 2173/41, 52))
for index in range(100):#use a loop to set the positions and speed
    x = randint(100,700)
    y = randint(100,4000)
    asteroids[index].moveTo(x, -y)
    #Zero degrees moves a graphics up
    asteroids[index].setSpeed(6,180)


#Title Screen - first game loop
while not game.over:
    game.processInput()

    game.scrollBackground("down",2)
    title.draw()
    story.draw()
    howtoplay.draw()
    play.draw()
    hero.draw()

    if play.collidedWith(mouse)and mouse.LeftClick:
        game.over = True
    
    game.update(30)

game.over = False#continue the game with a new game loop
#Level 1
asteroidPassed=0
ammo=[]
for index in range(20):
    ammo.append(Animation("images\\plasmaball1.png",11,game,352/11,32))
while not game.over:
    game.processInput()
    
    game.scrollBackground("down",2)
    hero.draw()
    explosion.draw(False)

    for index in range(100):#the loop will go through the list of asteroids
        asteroids[index].move()#each asteroid will move
        if asteroids[index].collidedWith(hero):#each asteroid is checked
            hero.health -= 1
            explosion.moveTo(asteroids[index].x,asteroids[index].y)
            explosion.visible = True
        if asteroids[index].isOffScreen("bottom") and asteroids[index].visible:
            asteroids[index].visible=False
            asteroidPassed += 1
        if asteroidPassed >= 100:
            game.over = True       
    if keys.Pressed[K_UP]:
        hero.y -= 4#Up 4 pixels
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_LEFT]:
        hero.x -= 4
    
        
    
    game.drawText("health: "+str(hero.health),hero.x,hero.y+50)
    game.drawText("asteroidPassed: " + str(asteroidPassed), 600, 100)
    game.update(30)

game.over = False
#level 2
alienPassed=0
aliens=[]
for index in range(50):
    aliens.append(Image("images\\alien2.png",game))
    x = randint(100,700)
    y = randint(100,4000)
    s=randint(8,12)
    aliens[index].moveTo(x, -y)
    aliens[index].resizeBy(-60)
    aliens[index].setSpeed(s,180)
alienWave1complete=0
aliens2=[]
for index in range(100):
    aliens2.append(Image("images\\alien3.png",game))
    x = randint(100,700)
    y = randint(100,4000)
    s=randint(8,12)
    aliens2[index].moveTo(x, -y)
    aliens2[index].resizeBy(-60)
    aliens2[index].setSpeed(s,180)
alienWave2complete=0
while not game.over and hero.health >1:
    game.processInput()
    
    game.scrollBackground("down",2)
    hero.draw()
    explosion.draw(False)

    if keys.Pressed[K_UP]:
        hero.y -= 4#Up 4 pixels
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_LEFT]:
        hero.x -= 4

    for index in range(50):
        aliens[index].move()

        if aliens[index].collidedWith(hero):
            hero.health-=2
            explosion.moveTo(aliens[index].x,aliens[index].y)
            explosion.visible = True
            
        if aliens[index].isOffScreen("bottom") and aliens[index].visible:
            aliens[index].visible=False
            alienPassed += 1
        if alienPassed >= 50:
            game.over = True
            alienPassed-=50
    '''for index in range(100):
        aliens2[index].move()

        if aliens2[index].collidedWith(hero):
            hero.health-=2
            explosion.moveTo(aliens2[index].x,aliens[index].y)
            explosion.visible = True
            
        if aliens2[index].isOffScreen("bottom") and aliens2[index].visible:
            aliens2[index].visible=False
            alienPassed += 1
        if alienPassed >= 100:
            game.over = True
        if hero.health<=1:
            game.over=True'''
    game.drawText("health: "+str(hero.health),hero.x,hero.y+50)        
    game.drawText("alienPassed: " + str(alienPassed), 600, 100)
    game.update(30)
game.over = False
ms=Image("image\\aliensh.png",game)
ms.resizeTo(game.width-20,ms.height-100)
ms.y=-100
ms.setSpeed(0.25,180)

earth=Image("image\\earth.png",game)
earth.resizeTo(game.width+100,earth.height)
earth.y=game.height=+20

pb=Animation("image\\plasmaball1.png",11,game,352/11,32)
pb.visible=False

msa=Image("image\\alien4.png",game)
msa.resizeBy(-60)
msa.visible=False
fires=[]
firecount=0
while not game.over and hero.health >1:
    game.processInput()
    
    game.scrollBackground("down",2)
    ms.move()
    earth.draw()
    fires.draw()
    hero.draw()
    explosion.draw(False)
    

    if pb.collidedWith(ms):
        ms.damage+=10
        pb.visible=False
    if pb.collidedWith(msa):
        msa.visible=False
        pb.visible=False
    for index in range(firecount):
        fires[index].draw()
        if msa.collidedWith(earth):
            fires.append(Animation("image\\fire2.png",9,game,700/9,156))
            fires[firecount].moveTo(msa.x,msa.y)
            firecount-=1
    if keys.Pressed[K_UP]:
        hero.y -= 8
    if keys.Pressed[K_DOWN]:
        hero.y += 8
    if keys.Pressed[K_RIGHT]:
        hero.x += 8
    if keys.Pressed[K_LEFT]:
        hero.x -= 8
    if keys.Pressed[K_SPACE]:
        pb.moveTo(hero.x,hero.y)
        pb.setSpeed(24,0)
        pb.wisible=True
    if hero.health<1:
        game.over=True
    if ms.health>=100:
        game.over=True
    game.update(30)



