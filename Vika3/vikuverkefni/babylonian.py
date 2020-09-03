# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

# Implement the Babylonian square root algorithm

# let n be the number for which to find the square root (number)
# let g be the initial guess (guess)
# let t be the tolerance (tolerance)
# let g' be our previous guess, initialized to 0
# previous_guess = 0
# while the absolute difference between g and g' is greater than t
#   g' = g
# previous_guess = guess
#   g = average of n/g and g
# guess = float(((number/guess) + guess) / 2)

count = 0
previous_guess = 0
while abs(previous_guess - guess) > tolerance:
    previous_guess = float(guess)
    guess = float(((number/guess) + guess) / 2)
    count += 1

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")