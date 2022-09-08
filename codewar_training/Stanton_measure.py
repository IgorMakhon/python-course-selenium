'''
The Stanton measure of an array is computed as follows: count the number of occurences for value 1 in the array. Let this count be n. The Stanton measure is the number of times that n appears in the array.

Write a function which takes an integer array and returns its Stanton measure.

Examples
The Stanton measure of [1, 4, 3, 2, 1, 2, 3, 2] is 3, because 1 occurs 2 times in the array and 2 occurs 3 times.

The Stanton measure of [1, 4, 1, 2, 11, 2, 3, 1] is 1, because 1 occurs 3 times in the array and 3 occurs 1 time.
'''
def stanton_measure(arr):
    count = 0
    count2 = 0
    for i in range(len(arr)):
    # print(i)
        if arr[i] == 1:
        # print(arr[i])
            count += 1
    for z in range(len(arr)):
    # print(count)
        if arr[z] == count:
        # print(arr[z])
            count2 += 1
    return count2