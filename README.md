# 3-Line-Gradient-Descent
Probably the shortest gradient descent algorithm ever in existence

```py
def f(x):global y;return eval(y)
x=float(input('x = '));y=input('y = ')
for iter in range(100):x-=(f(x+0.001)-f(x))/0.001*0.1;print('\nx =',x,'\ny =',f(x))
  ```
