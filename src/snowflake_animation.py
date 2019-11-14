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


def move_snowball(turtle_name, falling_speed=1):
    turtle_name.clear()
    turtle_name.color("snow")
    turtle_name.sety(turtle_name.ycor() - falling_speed)
    turtle_name.dot(turtle_name.size)


def write_headline(turtle, text=""):
    turtle.penup()
    turtle.setposition(0, 150)
    turtle.color("snow")
    turtle.write(text, font=("Sahadeva", 30, "bold"), align="center")
    turtle.hideturtle()


def write_greetings(turtle, text):
    turtle.penup()
    turtle.setposition(-100, -160)
    turtle.color("Alice Blue")
    turtle.write("Sends you", font=("Sahadeva", 15, "bold"), align="right")
    turtle.setposition(-10, -200)
    turtle.color("Gainsboro")
    turtle.write(text, font=("Sahadeva", 25, "bold"), align="right")
    turtle.hideturtle()


def draw():
    screen.setup(width, height)
    screen.bgpic(backgroung_picture)
    screen.title(headline_text)

    # Write text
    screen.tracer(0)
    headline = turtle.Turtle()
    greetings = turtle.Turtle()
    write_headline(headline, headline_text)
    write_greetings(greetings, greetings_text)

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


backgroung_picture = "img/reduced_icy_pic.gif"
headline_text = "Frosty Greetings"
greetings_text = "Christine Winter"

# Set up screen
width = 600
height = 450
screen = turtle.Screen()
file_name = "res/winter_greetings{0:03d}.eps"

draw()

