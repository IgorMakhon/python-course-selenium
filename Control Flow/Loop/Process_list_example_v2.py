"""
Scenario:
    You own an ecommerce marketplace site. Several partners sell their products on your site.
    Like amazon.com. The partners update their list of products and prices daily. They send you the
    product information in one of several ways (API, FTP, Email, ...).

    You have received the products information and created a list as provided below.
    Variable 'products' is the list of products you have received.


Exercise:
    - Print the name of all products that have price greater than 25.

"""

products = [
    {'id': 1, 'name': 't-shirt', 'price': '$12.99', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': '$22.45', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': '$43.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': '$14.99', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': '$32.50', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': '$150.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]


print("Exercise 1: Iterate the products list and print the name of all products that have price greater than 25.")
#print(len(products_list))
for index in range(len(products)): # define how many elements(dictionaries) in the list product_list
    for key, value in products[index].items(): # iterate all keys and values of the dictionaries to use each in 'if'
        if key == 'price':
            my_value = value.split("$")
            my_value1 = float(my_value[1])
            if my_value1 > 25:
                print(products[index].get('name'))
                break

print('=========================another solution------------')
for i in products:
    tmp_price = i['price'].replace("$"," ")
    # tmp_price = i["proce"][1:] same result as line above!
    price = float(tmp_price)
    if price > 25:
        print(i['name'])