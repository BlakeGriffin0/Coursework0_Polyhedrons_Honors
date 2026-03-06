#Author - Blake Griffin | Class - MW 1:30 | January 16, 2026
#Polyhedrons Homework 1

import math as m
print ("Welcome to HW-1H-Polyhedrons.") 
print ("Solution by Blake Griffin.")
print ("Shape 1: Could you please provide the Length of the edge of the Tetrahedron? I will need this to calculate the surface area, volume, radius of the circumscribed sphere, and mass constructed of various materials.")
while True:
    a = input("Enter a numeric value: ")
    try:
        a = float(a)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
print (f"Great, you entered {a} successfully! Calculating...")
b = m.pow(a, 2) * m.sqrt(3)
b = round(float(b), 2)
print (f"The area of the Tetrahedron is: {b}.")
z = m.pow(a, 3) * m.sqrt(2) / 12
z = round(float(z), 2)
print (f"The volume of the Tetrahedron is: {z}.")
sphere1 = round(a * (m.sqrt(6) / 4), 2)
print (f"The radius of the circumscribed sphere for the Tetrahedron is: {sphere1}.")
density0 = float(2.70) #g/cm^3
density1 = float(7.87) #g/cm^3
density2 = float(19.05) #g/cm^3
mass0 = round(float(density0 * z), 2)
mass1 = round(float(density1 * z), 2)
mass2 = round(float(density2 * z), 2)
print (f"The mass of the Tetrahedron constructed of Aluminum is: {mass0}g/cm^3, or {mass1}g/cm^3 made of Iron, and {mass2}g/cm^3 wben made of Uranium.")
print (" ")
print("Shape 2: Could you please provide the Length of the edge of the Cube?")
while True:
    c = input("Enter a numeric value: ")
    try:
        c = float(c)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
c = float(c)
d = m.pow(c, 2) * 6
d = round(float(d), 2)
print (f"The area of the Cube is: {d}.")
e = m.pow(c, 3)
e = round(float(e), 2)
print (f"The volume of the Cube is: {e}.")
sphere0 = round(c * (m.sqrt(3) / 2), 2)
print (f"The radius of the circumscribed sphere for a cube is: {sphere0}.")
mass3 = float(density0 * e)
mass4 = float(density1 * e)
mass5 = float(density2 * e)
mass3 = round(float(mass3), 2)
mass4 = round(float(mass4), 2)
mass5 = round(float(mass5), 2)
print (f"The mass of the cube constructed of Aluminum is: {mass3}g/cm^3, or {mass4}g/cm^3 made of Iron, and {mass5}g/cm^3 wben made of Uranium.")
print (" ")
print("Shape 3: Now, provide the length of the edge of the Octahedron.")
while True:
    g = input("Enter a numeric value: ")
    try:
        g = float(g)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
g = float(g)
h = m.pow(g, 2) * 2 * m.sqrt(3)
h = round(float(h), 2)
print(f"The area of the Octahedron is: {h}.")
I = float((m.pow(g, 3) * m.sqrt(2) / 3))
I = round((I), 2)
print(f"The volume of the Octahedron is: {I}.")
sphere2 = round(g * (m.sqrt(2) / 2), 2)
print (f"The radius of the circimscribed sphere for the Octahedron is: {sphere2}.")
mass6 = float(density0 * I)
mass7 = float(density1 * I)
mass8 = float(density2 * I)
mass6 = round(float(mass6), 2)
mass7 = round(float(mass7), 2)
mass8 = round(float(mass8), 2)
print (f"The mass of the octahedron constructed of Aluminum is: {mass6}g/cm^3, or {mass7}g/cm^3 made of Iron, and {mass8}g/cm^3 wben made of Uranium.")
print(" ")
print("Now, please enter the length of the edge of the Dodecahedron.")
while True:
    n = input("Enter a numeric value: ")
    try:
        n = float(n)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
n = float(n)
M = (m.pow(float(n), 2) * 3 * m.sqrt(25 + 10 * m.sqrt(5)))
M = round(float(M), 2)
print(f"The area of the Dodecahedron is: {M}.")
p = (m.pow(float(n), 3) * (15 + 7 * m.sqrt(5)) / 4)
p = round(float(p), 2)
print(f"The volume of the Dodecahedron is: {p}.")
q = round(float(n) * 1.401258538, 2)
print (f"The radius of the circumscribed sphere of the Dodecahedron is: {q}.") 
mass9 = float(density0 * p)
mass10 = float(density1 * p)
mass11 = float(density2 * p)
mass9 = round(float(mass9), 2)
mass10 = round(float(mass10), 2)
mass11 = round(float(mass11), 2)
print (f"The mass of the dodecahedron constructed of Aluminum is: {mass9}g/cm^3, or {mass10}g/cm^3 made of Iron, and {mass11}g/cm^3 wben made of Uranium.")
print(" ")
print ("Last, enter the length of the edge of the Icosahedron and I will calculate the results for you.")
while True:
    t = input("Enter a numeric value: ")
    try:
        t = float(t)
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
t = float(t)
u = (m.pow(float(t), 2)) * 5 * m.sqrt(3)
u = round(float(u), 2)
print (f"The area of the Icosahedron is: {u}")
v = (m.pow(float(t), 3)) * (15 + (15 + (5 * m.sqrt(5)))) / 12
v = round(float(v), 2)
print (f"The volume of the Icosahedron is: {v}")
w = 0.9510565163 * t
w = round(w, 2)
print (f"THe radius of the circumscribed sphere of the Icosahedron is: {w}.")
mass12 = float(density0 * v)
mass13 = float(density1 * v)
mass14 = float(density2 * v)
mass12 = round(float(mass12), 2)
mass13 = round(float(mass13), 2)
mass14 = round(float(mass14), 2)
print (f"The mass of the icosahedron constructed of Aluminum is: {mass12}g/cm^3, or {mass13}g/cm^3 made of Iron, and {mass14}g/cm^3 wben made of Uranium.")
