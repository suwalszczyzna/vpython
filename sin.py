from vpython import *


def get_int():
    while True:
        try:
            return int(input("Podaj x_min: "))
        except ValueError:
            print("Musisz podać liczbę całkowitą")


x_min = get_int()
x_max = get_int()

curve = gcurve(color=color.red)  # a graphics curve
for x in arange(x_min, x_max + 0.1, 0.1):  # x goes from 0 to 8
    curve.plot(x, sin(x))
