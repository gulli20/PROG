length = int(input("Input the length of series: "))
sum = 0
num = 0
for i in range(length):
    num += 2
    if num % 4 == 0:
        num = num * -1
    print(num)
    sum += num
    if num < 0:
        num = num * -1
print("sum:", sum)




sum = 0
for i in range(1, num+1):
    sum += i
    print(sum)