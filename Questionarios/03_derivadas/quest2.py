import sympy as sp

t = sp.symbols('t')
r_x = 4.9 * sp.cos(9 * t)
r_y = 4.9 * sp.sin(9 * t)
r_z = 7.1 * t**2

v_x = sp.diff(r_x, t)
v_y = sp.diff(r_y, t)
v_z = sp.diff(r_z, t)

lambv_x = sp.lambdify(t, v_x)
lambv_y = sp.lambdify(t, v_y)
lambv_z = sp.lambdify(t, v_z)

v_abs = sp.sqrt(lambv_x(1.8)**2 + lambv_y(1.8)**2 + lambv_z(1.8)**2)

print("%.1f"%v_abs)
