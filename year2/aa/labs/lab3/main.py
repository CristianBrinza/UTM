# ▒▄▀▄▒▄▀▄  c. AA | FAF | FCIM | UTM | Spring 2023
# ░█▀█░█▀█  FAF-212 Cristian Brinza lab3

# Importing the required libraries for this script

# Importing the required libraries for this script
import time  # Library for time-related functions
import matplotlib.pyplot as plt  # Library for data visualization
from prettytable import PrettyTable  # Library for table data visualization


# This is a function that implements the Sieve of Eratosthenes algorithm to find all prime numbers up to n
def eratosthenes_sieve_1(n):
    # Create a list c that will hold boolean values indicating if each number up to n is prime
    c = [True for i in range(n+1)]
    # 1 is not prime, so set it to False
    c[1] = False
    # Start at 2, the first prime number
    i = 2
    # Iterate through each number up to n
    while i <= n:
        # If the current number i is prime, mark all multiples of i as not prime
        if c[i] == True:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
            # Move to the next number
        i += 1
    # Create a list primes to hold all prime numbers found
    primes = []

    # Iterate through each number up to n
    for i in range(2, n+1):
        # If the current number is prime, add it to the list of primes
        if c[i] == True:
            primes.append(i)
    
    # Return the list of primes
    return primes

# This is an implementation of the Sieve of Eratosthenes algorithm to find all prime numbers up to n.
def eratosthenes_sieve_2(n):
    # create a boolean array c, where c[i] is True if i is prime, and False otherwise
    c = [True for i in range(n+1)]
    # 1 is not considered prime, so set it to False
    c[1] = False
    # start at 2, the first prime number
    i = 2
    while i <= n:
        # mark all multiples of i as composite (not prime)
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        # move to the next number
        i += 1
    # initialize empty list to store prime numbers
    primes = []
    for i in range(2, n+1):
        if c[i] == True: # if c[i] is True, then i is prime, so append it to the list of primes
            primes.append(i)
    # return list of prime numbers up to n
    return primes

# This is a function that uses the Sieve of Eratosthenes algorithm to find all prime numbers up to n
def eratosthenes_sieve_3(n):
    # Create a list of booleans to represent whether a number is prime or not
    c = [True for i in range(n+1)]
    # Set 1 to be a non-prime number
    c[1] = False
    # Start with the first prime number, 2
    i = 2
    # Loop through all numbers up to n
    while i <= n:
        # If the current number is prime
        if c[i] == True:
            # Mark all multiples of i as non-prime
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1
    # Create a list of all prime numbers up to n
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)
    # Return the list of prime numbers
    return primes

# This is a function that uses the Sieve of Eratosthenes algorithm to find all prime numbers up to n
def erastosthenes_sieve_4(n):
    # Create a list of booleans to represent whether a number is prime or not
    c = [True for i in range(n+1)]
    # Set 1 to be a non-prime number
    c[1] = False
    # Start with the first prime number, 2
    i = 2
    # Loop through all numbers up to n
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    # Create a list of all prime numbers up to n
    primes = []
    for i in range(2, n+1):
        # If the current number is prime
        if c[i] == True:
            # Mark all multiples of i as non-prime
            primes.append(i)
    # Return the list of prime numbers     
    return primes

#This is an implementation of the Sieve of Eratosthenes algorithm to find prime numbers up to n
def eratosthenes_sieve_5(n):
    # Create a boolean list to keep track of which numbers are prime
    c = [True for i in range(n+1)]
    # 1 is not a prime number, so mark it as False
    c[1] = False

    # Loop over all numbers from 2 to n
    i = 2
    while i <= n:
        # Loop over all numbers from 2 to the square root of i
        j = 2
        while j <= i**0.5:
            # If i is divisible by j, mark it as not prime
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    # Collect all prime numbers
    primes = []
    for i in range(2, n+1):
        if c[i] == True:
            primes.append(i)

    return primes


# Defining the input
input = [1000, 10000, 20000]

# Creating an empty list to store the results
results = []
for i in input:
    start = time.time()
    eratosthenes_sieve_1(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    eratosthenes_sieve_2(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    eratosthenes_sieve_3(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    erastosthenes_sieve_4(i)
    end = time.time()
    results.append(end - start)
    start = time.time()
    eratosthenes_sieve_5(i)
    end = time.time()
    results.append(end - start)


results_1 = results[0:5]
results_2 = results[5:10]
results_3 = results[10:15]

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[0], results_2[0], results_3[0]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[1], results_2[1], results_3[1]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[2], results_2[2], results_3[2]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[3], results_2[3], results_3[3]])
print(table)

table = PrettyTable()
table.field_names = ["1000", "10000", "20000"]
table.add_row([results_1[4], results_2[4], results_3[4]])
print(table)


plt.figure(1)
plt.bar(['Algorithm 1', 'Algorithm 2', 'Algorithm 3',
        'Algorithm 4', 'Algorithm 5'], results_1, color='green')
plt.title('Computing prime numbers up to 1000')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

plt.figure(2)
plt.bar(['Algorithm 1', 'Algorithm 2', 'Algorithm 3',
        'Algorithm 4', 'Algorithm 5'], results_2, color='blue')
plt.title('Computing prime numbers up to 10000 ')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

plt.figure(3)
plt.bar(['Algorithm 1', 'Algorithm 2', 'Algorithm 3',
        'Algorithm 4', 'Algorithm 5'], results_3, color='red')
plt.title('Computing prime numbers up to 20000')
plt.xlabel('Algorithms')
plt.ylabel('Time in seconds')

plt.show()