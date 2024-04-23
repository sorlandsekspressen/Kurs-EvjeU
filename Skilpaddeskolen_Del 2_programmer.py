# Fullstendig dokumentasjon: https://docs.python.org/3/library/turtle.html

import turtle as t

# Vi får frem skilpadden, gir litt farger og gjør pennen tykkere

t.shape('turtle')
t.color('red')
t.pencolor('blue')
t.pensize('2')

# program 1a: Tegn et kvadrat manuelt uten variabler

t.forward(200) #100 pixler
t.right(90)    #90 grader
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

t.reset() #Fjerner formatteringen vi utførte over

# program 1b: Tegn et kvadrat med foor-loop og variabler

for i in range (4):
    t.forward(200)
    t.right(90)
    
t.reset()  
    
# program 2a: Tegn et rektangel uten variabler

t.forward(200) 
t.right(90)    
t.forward(60)
t.right(90)
t.forward(200)
t.right(90)
t.forward(60)

t.reset() 

# program 2b: Tegn et rektangel med variabler

lengde = 200
bredde = 60

t.forward(lengde) 
t.right(90)    
t.forward(bredde)
t.right(90)
t.forward(lengde)
t.right(90)
t.forward(bredde)

t.reset() 

# program 3a: Tegn en likesidet trekant manuelt 

t.forward(200)
t.right(120)
t.forward(200)
t.right(120)
t.forward(200)

t.reset() 

# program 3b: Tegn en likesidet trekant med loop 

for i in range (3):
    t.forward(200)
    t.right(120)
    
t.reset() 

# program 4: Parallellogram med loop og variabler

lengde = 200
bredde = 60

big_angle = 120

for i in range (2):
    t.forward(lengde)
    t.right(big_angle)
    t.forward(bredde)
    t.right(180-big_angle)

t.reset() 

#program 5: Tegn en rettvinklet trekant

t.forward(300)
t.right(90)
t.forward(400)
t.home()

t.reset() 

# program 6a: Tegn en regulær sekskant med foor-loop

lengde = 100

for i in range (6):
    t.forward(lengde)
    t.right(60)
    
t.reset() 

#program 6b: regulær n-kant (sirkel hvis n->uendelig)

n = 20          #antall sider
omkrets = 600  

for i in range (n):
    t.forward(omkrets/n)
    t.right(360/n)

#program 6c: Morsom loop som tegner alle n-kanter fra n=1 til n=99.

omkrets = 800  

for n in range(1,100):

    for i in range (n):
        t.forward(omkrets/n)
        t.right(360/n)
    
    t.reset()
    
    

# Vent med å avslutte programmet til vinduet lukkes
t.mainloop()