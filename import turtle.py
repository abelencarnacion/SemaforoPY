import turtle
import time











# Diseño
canvas = turtle.Screen()
canvas.title("SEMAFORO ABEL ENCARNACION")
canvas.bgcolor("BLACK")
canvas.setup(width=600, height=400)

# Creación del semáforo
semaphore = turtle.Turtle()
semaphore .hideturtle()
semaphore .speed(0)
semaphore .penup()
semaphore .goto(0, 100)
semaphore .pendown()
semaphore .pensize(3)

# Dibujo\Formas del semáforo
semaphore .circle(50)
semaphore .penup()
semaphore .goto(0, 70)
semaphore .pendown()
semaphore .begin_fill()
semaphore.circle(20)
semaphore.end_fill()
semaphore.penup()
semaphore.goto(0, 0)
semaphore.pendown()
semaphore.begin_fill()
semaphore.circle(20)
semaphore.end_fill()
semaphore.penup()
semaphore.goto(0, -70)
semaphore.pendown()
semaphore.begin_fill()
semaphore.circle(20)
semaphore.end_fill()

# Función para encender la luz verde
def green_light():
    semaphore.penup()
    semaphore.goto(0, 70)
    semaphore.pendown()
    semaphore.fillcolor("green")
    semaphore.begin_fill()
    semaphore.circle(20)
    semaphore.end_fill()
    time.sleep(3)

# Función para encender la luz amarilla
def yellow_light():
    semaphore.penup()
    semaphore.goto(0, 0)
    semaphore.pendown()
    semaphore.fillcolor("yellow")
    semaphore.begin_fill()
    semaphore.circle(20)
    semaphore.end_fill()
    time.sleep(1)

# Función para encender la luz roja
def red_light():
    semaphore.penup()
    semaphore.goto(0, -70)
    semaphore.pendown()
    semaphore.fillcolor("red")
    semaphore.begin_fill()
    semaphore.circle(20)
    semaphore.end_fill()
    time.sleep(3)

# Ciclo principal del semáforo
while True:
    green_light()
    semaphore.clear()
    yellow_light()
    semaphore.clear()
    red_light()
    semaphore.clear()
