# This is a sample Python script.

"""this piece of code below solves any Actual flow for an orifice plate equation using the formula method"""

# ask the user question on

Ao = float(input('enter the value of Ao '))
Do = float(input('enter the value of Do '))
D1 = float(input('enter the value of D1 '))
Cd = float(input('enter the value of Cd '))
g = float(input('enter the value of g '))
h = float(input('enter the value of h '))
Pm = float(input('enter the value of Pm '))
Pf = float(input('enter the value of Ps '))


# the section below for the formulas are broken in parts for simplicity


multi = (Pm/Pf-1)
multi_2 =( 2 * g * h * multi)
multi_3 = 1-(Do/D1)** 4
squt = (multi_2/multi_3)** 0.5
Q = (Ao * Cd * squt)

print('The answer for  Actual flow for an orifice plate is  =',  Q)