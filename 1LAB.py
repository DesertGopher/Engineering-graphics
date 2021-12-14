from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import math
import pylab

# ---------13(1)---------#
pylab.figure(1)

title("Построение графиков функций вар.13")
plt.grid(True)

X1 = []
Y1 = []
for i in range(1, 11):
    a = float(i / 5)
    X1.append(a)
    Y1.append(sin(1 / (sqrt(a))))

X2 = []
Y2 = []
for i in range(1, 11):
    a = float(i / 5)
    X2.append(a)
    Y2.append(cos(1 / (sqrt(a))))

pylab.plot(X1, Y1, 'r-', X2, Y2, 'b-')
pylab.plot(X1, Y1, 'y.', X2, Y2, 'g.')

# ---------14(1)---------#
pylab.figure(2)

title("Построение графиков функций вар.14")
plt.grid(True)

X1 = []
Y1 = []
for i in range(1, 9):
    a = float(i / 2)
    X1.append(a)
    Y1.append(pow(a, 0.3 * (math.pi + 1)))

X2 = []
Y2 = []
for i in range(1, 9):
    a = float(i / 2)
    X2.append(a)
    Y2.append(pow(a, (math.e - 1)))
pylab.plot(X1, Y1, 'r-', X2, Y2, 'b-')
pylab.plot(X1, Y1, 'm.', X2, Y2, 'g.')

# ---------13(2)---------#
pylab.figure(3)

title("Построение графиков функций вар.13")
plt.grid(True)

X1 = []
Y1 = []
for i in range(1, 101):
    a = float(i / 50)
    X1.append(a)
    Y1.append(sin(1 / (sqrt(a))))

X2 = []
Y2 = []
for i in range(1, 101):
    a = float(i / 50)
    X2.append(a)
    Y2.append(cos(1 / (sqrt(a))))
pylab.plot(X1, Y1, 'r-', X2, Y2, 'b-')

# ---------14(2)---------#
pylab.figure(4)

title("Построение графиков функций вар.14")
plt.grid(True)

X1 = []
Y1 = []
for i in range(1, 81):
    a = float(i / 20)
    X1.append(a)
    Y1.append(pow(a, 0.3 * (math.pi + 1)))

X2 = []
Y2 = []
for i in range(1, 81):
    a = float(i / 20)
    X2.append(a)
    Y2.append(pow(a, (math.e - 1)))
pylab.plot(X1, Y1, 'r-', X2, Y2, 'b-')

pylab.figure(5)

title("Синусоида")
plt.grid(True)

X1 = []
Y1 = []
for i in range(-80, 81):
    a = float(i / 20)
    X1.append(a)
    Y1.append(sin(a))

pylab.plot(X1, Y1, 'r-')

pylab.show()
