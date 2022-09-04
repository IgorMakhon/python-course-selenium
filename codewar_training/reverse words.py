s = 'hello world!'
split_input = s.split()
split_input.reverse()
s=' '.join(split_input)
print(s)

# d = ''
# for i in split_input:
#     # print(i)
#     tmp_list = list(i)
#     tmp_list.reverse()
#     d += ''.join(tmp_list)+" "
# s=d.rstrip(" ")
# print(type(s))
# print(s)