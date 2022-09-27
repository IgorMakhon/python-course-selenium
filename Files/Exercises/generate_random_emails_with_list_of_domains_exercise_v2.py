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

V2:
- Create 100 total emails with domains randomly elected from the list. So the number of emails
for each domain will be unknown.
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v2.csv

** the difference from V1 is the domains are random for this one.
"""

import random
import string
# import ipdb
# ipdb.set_trace()

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']
list_of_emails = []
letters = string.ascii_lowercase

#generate 100 random emails with random domians from list and store in string
for k in range(100):
    email = ''.join(random.choice(letters) for i in range(5)) + '@' + random.choice(list_of_domains)
    list_of_emails.append(email)

#save to CSV file with requirements: Output a csv file with one email on each line and each line ending with a comma
with open('./EXERCISE_v2.csv', 'w') as my_f:
    my_f.write(',\n'.join(list_of_emails))
