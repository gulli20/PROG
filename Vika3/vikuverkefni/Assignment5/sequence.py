n = int(input("Enter the length of the sequence: ")) # Do not change this line

# 1 - Take the integer(int) n as an input from the user
# 2 - The sequence is the sum of last three numbers in the sequnce
# 3 - The sequence looks like 1, 2, 3, 6 , 11
# 4 - Output the first n(input) numbers of the squence
# 5 - Program ends

num_one = 1
num_two = 2
num_three = 3
num_four = 0
# Print out the first 3 in the sequence
for i in range(1, n):
    if i == 4:
        break
    print(i)
# Print out the remaining of the sequence for n
for i in range(1, n-2):
    num_four = num_one + num_two + num_three
    num_one = num_two
    num_two = num_three
    num_three = num_four
    print(num_four)