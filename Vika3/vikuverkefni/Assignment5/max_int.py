
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

# 1 - Take the input number from the user (integer, int)
# 2 - Keep taking input from the user (integer, int)
# 3 - See if the new input is larger or smaller than the last input
# 4 - If the new input is larger than the last one assign it to the variable max_int
# 5 - If the user inputs a negative number (integer, int) stop taking in inputs
# 6 - Output the highest input number that the user inputted
# 7 - Program ends

# Program that outputs the highest number that the user inputs
last_input_num_int = 0
while num_int > 0:
    last_input_num_int = num_int
    num_int = int(input("Input a number: "))
    if num_int > last_input_num_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line
