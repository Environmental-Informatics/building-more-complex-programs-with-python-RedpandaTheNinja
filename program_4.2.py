import turtle
import math
bob = turtle.Turtle()
bob.speed('fastest')
# print(bob)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
#

# def circle(t, r):
#     circumference = 2 * math.pi *r
#     n = 50
#     length= circumference / n
#     polygon(t, n, length)
#     # arc(t, r, 360)
def polygon(t,n, length):
    angle = 360 /n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def circle(t,r):
    arc(t,r,360)

# polygon(bob, 7,70)

def polyline(t , n , length, angle):
    "draws n line seg with the given length and angle. t is a turtle"
    for i in range (n):
        t.fd(length)
        t.lt(angle)
def polygon(t,n,length):
    angle = 360.0/n
    polyline(t,n,length,angle)

def petal( t, r, angle):
    for i in range(2):
        arc(t,r,angle)
        t.lt(180-angle)
def flower (t,n,r,angle,p):
    "draw flower with n petal"
    for i in range(n):
        petal(t,r,angle)
        t.lt(p/n)

#create 7 leaf flower
# flower(bob, 7, 50, 60, 360)
#overlapping leaf with more leaf , changed pedal num and angle compared to before
# flower(bob, 10, 50, 100, 360)
#added more leaf and adjust angle to create thinner appearance
flower(bob, 20, 90, 20, 360)
turtle.mainloop()