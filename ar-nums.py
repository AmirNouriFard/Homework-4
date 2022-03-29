# Program to check Armstrong Number in range (1,10000)
minim = 1
maxim = 10000
for n in range(minim, maxim + 1):
   # order of number
   numlen = len(str(n))
   # initialize sum
   sum = 0
   t = n
   while t > 0:
       divsn = t % 10
       sum += divsn ** numlen
       t //= 10
   if n == sum:
       print(n)
