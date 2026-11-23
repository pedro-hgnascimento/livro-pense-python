# Exercícios do capítulo 4, no livro estão meio 'fora de ordem'.
import turtle
from math import pi

def square(t, length):
    """Desenha um quadrado com a tartaruga t."""
    for i in range(4):
        t.fd(length)
        t.lt(90)

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

def circle(t, r):
    """Desenha um círculo com raio r usando a função arc."""
    arc(t, r, 360)

def arc(t, r, angle):
    """Desenha um arco com raio r e ângulo angle usando a função polyline."""
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, step_length, n, step_angle)



def main():
    bob = turtle.Turtle()
    # square(bob, 100)
    # square(bob, 50)
    # square(bob, 25)
    # square(bob, 200)
    # square(bob, 400)
    # polyline(bob, 50, 7)
    # polyline(bob, 60, 8)
    # polyline(bob, 70, 9)
    # polyline(bob, 80, 10)
    # circle(bob, 50)
    # circle(bob, 100)
    # circle(bob, 150)
    # arc(bob, 100, 90)
    # arc(bob, 100, 180) 
    arc(bob, 100, 270)
    # arc(bob, 100, 340)

    turtle.mainloop()

main()