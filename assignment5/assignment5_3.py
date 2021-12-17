import turtle

def drawPolygan(n):
    for i in range(n):
        turtle.shape("turtle")
        turtle.speed(1)
        turtle.forward( 10 +  50 + (n**2) )
        turtle.right( 360 / n )              
n = 3    
while n <= 13:
        drawPolygan(n)
        turtle.penup()
        turtle.right(50)
        turtle.forward(-10)
        turtle.left(50)
        turtle.pendown ()
        n = n + 1 
