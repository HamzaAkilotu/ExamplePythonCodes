import turtle
import random

# Properties, Variables
FONT = ("Impact", 30, "bold")
score = 0
game_over = False

# Turtle Screen
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

# Turtle Score Board
score_board = turtle.Turtle()
score_board.color("dark blue")
score_board.hideturtle()
score_board.penup()
height = screen.window_height() / 2
score_board.setpos(x=0, y=height * 0.8)
score_board.write(arg=f"Score={score}", move=False, align="center", font=FONT)

# Turtle Object
turtle_object = turtle.Turtle()
turtle_object.shape("turtle")
turtle_object.shapesize(2, 2)
turtle_object.color("dark green")
turtle_object.penup()

# Count Down
count_down = turtle.Turtle()


def set_count_down(time):
    global game_over
    count_down.color("red")
    count_down.hideturtle()
    count_down.penup()
    height = screen.window_height() / 2
    count_down.setpos(x=0, y=height * 0.7)
    count_down.clear()
    if time > 0:
        count_down.write(arg=f"Time={time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: set_count_down(time - 1), 1000)
    else:
        game_over = True
        count_down.write(arg="GAME OVER", move=False, align="center", font=FONT)


def move_turtle():
    turtle_object.hideturtle()
    if not game_over:
        turtle_object.goto(random.randint(-300, 300), random.randint(-200, 200))
        screen.ontimer(move_turtle, 1500)
    turtle_object.showturtle()


def update_score():
    score_board.clear()
    score_board.write(arg=f"Score={score}", move=False, align="center", font=FONT)


def mouse_click(x, y):
    global score
    if not game_over:
        if turtle_object.distance(x, y) < 20:
            score += 1
            update_score()


screen.onscreenclick(mouse_click)


def start_game():
    move_turtle()
    set_count_down(10)


start_game()
turtle.mainloop()
