# Import the math library to use Binet's Formula Method
import sys
# Import the time library to calculate the time of execution of the methods
import time
# Import the math library to use Binet's Formula Method
import math
# Import the matplotlib library to generate the graphs
import matplotlib.pyplot as plt
# Import the NumPy library to use matrix multiplication
import numpy as np
# Import the NumPy library to use matrix power
from numpy.linalg import matrix_power
# Import the prettytable library to generate a table with responses
from prettytable import PrettyTable

sys.setrecursionlimit(10**6) # Fixing maximum recursion depth exceeded error

# Method 1: Using recursion
"""
    Recursive Method:
    This method uses recursive approach to calculate the n-th term of the fibonacci sequence.
    It calculates the n-1 and n-2 term of the sequence and adds them to find the n-th term.
    
    In the recursive method, we have used a recursive function fibonacci_recursive that calculates the n-th term by calling itself to calculate the n-1 and n-2 term and then adds them to find the n-th term.
    This approach has an exponential time complexity, O(2^n), as each term has two sub-problems and the size of the sub-problems is getting reduced by one in each call.

"""
def fib_recursive(n):
    if n == 0 or n == 1: # default cases of the f(1'term) and f(2'nd term)
        return n
    return fib_recursive(n-1) + fib_recursive(n-2) # all the other cases using recursive method

# Method 2: Using iteration
"""
    Iterative Method:
    It starts with 0 and 1 as the first two terms and iteratively calculates the next term
    by adding the previous two terms.
    
    In the iterative method, we have used a loop to calculate the n-th term. We start with 0 and 1 as the first two terms and then iteratively calculate the next term by adding the previous two terms.
    This method uses iterative approach to calculate the n-th term of the fibonacci sequence.
    This approach has a linear time complexity, O(n), as we are iteratively calculating the next term
    """
def fib_iterative(n):
    if n == 0 or n == 1:   # default cases of the f(1'term) and f(2'nd term)
        return n
    a, b = 0, 1
    for i in range(2, n+1): # all the other cases using iterative method
        c = a + b
        a = b
        b = c
    return b


# Method 3: Using a loop
"""
    Loop Method:
    
    Tme complexity of O(n)
     """

def fib_loop(n):
    # Initialize variables to store the previous two terms of the sequence
    prev1 = 0
    prev2 = 1
    # If n is 1 or 2, return the corresponding value
    if n == 1:
        return prev1
    elif n == 2:
        return prev2

    # Initialize a counter to keep track of the current term
    current_term = 3

    # Loop through the sequence, adding the previous two terms to find the next
    while current_term <= n:
        next_term = prev1 + prev2
        prev1 = prev2
        prev2 = next_term
        current_term += 1

    return prev2

# Method 4: Using a formula
""""
    Formula Method:
    
    Formula method may not be as accurate for large values of n as it relies on the approximation of the golden ratio.
    Time complexity of O(1).
"""
def fib_formula(n):
    # Calculate the golden ratio
    golden_ratio = (1 + 5**0.5) / 2
    # Calculate the nth term using the formula
    nth_term = ((golden_ratio ** n) - ((1 - golden_ratio) ** n)) / 5 ** 0.5

    return int(nth_term)

# Method 5: Using Matrix Multiplication
"""
    Matrix Multiplication Method:
     
     As seen from the empirical analysis, the execution time increases as the value of n increases. 
    However, the increase is not very drastic, which shows that the matrix multiplication method is efficient in calculating the nth term of the Fibonacci sequence.
"""

def fib_matrix(n):
    # Define the matrix used in the calculation
    matrix = np.array([[1, 1], [1, 0]])

    # Raise the matrix to the power of n-1
    result = np.linalg.matrix_power(matrix, n - 1)

    # Return the first element of the resulting matrix
    return result[0, 0]


# Method 6: Using Binet's Formula
"""
     Binet's Formula Method:

    The time complexity of Binet's formula is O(1), since it only requires a constant amount of operations to calculate the nth Fibonacci number. This is a significant improvement over other methods, such as the iterative method, which have a time complexity of O(n).
The space complexity of Binet's formula is also O(1), since it only requires a few variables to store intermediate results.
However, Binet's formula is not exact for all inputs, and may produce imprecise results for very large values of n due to rounding errors. For most practical purposes, however, the results are accurate and Binet's formula is a fast and efficient method for calculating the nth Fibonacci number.
    """
def fib_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi ** n - psi ** n) / math.sqrt(5))

#  Extra Method: Using Generators
"""
   Generators Method:
    
    The fib_generator function uses a generator to calculate the nth term of the Fibonacci sequence. Generators allow us to generate values one at a time, as they are required, rather than all at once, which makes them more memory-efficient. In each iteration of the loop, the generator yields the current value of a and then updates a and b as b and a + b, respectively.
"""
def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


n_terms = 30 # Number of terms to calculate
ns=[]
recursive_time = []
iterative_time = []
loop_time = []
formula_time = []
matrix_time = []
binet_time = []



for i in range(n_terms):
    ns.append(i+1)


    start_time = time.time()
    result_recursive = fib_recursive(i)
    fib_recursive(i)
    recursive_time.append(time.time() - start_time)
    time_recursive = time.time() - start_time

    start_time = time.time()
    result_iterative = fib_iterative(i)
    fib_iterative(i)
    iterative_time.append(time.time() - start_time)
    time_iterative = time.time() - start_time

    start_time = time.time()
    result_loop = fib_loop(i)
    fib_loop(i)
    loop_time.append(time.time() - start_time)

    start_time = time.time()
    result_formula = fib_formula(i)
    fib_formula(i)
    formula_time.append(time.time() - start_time)

    start_time = time.time()
    result_matrix = fib_matrix(i)
    fib_matrix(i)
    matrix_time.append(time.time() - start_time)

    start_time = time.time()
    result_binet = fib_binet(i)
    fib_binet(i)
    binet_time.append(time.time() - start_time)




# Plotting the comparison graph
plt.plot(range(n_terms), recursive_time, label='Recursive')
plt.plot(range(n_terms), iterative_time, label='Iterative')
plt.plot(range(n_terms), loop_time, label='Loop')
plt.plot(range(n_terms), formula_time, label='Formula')
plt.plot(range(n_terms), matrix_time, label='Matrix')
plt.plot(range(n_terms), binet_time, label='Binet')
plt.legend()
plt.xlabel('Nth Term')
plt.ylabel('Time (s)')
plt.title('Fibonacci Sequence Calculation Time Comparison')
plt.show()

result_recursive= "%.1f" % result_recursive
result_iterative= "%.1f" % result_iterative
result_loop= "%.1f" % result_loop
result_formula= "%.1f" % result_formula
result_matrix= "%.1f" % result_matrix
result_binet= "%.1f" % result_binet





table = PrettyTable()
table.field_names = ['Method', 'Result', str(ns)]
table.add_row(['Recursive', result_recursive, recursive_time])
table.add_row(['Iterative', result_iterative, iterative_time])
table.add_row(['Loop', result_loop, loop_time])
table.add_row(['Formula', result_formula, formula_time])
table.add_row(['Matrix', result_matrix, matrix_time])
table.add_row(['Binet', result_binet, binet_time])


print(table)
