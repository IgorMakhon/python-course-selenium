'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

'''
arr = [64, [2, 2, 2, 2, 2, 2]]
sum_int= 1
sum_int2 = 1
total_sum = 0
for i in range(len(arr)):
    if type(arr[i]) == int:
        sum_int *= arr[i]
    else:
        for z in range(len(arr[i])):
            sum_int2 *= arr[i][z]
            total_sum=sum_int2
if total_sum == 0:
    print(sum_int)
else:
    print(sum_int*total_sum)


