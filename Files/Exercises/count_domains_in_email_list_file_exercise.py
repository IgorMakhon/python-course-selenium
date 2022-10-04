"""
Read the list of email addresses from the input file and create a dictionary
with keys being domain name and value being the number of occurrences for the domain.
In other words count how many times each domain exists and create a report of the count as a dictionary.
Save the output into a .json file.

- input file: count_domains_in_email_list_file_exercise_input.csv
- output file: count_domains_in_email_list_file_exercise_output.json

Example output:
{'yahoo.com': 19, 'gmail.com': 20, 'msn.com': 16, 'supersqa.com': 20, 'outlook.com': 25}

"""


input_file = "count_domains_in_email_list_file_exercise_input.csv"
output_file = "count_domains_in_email_list_file_exercise_output.json"
list_of_domains = []
#open file
with open(input_file, 'r') as f:
    #read file
    text_from_file = f.read()
#split string by @ to the list
splitted_text1 = text_from_file.split('@')
#join list by comma in string
string1 = ','.join(splitted_text1)
#split string by comma to list
my_list = string1.split(',')
# print(my_list)

#create list of domains
for i in range(len(my_list)):
     # print(my_list[i])
     # print('---------------')
     if my_list[i].endswith('com'):
         list_of_domains.append(my_list[i])

count_yahoo = 0
count_gmail = 0
count_msn = 0
count_supersqa = 0

#count domains
for k in range(len(list_of_domains)):
    if list_of_domains[k] == 'yahoo.com':
        count_yahoo += 1
    elif list_of_domains[k] == 'gmail.com':
        count_gmail += 1
    elif list_of_domains[k] == 'msn.com':
        count_msn += 1
    elif list_of_domains[k] == 'supersqa.com':
        count_supersqa += 1
#print(count_supersqa,count_yahoo, count_msn, count_gmail)
yahoo = '"yahoo.com": ' +str(count_yahoo)
gmail = '"gmail.com" : ' + str(count_gmail)
msn = '"msn.com": ' + str(count_msn)
supr = '"supersqa.com": ' + str(count_supersqa)
my_string = '{' + yahoo + ', ' + gmail + ', ' + msn + ', ' + supr + '}'
#print(my_string)
#wtite file
with open('count_domains_in_email_list_file_exercise_output.json','w')as f1:
     f1.writelines('{' + yahoo + ', ' + gmail + ', ' + msn + ', ' + supr + '}')