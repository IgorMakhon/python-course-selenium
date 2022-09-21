'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
'''
import ipdb
def likes(names):
    my_phrase = ''
    quantity= 0
    if len(names) <= 0:
        my_phrase = "no one likes this"
    elif len(names) == 1:
        my_phrase = names[0] + ' likes this'
    elif len(names) == 2:
        my_phrase = names[0] + ', ' + names[1] + ' like this'
    elif len(names) == 3:
        my_phrase = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    elif len(names) >3:
        quantity = len(names) - 2
        my_phrase = names[0] + ', ' + names[1] + ' and ' + str(quantity) + ' others like this'
    return my_phrase
ipdb.set_trace()
