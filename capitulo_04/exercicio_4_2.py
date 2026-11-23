# Desenhando flores com a tartaruga

import turtle
from math import pi

def polyline(t, length, n, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turle.
    """
    
    for i in range(n):
        t.fd(length)
        t.lt(angle) # Fórmula padrão para cálculo do ângulo interno de um polígono regular.

def polygon(t, length, n):
    """Desenha um polígono regular com n lados."""
    angle = 360.0 / n
    polyline(t, length, n, angle)

def arc(t, r, angle):
    """Desenha um arco com raio r e ângulo angle usando a função polyline."""
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, step_length, n, step_angle)

def flower(t, length, n):
    """Desenha uma flor com n pétalas."""
    for i in range(n):
        arc(t, length, 180)  # Desenha um arco como pétala
        t.lt(90.0 - 90.0 / n)  # Gira a tartaruga para a próxima pétala

def main():
    bob = turtle.Turtle()
    flower(bob, 50, 9)  # Desenha uma flor com 6 pétalas e raio de 100

    turtle.mainloop()   

main()