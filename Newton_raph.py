#Program of Newton Raphson Method for solving equation
#The equation is x^3 - x^2 + 2
def equation( x ):
    return x * x * x - x * x + 2
def func( x ):
    return 3 * x * x - 2 * x
def raphson( x ):
    h = equation(x) / func(x)
    while abs(h) >= 0.0001:
        h = equation(x)/func(x)
        x = x - h  
    print("The value of the root is : ","%.4f"% x)
x0 = -20
raphson(x0)