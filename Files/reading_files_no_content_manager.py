import ipdb

#demo one
# sample_file = './sample_files/programming_language_wikipedia.txt'
# my_file=open(sample_file, 'r')
# content=my_file.read()
# my_file.close()
#
# ipdb.set_trace()


#exampl two
sample_file = './sample_files/programming_language_wikipedia.txt'
# my_file = open(sample_file, 'r')
# content = my_file.readlines()
# my_file.close()
#
# print(content)

#gotcha!
#the .seek()
my_file = open(sample_file, 'r')
content = my_file.read()
my_file.seek(0)
print(content)
print('1------------')
content2 = my_file.read()
print(content2)
print('2------------')
my_file.close()
