import sympy as sp
import math

print("Sympy sqrt of 2: ")
sp.pprint(sp.sqrt(2))
print(f"Python native math sqrt of 2: \n{math.sqrt(2)}")

# Creating symbols
x, y, z = sp.symbols("x, y, z")
print(x)
2*x + 5
print(f"2*x+x-5 is automatically simplified: {2*x + x - 5}")
# Sine and Cosine
print("How the terminal represents sine, cosine, and exponents: ")
sp.pprint(sp.sin(x)**2 + sp.cos(x)**2)
print("Divisor representation in the terminal: ")
sp.pprint(2*x/6)
print("Paranthesis representation in the terminal: ")
paren_expr = x*(x+2)
sp.pprint(paren_expr)
# does not change the original expr, can also say sp.expand(paren_expr)
sp.pprint(paren_expr.expand()) 

# Define multiple symbols at once, use either space or comma as delim
sp.symbols("s t")
sp.pprint(sp.symbols("s t"))
print(type(sp.symbols("s t")))
# Also can define with tuple unpacking
s,t = sp.symbols("s,t")
polynomial = t*(s+2)*(t-3)
sp.pprint(polynomial)
print("Expanded polynomial: ")
sp.pprint(polynomial.expand())
# Factor polynomials
expr_to_factor = x**2 + 2*x - 15
print("Before factoring: ")
sp.pprint(expr_to_factor)
print("After factoring: ")
sp.pprint(expr_to_factor.factor())
# Create many symbols
x_v = sp.symbols("x0:10")
print("Create multiple symbols: ")
sp.pprint(x_v)
# Access via a list like format
print("Access symbols in a list like format: ")
ex = x_v[0]**2 * x_v[1] * x_v[2] + x_v[0] * x_v[1] * x_v[2]
sp.pprint(ex)
print("Above expression factored: ")
sp.pprint(ex.factor())
# Numerical Typing
cube_root = x ** (sp.Integer(1) / sp.Integer(3)) 
sp.pprint(cube_root)
print("Multiplied by ^ 1/5: ")
sp.pprint(cube_root ** (sp.Integer(1) / sp.Integer(5)))
# Rational Numbers (a fraction of two integers)
rational = sp.Rational(1,3)
sp.pprint(rational)
sp.pprint(x**rational)
# Constants and functions
sp.pprint(sp.pi) # pi
sp.pprint(sp.E) # e
sp.pprint(sp.oo) # infinity
sp.pprint(sp.I) # imaginary unit
sp.pprint(sp.exp(x)) # exponential function
sp.pprint(sp.exp(sp.pi * sp.I)) # Euler's identity
sp.pprint(sp.log(x)) # Naturual Logarithm Function 
sp.pprint(sp.sin(x) + sp.cos(x) + sp.tan(x)) # Trigonometric functions 
# Defining Equations
eq = sp.Eq(x**2, 5)
print("Define Equation x^2=5: ")
sp.pprint(eq)
# Solve Set
print("Then solve it: ")
sp.pprint(sp.solveset(eq, x)) # specifying x means solve for x
print(f"Type of set: {type(sp.solveset(eq))}")
# Extracting the solution in a list
print("Extracted list of solutions, first element shown: ")
sp.pprint(list(sp.solveset(eq, x))[0])
# Sine and Cosine
eq2 = sp.Eq(sp.cos(x)-sp.sin(x), 0)
sp.pprint(sp.solveset(eq2))
sp.pprint(type(sp.solveset(eq2)))
# A nonsolvable equation
eq3 = sp.Eq(sp.cos(x), x)
print("Equation not symbolically solvable: ")
sp.pprint(eq3)
sp.pprint(sp.solveset(eq3))
sp.pprint(type(sp.solveset(eq3)))
# Some example problems
exp4 = -(2*x**2*y)*(-x*y**4)
# Simplifies automatically 
sp.pprint(exp4)
exp5 = 2*x*(x-5)
sp.pprint(exp5)