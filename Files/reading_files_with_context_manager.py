
import ipdb

#example1
#sample_files = './sample_files/programming_language_wikipedia.txt'
# with open(sample_files, 'r') as f:
#     content = f.read()
#
# print(content)

#example2

contries_file = './sample_files/list_of_countries_with_no_comma.txt'

with open(contries_file, 'r') as f:
    #content = f.read()
    countries = f.readlines()


ipdb.set_trace()
#list_of_c = [i.strip() for i in countries] - remove '\n'
