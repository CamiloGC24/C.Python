print('\n Welcome to the fibonacci calcuator app.')

number = int(input('\n How many digits of the Fibonacci Sequence would you like to compute: : '))

fib_list = [1,1]

for i in range (number-2):
    new_fibo = fib_list[i] + fib_list[i+1]
    fib_list.append(new_fibo)

print(f'\n The first {number}  numbers of the Fibonacci sequence are: ')
for i in fib_list:
    print(f'\n{i}')

golden_list = list(fib_list)

for i in range(len(fib_list)-1):
    gr = fib_list[i+1]/fib_list[i]
    golden_list.append(gr)

print(f'\n The corresponding Golden Ratio values are: ')
for i in golden_list:
    print(f'\n{i}')

print("The ratio of consecutive Fibonacci terms approaches Phi; 1.618...")