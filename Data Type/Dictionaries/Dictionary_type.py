# capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
# print(type(capitals))

# return value from dictionary
# cap_FRA = capitals["France"]
# print(cap_FRA)
# print("=================")
#
# # another way to return value from dictionary(preferable)
# cap_USA = capitals.get('USA')
# print(cap_USA)
# print("=================")


# get KYE that doesn't exist
# cap_ITA = capitals["Italy"] # will fail and stop the script
# print(cap_ITA)
# print("=================")

# get KYE that doesn't exist another approach - method 'get'
# cap_ITA = capitals.get("Italy", "the dictionary doesn't contain this value")
# print(cap_ITA)
# print("=================")

###################

# add key : Value in the dictionary
# 1 option
# print("Before add ")
# print(capitals)
# capitals["Poland"] = "Warsaw"
# print("After add ")
# print(capitals)
# print("=================")
#
# # 2 Option
# print ("the second option to add via .update ")
# capitals.update({"Ukraine": "Kiev"})
# print(capitals)
# print("=================")
#
# # Assigment 1 - UPDATE when the value already exists in the dictionary
#
# print ("UPDATE when the value already exists in the dictionary ")
# capitals.update({"Ukraine": "Kiev"})
# print(capitals.update({"Ukraine": "Kiev"}))
# print(capitals)
# print("=================")
#
#
# # Assigment 2 - setfefault method
# print ("1 setfefault method to Ukraine ")
# print(capitals.setdefault("Ukraine"))
# print(capitals)
# print("----------------------")
# print ("2 setfefault method to non-existed key Germany ")
# print(capitals.setdefault("Germany", "igor"))
# print(capitals)
#
# print("----------------------")
# print ("3 setfefault method to non-existed key Germany + value Berlin")
# default_value = 100
# print(capitals.setdefault(default_value, 'new'))
# print(capitals)

capitals = {"USA": "Washington DC", "France": "Paris", "Turkey": "Ankara"}
print(type(capitals))
all_keys = capitals.keys()
all_values = capitals.values()
print(all_keys)
print(all_values)
print(list(all_keys)) #in Python3
print(list(all_values)) #in Python3