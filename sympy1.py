import sympy as sp
import re
from sympy import sympify
from sympy.interactive import printing
printing.init_printing(use_latex=True)

#creating independent variables a,b,d,x
a,b,d,x = sp.symbols("a b d x")

#inputting the equation
inp = input("Enter the Equation(solving for x, other variables are a,b,d): ")
inp = inp.replace('=',',')

#creating equation
exp = sympify(inp)

print(sp.solve(exp,x))