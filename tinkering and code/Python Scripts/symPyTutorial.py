import sympy
bruh = sympy.sqrt(3)
print(bruh)

print(sympy.sqrt(8))
print(" ")

from sympy import symbols

x, y = symbols('x, y')
expression = x + 2 * y

expression = expression + 1
print(expression)
print(expression - x)

print("")

#print(x*expression*y*y)

#print("")

from sympy import expand, factor
#expanded version
expandedExpression = expand(x*expression)
print(expandedExpression)
print("")
#factored version
print(factor(expandedExpression))

print("")
from sympy import *
x, t, z, nu = symbols('x t z nu')

init_printing(use_unicode=True)

bruh = diff(sin(x) * exp(x), x)
print(bruh)

print('')

print(integrate(exp(x)*sin(x) + exp(x)*cos(x), x)



#eigenvalues

print(Matrix([[1, 2], [2, 2]]).eigenvalues())





