import time
import turtle
import random



#Oyun Ekranını oluşturma
game_sc = turtle.Screen()
game_sc.bgcolor("light blue")
game_sc.title("Catch the Turtle Game")


#Oyuncunun turtle oluşturma
player = turtle.Turtle()
player.shape("turtle")
player.hideturtle()



#skor fonksiyonları için yardımcı kalemleri oluşturma
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()


#Oyun süresi için yardımcı kalem oluşturma
timepen = turtle.Turtle()
timepen.hideturtle()
timepen.penup()


# Zamanı güncelleyen fonksiyon
sure = 30
x_pos1 = 0
y_pos1 = 250

def update_time():
    global sure

    if sure >= 0:
        timepen.clear()
        timepen.goto(x_pos1, y_pos1)
        timepen.write("Süre: {} saniye".format(sure), align="center", font=("monospace", 16))
        sure -= 1
        timepen.getscreen().ontimer(update_time,1000)

    else:
        timepen.color("red")
        timepen.clear()
        timepen.goto(x_pos1, y_pos1)
        timepen.write("Oyun Bitti!", align="center", font=("monospace", 20))
        time.sleep(3)
        turtle.bye()


#skor gösterme fonk.
def show_score():
    x_pos = -40
    y_pos = 280

    pen.color("blue")
    pen.clear()
    pen.goto(x_pos, y_pos)
    pen.write(f"Score: {sayac}", font=("monospace", 16))


sayac = 0

#Skor ekleme fonk.
def add_score(x, y):
    global sayac
    sayac += 1
    show_score()
    turtle.update()



# Oyuncu turtle'ının hareketini ayarlayan fonksiyon

# Yer değiştirip , turtle gösteren fonk.
def show_and_move_turtle():

    x = random.randint(-game_sc.window_width() // 2, game_sc.window_width() // 2)
    y = random.randint(-game_sc.window_height() // 2, game_sc.window_height() // 2)
    player.penup()
    player.goto(x, y)
    player.showturtle()
    game_sc.ontimer(hide_turtle, 1000)

def hide_turtle():
    player.hideturtle()
    game_sc.ontimer(show_and_move_turtle, 1000)



# Ana oyun döngüsü

player.onclick(add_score)
show_score()
update_time()
show_and_move_turtle()


game_sc.mainloop()