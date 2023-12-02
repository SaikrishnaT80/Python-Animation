import turtle as tur
import colorsys as cs
tur.setup(500,500)
tur.speed(150)
tur.width(4)
tur.bgcolor("black")
for j in range(50):
    for i in range(30):
        tur.color(cs.hls_to_rgb (i/10, j/10,1))
        tur.right(80)
        tur.circle(90-j*4,90)
        tur.left(80)
        tur.circle(90-j*4,90)
        tur.right(80)
        tur.circle(90,90)
        
tur.hideturtle()
cs.done()
    

