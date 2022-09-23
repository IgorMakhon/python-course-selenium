"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate-random_email_with_list_of_domains_v1.csv
"""
import random
import string
# import ipdb
# ipdb.set_trace()

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
length = 5
letters = string.ascii_lowercase
random_string = ''
email = ''
list_of_emails = []

for j in range(len(list_of_domains)):
    for k in range(20):
        random_string = ''.join(random.choice(letters) for i in range(length))
        email = random_string + '@' + list_of_domains[j]
        list_of_emails.append(email)

str_emails = ',\n'.join(list_of_emails)
with open('./EXERCISE_v1.csv', 'w') as my_f:
    my_f.write(',\n'.join(list_of_emails))
