#example 1
# a=4
# b=4
# c=30
# d=40
#
# if a>b:
#     print("'a' is bigger than 'b'")
# elif a<b:
#     print("'a' is less than 'b'")
# else:
#     print("'a' equals 'b'")

#example 2

shows = ['friends', 'the office']
movie = ['rockie', 'jaws']

my_choice = 'Friends'

if my_choice in shows:
    print(my_choice + " is a show")
elif my_choice in movie:
    print(my_choice + ' is a movie')
else:
    print(my_choice + ' is unknown')