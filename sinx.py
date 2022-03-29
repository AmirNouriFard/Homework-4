pi = 3.1415926535897932384626433832795028841971  # Value of  pi
def Factorial(n):  # Factorial Function
    if n == 1 or n == 0:
        return 1
    else:
        return n * Factorial(n - 1)

def sin(x):  # Taylor Expansion of sinx
    k = 0
    sinx = 0
    while x >= pi:
        x -= pi
    if pi > x > pi / 2:
        x = pi - x
    while k < 15:
        sinx += (-1)**k * x**(2*k + 1) / Factorial(2*k + 1)
        k += 1
    return sinx
