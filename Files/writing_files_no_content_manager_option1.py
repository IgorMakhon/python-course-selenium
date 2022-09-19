my_string = 'I love Alla'

#example 1
# my_f = open('./sample_files/my_example_file_1','w')
# my_f.write(my_string)
# my_f.close()

#example 2
my_f = open('./sample_files/my_example_file_1.txt','w')
my_f.write(my_string)
my_f.write('\n')
my_f.write(my_string)
my_f.write('\n')
my_f.write(my_string)
my_f.close()