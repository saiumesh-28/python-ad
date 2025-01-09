# 1. Program to print numbers from 1 to n and calculate the sum using for and while loops
n = int(input("Enter a number: "))
a = 0
for i in range(1, n + 1):
    print(i)
b = 0
i = 1
while i <= n:
    print(i)
    b += i
    i += 1
print("Sum using while loop: ",b)


# 2. Program with a user-defined function calculate_square
def calculate_square(n):
    return n **2
n = int(input("Enter a positive integer: "))
a = calculate_square(n)
print("The square of", n, "is:", a)
