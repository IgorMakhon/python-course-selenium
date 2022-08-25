# desirable_number = 10
# user_input = 0
# while user_input != desirable_number:
#     user_input = int(input("Please guess the number from 0 to 10: "))
#     print(f"You entered : {user_input}")
# print("great!")


# example1 with break
# desirable_number = 10
# while True:
#     user_input = int(input("Please enter the number from 0 to 10!: "))
#     if user_input == desirable_number:
#         break
#     else:
#         continue
# print("great!")

# EXAMPLE2 - given a country, print its capital from dictionary, if not print "unknown"


# capitals = {
#     "Belarus": "Minsk",
#     "Spain": "Madrid",
#     "Russia": "Moscow",
#     "Poland": "Warsaw",
#     "Ethiopia": "Adis Ababa",
#     "Ghana": "Accra",
#     "Ukraine": "Kiev"
# }
#
# user_input = input("please input the country: ")
# # print(user_input.lower())
# # print("---------------------------")
#
# for country, capital in capitals.items():
#     # print("Country = " + country)
#     # print("Capital = " + capital)
#     # print("=============================================")
#     if user_input.lower() == country.lower():
#         print("The capital is: " + capital)
#         break
# print("The capital of this country '"+user_input+"' is uknown!")


# example with continue
## given a dictionary with book price and list of courses, calculate the total cost of books

book_prices = {
    "math": 200,
    "physics": 200,
    "english": 200,
}
my_courses = ["math", "english", "history", "physics"]

total_price =0

for course in my_courses:
    if course not in book_prices.keys():
        continue
    print(f"book_price[course]= {book_prices[course]}")
    print("==================================================")
    total_price += book_prices[course]
    print(f"interim price {total_price}")

print(f"Price = {total_price}")