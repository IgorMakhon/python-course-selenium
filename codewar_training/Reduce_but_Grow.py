arr = [1, 2, 3, 4, [5, 4]]
sum_int= 1
sum_list =1
total_sum = 0
list = []
for i in range(len(arr)):
    # print(arr[i])
    # print(type(arr[i]))
    if type(arr[i]) == list:
        for v in range(len(arr[i])):
            sum_list *= arr[i][z]
        # print(type(arr[i]))
        print('-----------------')
    else:
        sum_int *= arr[i]
        # print(type(arr[i]))
        # print(sum)
        print('-----------------')
total_sum = sum_int*sum_list
print(total_sum)

     # if type(arr[i]) == int:
     #     #print(arr[i])
     #     sum = arr[i]*arr[i+1]
     #     sum+=sum
     #     print(sum)
     #     print("-------------")
     # else:



