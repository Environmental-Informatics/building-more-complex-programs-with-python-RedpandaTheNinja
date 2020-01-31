import turtle
import math

bob = turtle.Turtle()
bob.speed( 'fastest' )


# polygon example from the book
def polygon(t , n , length):
    angle = 360 / n
    for i in range( n ):
        t.fd( length )
        t.lt( angle )


# arc example from the book
def arc(t , r , angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int( arc_length / 3 ) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range( n ):
        t.fd( step_length )
        t.lt( step_angle )


# petal function to draw the petal
def petal(t , r , angle):
    for i in range( 2 ):
        arc( t , r , angle )
        t.lt( 180 - angle )


# flower function with n number of leaf
def flower(t , n , r , angle , p):
    "draw flower with n petal"
    for i in range( n ):
        petal( t , r , angle )
        t.lt( p / n )


# create 7 leaf flower
# flower(bob, 7, 50, 60, 360)
# overlapping leaf with more leaf , changed pedal num and angle compared to before
# flower(bob, 10, 50, 100, 360)
# added more leaf and adjust angle to create thinner appearance
flower( bob , 20 , 90 , 20 , 360 )
turtle.mainloop()
