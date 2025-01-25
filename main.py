import turtle
import random


ekran = turtle.Screen()
ekran.bgcolor("#1e423e")
ekran.title("Cath The Turtle")

yazar = turtle.Turtle()
yazar.penup()
yazar.sety(280)
yazar.write("Hedefi Yakala!", align="center", font=("Arial", 16, "normal"))
yazar.hideturtle()

puan = 0
puan_gosterici = turtle.Turtle()
puan_gosterici.penup()
puan_gosterici.sety(260)
puan_gosterici.write(f"Score: {puan}", align="center", font=("Arial", 14, "normal"))
puan_gosterici.hideturtle()

hedef = turtle.Turtle()
hedef.shape("turtle")
hedef.penup()

def hedef_konum_degistir():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    hedef.goto(x, y)
    hedef.getscreen().ontimer(hedef_konum_degistir, 300)

hedef_konum_degistir()

def sol_tikla(x,y):
    print("Sol tık yapıldı")
    global puan
    if hedef.distance(x,y) < 15:
        puan += 1
        puan_gosterici.clear()
        puan_gosterici.write(f"Score: {puan}", align="center", font=("Arial", 14, "normal"))
        print(f"Puan: {puan}")
        if puan == 5:
            hedef.hideturtle()
            yazar.home()
            yazar.write("Hedefi tamamladınız!", align="center", font=("Arial", 16, "normal"))


ekran.onscreenclick(sol_tikla, 1)

turtle.mainloop()
