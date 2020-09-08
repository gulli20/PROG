question_str = str(input("Input f|a|b (fibonacci, abundant or both): "))

# Fibonachi
    # 1 - Ask the user the lenght 'n' of the fibonacci sequence.
    # 2 - Program a for loop that outputs the first 'n' numbers in the fibonacci sequence.
    # 3 - The formula for the fibonacci sequence is the sum of the 2 numbers before the next number is the next number in the sequence (num_one + num_two = next_num) and it always starts with 1, 2.

if question_str == 'f' or question_str == 'b':
    
    n_fibo_int = int(input("Input the length of the sequence: "))
    num_one_int = 0
    num_two_int = 1
    num_next_int = 0
    print("Fibonacci Sequence:")
    print("-------------------")
    for i in range(0, n_fibo_int+1):
        # Print the first 2 numbers as they are always 0, 1
        if i < 2:
            print(i)
        if i > 2:
            num_next_int = num_one_int + num_two_int
            num_one_int = num_two_int
            num_two_int = num_next_int
            print(num_next_int)

# Abundant numbers
    # 1 - To find a abundant number: if the sum of all divisors (that leave no remainders) of a given number is larger than the number it is abundant
    # 2 - Find all the divisors of a number and sum them up
    # 3 - Program a for loop that checks every number from '1 to n', if it is an abundant number, where 'n' is an input from the user
    # 4 - Output all abundant numbers from '1 to n'

if question_str == 'a' or question_str == 'b':

    n_abundant_int = int(input("Input the max number to check: "))
    print("Abundant numbers:")
    print("-----------------")
    sum_divisor = 0

    for i in range(1, n_abundant_int+1):
        for j in range(1, i):
            if i % j == 0:
                sum_divisor += j
        if sum_divisor > i:
            print(i)
            sum_divisor = 0
        sum_divisor = 0