#ex1

# my_string = 'I love Alla'
#
# with open('./sample_files/new_file.txt', 'w') as my_f:
#     my_f.write(my_string)

#ex2
# my_list = ['i','love','alla']
# with open('./sample_files/new_file.txt', 'w') as my_f:
#     # my_f.write(my_list) - NameError: name 'my_string' is not defined
#     #my_f.write(str(my_list)) #return list
#     for i in my_list:
#         my_f.write(i+'\n')

#ex 3 (appending)

# var2 = 'and Mihy and Kiry'
# with open('./sample_files/new_file.txt', 'a') as my_f:
#     my_f.write(' ')
#     my_f.write(var2)

# #ex4
# my_langs = ['Python', 'js', 'PHP', 'Java', 'Ruby']
# with open('./sample_files/my_fav_lang.csv','w')as f:
#     f.writelines(my_langs)

# ex5 join
my_langs = ['Python', 'js', 'PHP', 'Java', 'Ruby']
with open('./sample_files/my_fav_lang.csv','w')as f:
    str_my_langs = '\n'.join(my_langs)
    f.writelines(str_my_langs)
