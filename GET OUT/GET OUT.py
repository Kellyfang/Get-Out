


#Almighty Tech
#Get out

from gamelib import*
game=Game(800,600,"GET OUT")
bk=Image("images\\bk.jpg",game)
bk.resizeTo(800,600)
logo=Image("images\\GET OUT!!!.png",game)
comp=Image("images\\ALMIGHTY TECH.png",game)
comp.moveTo(400,400)
bk2=Image("images\\haunted house.png",game)
bk2.resizeTo(800,600)
eman=Animation("images\\kevin.png",21,game,1161/7,810/3)
eman.resizeBy(-40)
eman.moveTo(100,500)

'''g1=Animation("images\\amy.png",21,game,670/7,391/3)
g1.resizeBy(-40)'''
angelica=Animation("images\\angel.png",8,game,863/8,141,6)
angelica.moveTo(200,500)
game.setBackground(bk2)
ghost=Animation("images\\ghost.png",40,game,466/10,192/4)
ghost2=Animation("images\\ghost.png",40,game,466/10,192/4)
ghosts=Animation("images\\ghost.png",40,game,466/10,192/4)
ghosts.resizeBy(-10)
ghost.setSpeed(3,60)
ghost.moveTo(100,450)
ghost2.setSpeed(3,60)
ghost2.moveTo(600,200)
jumping = False 
landed = False
factor = 1  
ghosts = []#empty list
for index in range(20):#use a loop to add items
    ghosts.append(Animation("images\\ghost.png",40,game,466/10,192/4,2))
for index in range(20):#use a loop to set the positions and speed
    x = randint(800,4000)
    y = randint(400,550)
    ghosts[index].moveTo(x,y)
    ghosts[index].setSpeed(3,90)

ghostsPassed=0
while not game.over:
    game.processInput()
    bk.draw()
    logo.draw()
    comp.draw()
    ghost.move(True)
    ghost2.move(True) 

    
    if keys.Pressed[K_SPACE]:
        game.over=True


    game.update(60)

game.over=False
ghosts = []#empty list
for index in range(20):#use a loop to add items
    ghosts.append(Animation("images\\ghost.png",40,game,466/10,192/4,2))
for index in range(20):#use a loop to set the positions and speed
    x = randint(800,4000)
    y = randint(400,550)
    ghosts[index].moveTo(x,y)
    ghosts[index].setSpeed(3,90)
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)                        
    angelica.draw()
    for index in range(20):
        ghosts[index].move()
    
    for index in range(20):#the loop will go through the list of asteroids   
        if ghosts[index].collidedWith(angelica):#each asteroid is checked
            angelica.health -= 1
        if ghosts[index].isOffScreen("left") and ghosts[index].visible:
            ghosts[index].visible=False
            ghostsPassed+=1
    if angelica.y< 500:
        landed = False
    else:
        landed = True

    if keys.Pressed[K_SPACE] or keys.Pressed[K_UP] and landed and not jumping:
        jumping = True


    if jumping:
        angelica.y -=27*factor
        factor*=.95
        landed = False
        if factor < .18:
            jumping = False
            factor = 1
            
    if not landed:
        angelica.y +=8
    if keys.Pressed[K_RIGHT]:
         angelica.x+=2
    if keys.Pressed[K_LEFT]:
        angelica.x-=2
    if angelica.health<=1:
        game.over=True
    if ghostsPassed>=20:
        game.over=True 
    game.drawText("ghostsPassed: " + str(ghostsPassed), 600, 100)
    game.drawText("health: "+str(angelica.health),angelica.x,angelica.y+50)
    game.update(60)

game.over=False
ghosts2 = []#empty list
for index in range(50):#use a loop to add items
    ghosts2.append(Animation("images\\ghost.png",40,game,466/10,192/4,2))
for index in range(50):#use a loop to set the positions and speed
    x = randint(800,10000)
    y = randint(400,550)
    ghosts2[index].moveTo(x,y)
    ghosts2[index].setSpeed(3,90)
ghostsPassed=0
health=0
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)                        
    eman.draw()
    for index in range(50):
        ghosts2[index].move()
    
    for index in range(50):#the loop will go through the list of asteroids   
        if ghosts2[index].collidedWith(eman):#each asteroid is checked
            eman.health -= 1
        if ghosts2[index].isOffScreen("left") and ghosts2[index].visible:
            ghosts2[index].visible=False
            ghostsPassed+=1
    if eman.y< 500:
        landed = False
    else:
        landed = True

    if keys.Pressed[K_SPACE] or keys.Pressed[K_UP] and landed and not jumping:
        jumping = True


    if jumping:
        eman.y -=27*factor
        factor*=.95
        landed = False
        if factor < .18:
            jumping = False
            factor = 1
            
    if not landed:
        eman.y +=8
    if keys.Pressed[K_RIGHT]:
         eman.x+=2
    if keys.Pressed[K_LEFT]:
        eman.x-=2
    if eman.health<=1:
        game.over=True
    if ghostsPassed>=50:
        game.over=True 
    game.drawText("ghostsPassed: " + str(ghostsPassed), 600, 100)
    game.drawText("health: "+str(eman.health),eman.x,eman.y+50)
    game.update(60)

game.over=False
logo2=Image("images\\gameover.png",game)



     
while not game.over:
          game.processInput()
          bk.draw()
          logo2.draw()
          game.update(60)
