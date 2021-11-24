import math

print('\nWelcome to Factorial Calculator App')

number = int(input('What number would you like to compute the factorial of? : '))

print(f'{number}! = ',end="")
for i in range(1, number):
    print(f'{i}', end="*")
print(f'{number}')    

print(f'\n Here is the result from the math library: \n The Factorial of  {number} : {math.factorial(number)}')

def factorial(number : int):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

result = factorial(number)
print(f'\n Here is the result from my own algorithm: \n The factorial of {number} is : {result}')

#Summary
print("\nIt is shown twice that " + str(number) + "! = " + str(result) + " (with excitement!)")