import sympy as sp

t = sp.symbols('t')
v = sp.sqrt(4*t**2 - 12*t + 13)

vd = sp.diff(v, t)

lambvd = sp.lambdify(t, vd)

v_abs = sp.sqrt(lambvd(3/2))

print(v_abs)
