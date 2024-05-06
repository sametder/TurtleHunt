import turtle
import random
import time

# Pencereyi oluştur
board = turtle.Screen()
board.title("Kaplumbağa Avi")
board.bgcolor("white")
board.setup(width=600, height=600)

# Skor 
skor = 0

skor_turtle = turtle.Turtle()
skor_turtle.speed(0)
skor_turtle.color("black")
skor_turtle.penup()
skor_turtle.hideturtle()
skor_turtle.goto(0, 260)
skor_turtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

#zaman
zaman_turtle = turtle.Turtle()
zaman_turtle.speed(0)
zaman_turtle.color("black")
zaman_turtle.penup()
zaman_turtle.hideturtle()
zaman_turtle.goto(0, -280)

# Kaplumbağa nesnesini oluştur
kaplumbaga = turtle.Turtle()
kaplumbaga.speed(0)
kaplumbaga.shape("turtle")
kaplumbaga.color("green")
kaplumbaga.penup()

def tiklama(x, y):
    global skor
    if kaplumbaga.distance(x, y) < 20:
        skor += 1
        kaplumbaga.goto(random.randint(-280, 280), random.randint(-280, 280))
        skor_turtle.clear()
        skor_turtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

board.onclick(tiklama)

# Oyunun ana döngüsü
while skor < 10:  # Örneğin, skor 10 olduğunda oyun dursun
    # Kaplumbağa rastgele bir konuma yerleştir
    kaplumbaga.goto(random.randint(-280, 280), random.randint(-280, 280))
    zaman = 10  # Zamanı 10 saniyeye ayarla
    while zaman > 0:
        zaman_turtle.clear()
        zaman_turtle.write("Zaman: {}".format(zaman), align="center", font=("Courier", 24, "normal"))
        time.sleep(1)
        zaman -= 1

# Oyun bittiğinde ekranda kalmak için bekle
board.mainloop()
