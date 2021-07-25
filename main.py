def optimize(f, x, rate=0.1): return x - (f(x + 0.001) - f(x)) / 0.001 * rate
def f(x): global y; return eval(y)
x = float(input('x = ')); y = input('y = ')
for iter in range(100):
	x = optimize(f, x); print('\nx =', x, '\ny =', f(x))
