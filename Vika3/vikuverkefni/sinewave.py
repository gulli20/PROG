# Don't change the following lines
import math

number_of_cycles = float(input("Number of cycles: "))
number_of_lines = int(input("Stretched over how many lines? "))

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines

# ...now fill in the rest

radians = 0.0
sin_wave = 0.0

for i in range(0, number_of_lines):
    radians = i * radians_per_line
    sin_wave = math.sin(radians)
    x_count = int(round((sin_wave * 20) + 20))
    for j in range(0, x_count):
        print('X', end='')
    print()