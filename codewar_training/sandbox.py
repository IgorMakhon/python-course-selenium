init_value = 0
sum = 0
number = 200
for i in range(number):
    if number <= 0:
        sum=0
    if i%3 == 0 or i%5 == 0:
        sum += i
        i += 1
print(sum)