theatre_name = 'Yanka Kypala'
age_limit = 18

print(f"Welcome to the {theatre_name}") #py3 only
print("Welcome to the {}".format(theatre_name)) #works in py2 and py3
print("Welcome to the " + theatre_name) #works in py2 and py3

user_input = input("Enter your age: ")
print(f"Your age is {user_input}")

if int(user_input) >= age_limit:
    print('Enjoy the movie')
else:
    print(f'You must be {age_limit} age to watch the movie')