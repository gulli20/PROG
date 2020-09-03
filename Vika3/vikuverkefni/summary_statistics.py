# You might need this to calculate a square root using math.sqrt
import math
n_int = int(input("Enter a number (-1 to exit) "))
# Loop until the user types in -1
count = 0
sum_n_int = 0
new_standard_s = 0
old_standard_s = 0
old_average = 0
while n_int > -1:
    # Calculate the cumulative moving average and standard deviation
    count += 1
    current_average = float((n_int + sum_n_int) / count)
    sum_n_int += n_int
    new_standard_s = float(old_standard_s + ((n_int - old_average)*(n_int - current_average)))
    old_standard_s = new_standard_s 
    standard_deviation = math.sqrt(new_standard_s/count)
    old_average = current_average
    # Print them out within the loop
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))
    n_int = int(input("Enter a number (-1 to exit) "))
