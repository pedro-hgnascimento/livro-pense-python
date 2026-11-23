# Resolvido o problema!! Antes de importar o turtle se certificar que o tkinter está instalado.

import turtle
bob = turtle.Turtle()
print(bob)

for i in range(4):
    bob.forward(100)
    bob.left(90)

turtle.mainloop()
