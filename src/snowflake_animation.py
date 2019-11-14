#!/bin/python3
import turtle
import random
import time


def place_snowball(screen_width, screen_height, snowball_size, snowball):
    snowball.color("snow")
    snowball.penup()
    snowball.setposition(random.randint(-2 * screen_width, screen_width / 2), screen_height / 2)
    snowball.hideturtle()
    snowball.size = random.randint(*snowball_size)
    return snowball


def move_snowball(snowball, falling_speed=1):
    snowball.clear()
    snowball.color("snow")
    snowball.sety(snowball.ycor() - falling_speed)
    snowball.dot(snowball.size)


def write_text(turtle, text="", pos=(0, 0), color="snow", font=("Sahadeva", 30, "bold"), align="center"):
    turtle.penup()
    turtle.setposition(pos[0], pos[1])
    turtle.color(color)
    turtle.write(text, font=font, align=align)
    turtle.hideturtle()


def draw():
    screen.setup(width, height)
    screen.bgpic(background_picture)
    screen.title(headline_text)

    # Write text
    screen.tracer(0)

    headline = turtle.Turtle()
    write_text(headline, headline_text, pos=(0, 150), color="snow", font=("Sahadeva", 30, "bold"), align="center")

    greetings = turtle.Turtle()

    write_text(greetings, greetings_text, pos=(-100, -160), color="Alice Blue", font=("Sahadeva", 15, "bold"),
               align="right")
    write_text(greetings, signature_text, pos=(0, -200), color="Gainsboro", font=("Sahadeva", 25, "bold"),
               align="right")

    # Settings for snowballs
    snowball_rate = 1, 3
    snowball_size = 5, 15
    list_of_snowballs = []

    snowball_time_delay = 0
    start_time = time.time()
    absolute_start_time = start_time

    # Draw snowballs until exit signal
    keep_drawing = True

    while keep_drawing:
        if time.time() - start_time > snowball_time_delay:
            list_of_snowballs.append(place_snowball(width, height, snowball_size, turtle.Turtle()))
            start_time = time.time()
            snowball_time_delay = random.randint(*snowball_rate) / 50

        for snowball in list_of_snowballs:
            move_snowball(snowball, falling_speed=.9)
            if snowball.ycor() < -height / 2:
                snowball.clear()
                place_snowball(width, height, snowball_size, snowball)

        screen.update()

        if time.time() - absolute_start_time > 30:
            keep_drawing = False
            screen.bye()


background_picture = "img/reduced_icy_pic.gif"
headline_text = "Frosty Greetings"
greetings_text = "Sends you"
signature_text = "Christine Winter"

# Set up screen
width = 600
height = 450
screen = turtle.Screen()
file_name = "res/winter_greetings{0:03d}.eps"

draw()
