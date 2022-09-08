'''

c = continue
n = next
l = show current line
s = step
h = help

'''


import pdb
import ipdb


# print('I am the 1st line')
# fname = 'igor'
# lname = 'mahon'
#
# pdb.set_trace()
#
# print('i am 2d line')
# print('i am 3h line')



# demo2

def get_name(name):
    names = {"igor" : "ig",
             "mark" : "mr"}
    print(f'The user "{names[name]}" is logged in')
    #pdb.set_trace()
    return names[name]

user_1 = get_name('igor')
print('User1: '+user_1)
ipdb.set_trace()

user_2=get_name('mark')
print('User2: '+user_2)