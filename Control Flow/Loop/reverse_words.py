# xs = ['i', 'l', 'p']
# s = ' '.join(xs)
# print(s)

my_input = 'Igor!1 split'
split_input = my_input.split()
# print(split_input)
# tmp_list =[]
# for i in split_input:








tmp_list = []
tmp_list_reversed = []
out_str = " "
for i in split_input:
    tmp_list = list(i)
    tmp_list.reverse()
    tmp_list_reversed.append(tmp_list)
    s = ' '.join([str(item) for item in tmp_list_reversed])
    break
# print(type(tmp_list_reversed))
# s = ' '.join(map(str, tmp_list_reversed))
print(s)




