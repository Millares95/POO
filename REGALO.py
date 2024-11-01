import turtle
import random

# Configuración de la pantalla
pantalla = turtle.Screen()
pantalla.title("Muñequita Despeinada")
pantalla.bgcolor("white")

# Configuración de la tortuga para dibujar
muñeca = turtle.Turtle()
muñeca.speed(2)
muñeca.width(2)

# Dibuja la cabeza
muñeca.penup()
muñeca.goto(0, -50)
muñeca.pendown()
muñeca.circle(50)

# Dibuja los ojos
muñeca.penup()
muñeca.goto(-20, 20)
muñeca.pendown()
muñeca.dot(10)

muñeca.penup()
muñeca.goto(20, 20)
muñeca.pendown()
muñeca.dot(10)

# Dibuja la boca
muñeca.penup()
muñeca.goto(-15, -10)
muñeca.pendown()
muñeca.right(90)
muñeca.circle(15, 180)

# Dibuja el cabello despeinado
for i in range(25):
    muñeca.penup()
    muñeca.goto(0, 50)  # punto de origen para el cabello
    muñeca.setheading(random.randint(0, 360))  # dirección aleatoria
    muñeca.pendown()
    muñeca.forward(random.randint(40, 70))  # largo aleatorio del cabello

# Dibuja el cuerpo
muñeca.penup()
muñeca.goto(0, -50)
muñeca.setheading(-90)
muñeca.pendown()
muñeca.forward(100)

# Dibuja los brazos
muñeca.penup()
muñeca.goto(0, -70)
muñeca.setheading(180)
muñeca.pendown()
muñeca.forward(60)

muñeca.penup()
muñeca.goto(0, -70)
muñeca.setheading(0)
muñeca.pendown()
muñeca.forward(60)

# Dibuja las piernas
muñeca.penup()
muñeca.goto(0, -150)
muñeca.setheading(-45)
muñeca.pendown()
muñeca.forward(60)

muñeca.penup()
muñeca.goto(0, -150)
muñeca.setheading(-135)
muñeca.pendown()
muñeca.forward(60)

# Finaliza el dibujo
muñeca.hideturtle()
pantalla.mainloop()
