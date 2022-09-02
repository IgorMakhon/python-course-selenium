# xs = ['i', 'l', 'p']
# s = ' '.join(xs)
# print(s)

s = 'olleh !dlrow'
split_input = s.split()
tmp_list = []
d = ''
for i in split_input:
    # print(i)
    tmp_list = list(i)
    tmp_list.reverse()
    d += ''.join(tmp_list)+" "
s=d.rstrip(" ")
print(type(s))
print(s)



