max_num = int(input("Input maximum number: "))

sum_cube = 0
sum = 0
for i in range(1, (max_num+1)):
    i_str = str(i)
    for j in i_str:
        sum += int(j)
    sum_cube = sum**3
    if sum_cube == i:
        print(i)
    sum = 0