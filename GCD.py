# Program to find Gretest Common Divisor 
def gcd(num1, num2): 
   while(num2):
       num1, num2 = num2, num1 % num2
   return num1

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

print("The Gretest Common Divisor is ", gcd(int(n1), int(n2)))