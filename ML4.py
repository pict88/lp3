def f(x):
    return (x + 3)**2

x = 2
lr = 0.1

for i in range(50):
    grad=2*(x+3)
    x = x - lr * grad

print("Local Minimum:", x)
print("Minimum Value:", f(x))


def f(x):
    return (x + 3)**2

def grad(x):
    h = 0.0001
    return (f(x+h) - f(x)) / h

x = 2
lr = 0.1

for i in range(50):
    x = x - lr * grad(x)

print("Local Minimum:", x)
print("Minimum Value:", f(x))
