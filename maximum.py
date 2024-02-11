import sympy as sym
x = sym.Symbol('x')
a = input()
limit = sym.diff(eval(a), x, 1)
ans = sym.solveset(limit, x)
print(str(ans)[1:-1])
