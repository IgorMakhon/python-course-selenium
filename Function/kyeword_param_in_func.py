# Example of using keword params
# Example 1: write a function that returns number of words that have X str, given a string
#
# def get_count_of_small_words(input_string, max_size=3):
#
#     small_words = []
#     for word in input_string.split():
#         if len(word) <= max_size:
#             small_words.append(word)
#
#     return len(small_words)
#
# my_joke = "In Python hashtags are used to tell the computer a line is not worth reading. Much like social."
# print(get_count_of_small_words(my_joke, 10))


#Example 2

def connect_to_DB(host="test.db.com", username='testuser', password='Password1!'):
    print(f'Connection to host {host}')
    print(f'Username is {username}')

# print(connect_to_DB())
# connect_to_DB("prod.com", "produser")
print(connect_to_DB())