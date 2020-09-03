# 1. Skrifað út fyrstu n1 >= 2 tölurnar í Fibonacci runu (ein tala í hverri línu).
# 2. Skrifað út allar "abundant" tölur á bilinu 1 upp í n2 (ein tala í hverri línu),

# Ask the user if he wants to find fibonacci numbers or abundant numbers or both

print("Would you like to see fibonacci numbers, abundant numbers or both?")
question_str = str(input("Input |f| for fibonacchi numbers, |a| for abundant numbers or both |b| for both"))

# Fibonachi
    # 1 - Set up variables for num_one_int and num_two_int
    # 2 - Program an for loop that outputs the first n numbers in the fibonacci sequence where n is an input from the user
if question_str == f or question_str == b:
    n_fibo_int = int(input("Input the lenght of the sequence: "))
    num_one_int = 0
    num_two_int = 1
    num_three_int = 0
    print("Here are the first", n_fibo_int, "numbers in the fibonacci sequence")
    print("________________________________________________________")
    for i in range(0, n_fibo_int+1):
        # Print the first 2 numbers as they are 0, 1 always
        if i < 2:
            print(i)
        if i > 2:
            num_three_int = num_one_int + num_two_int
            num_one_int = num_two_int
            num_two_int = num_three_int
            print(num_three_int)

# Abundant numbers

# 1 - Find all the dividers of a numbers and sum them up
# 2 - If the sum of the diveders of a given number is larger than the number it self it is abundant
# 3 - Set up a for loop that checks every number from 1 to n numbers where n is an input from the user
# 4 - Output all abundant numbers from 1 to n

if question_str == a or question_str == b:
    n_abundant_int = int(input("Set the range to check for abundant numbers from 1 to: "))

    print("Abundant numbers in the range of 1 to", n_abundant_int)

    sum_divisor = 0

    for i in range(1, n_abundant_int+1):
        for j in range(1, i):
            if i % j == 0:
                sum_divisor += j
        if sum_divisor > i:
            print(i)
            sum_divisor = 0
        sum_divisor = 0