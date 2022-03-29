#Exercise 34 - Page 155 from pythonbook
#write a Python program that allows the user to enter exactly twenty floating-point values.
#The program then prints the sum, average (arithmetic mean), maximum, and minimum of the values entered
count = 0
sum = 0.0
number = 1
print("Input 20 float values to calculate their sum and average")
while count<21:
	number = float(input(""))
	sum = sum + number
	count += 1

print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
