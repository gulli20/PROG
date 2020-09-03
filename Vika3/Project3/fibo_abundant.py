print("Would you like to see fibonacci numbers, abundant numbers or both?")
question_str = str(input("Input |f| for fibonacchi numbers, |a| for abundant numbers or both |b| for both: "))

while_value = 0

while while_value != 1:
    if question_str != 'a' or question_str != 'f' or question_str != 'b':
        print("I'm sorry, your input is invalid, please try again")
    question_str = str(input("Input |f| for fibonacchi numbers, |a| for abundant numbers or both |b| for both: "))
    if question_str == 'f' or question_str == 'a' or question_str == 'b':
        while_value = 1


print()
# Fibonachi

    # 1 - Program variables for the for loop
    # 2 - Ask the user for the lenght of the fibonacci sequence the user wants
    # 3 - Program a for loop that outputs the first n numbers in the fibonacci sequence where n is the input from the user
    # 4 - The formula for the sequence is the sum of the 2 numbers before the next number is the next number in the sequence

if question_str == 'f' or question_str == 'b':
    
    n_fibo_int = int(input("Input the lenght of the sequence: "))
    num_one_int = 0
    num_two_int = 1
    num_next_int = 0
    print("Here are the first", n_fibo_int, "numbers in the fibonacci sequence:")
    print("_")
    for i in range(0, n_fibo_int+1):
        # Print the first 2 numbers as they are always 0, 1
        if i < 2:
            print(i)
        if i > 2:
            num_next_int = num_one_int + num_two_int
            num_one_int = num_two_int
            num_two_int = num_next_int
            print(num_next_int)
print()

# Abundant numbers

    # 1 - Find all the divisors of a number and sum them up
    # 2 - If the sum of the divisors of a given number is larger than the number it self it is an abundant number
    # 3 - Program a for loop that checks every number from 1 to n if it is an abundant number, where n is an input from the user
    # 4 - Output all abundant numbers from 1 to n

if question_str == 'a' or question_str == 'b':

    n_abundant_int = int(input("Set the range to check for abundant numbers from 1 to: "))
    print("Abundant numbers in the range of 1 to", n_abundant_int, ":")
    print("_")
    sum_divisor = 0

    for i in range(1, n_abundant_int+1):
        for j in range(1, i):
            if i % j == 0:
                sum_divisor += j
        if sum_divisor > i:
            print(i)
            sum_divisor = 0
        sum_divisor = 0

print()
restart_str = str(input("Would you like to go again? (y/n): "))

if restart_str == 'n':
    while_value = 0
    continue
