'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''
vowels_list = ['A', 'e', 'i', 'o', 'u']
my_string = 'abracadabra'
splited_str = list(my_string)
count = 0
for i in range(len(splited_str)):
    for k in range(len(vowels_list)):
       if vowels_list[k].lower() == splited_str[i].lower():
            count += 1
print(count)




