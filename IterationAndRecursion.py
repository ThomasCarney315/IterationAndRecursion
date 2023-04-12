# Thomas Careny
# CIS 261 - Object-Oriented Computer Programming
# Iterative and Recursive Functionality

def iterative_factorial(n):
    factorial = 1
    for i in range(1 ,n + 1):
        factorial *= i
    return factorial

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def main():
    num_list = [0,5,10,25,50,100]
    print('Results for iteratve factorial function')
    for num in num_list:
        print(f'{num}! = {iterative_factorial(num)}')
    print('Results for recursive factorial function')
    for num in num_list:
        print(f'{num}! = {recursive_factorial(num)}')

if __name__ == "__main__":
    main()
