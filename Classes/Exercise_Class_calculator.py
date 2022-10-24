"""
Create a class that has basic calculating functions.

You can have as many methods as you like but here are few suggestions.
* method to take two numbers and add them and return the sum
* method to take two numbers and subtract the second number from the first number and return the diff
* method to take two numbers and return the multiplication of the two
* method to divide two numbers and return the result (first number divided by second number)

"""

# class Calculator(object):
#
#     def sum(self, first_arg, second_arg):
#         return print(f"The sum of the first and the second args is {float(first_arg)+float(second_arg)}")
#
#     def diff(self, first_arg, second_arg):
#         return print(f"The diff of the first and the second args is {float(first_arg) - float(second_arg)}")
#
#     def multiplication(self, first_arg, second_arg):
#         return print(f"The multiplication of the first on the second arg is {float(first_arg) * float(second_arg)}")
#
#     def division(self,first_arg, second_arg):
#         return print(f"The division of the first on the second arg is {float(first_arg) / float(second_arg)}")
#
#
# cal_sum = Calculator()
#
# cal_sum.sum(10,20)
# cal_sum.diff(10,20)
# cal_sum.division(10,20)
# cal_sum.multiplication(10,20)


class Calculator(object):

    def __init__(self, first_arg, second_arg):
        self.first_arg = first_arg
        self.second_arg = second_arg

    def sum(self):
        return print(f"The sum of the first and the second args is {float(self.first_arg)+float(self.second_arg)}")

    def diff(self):
        return print(f"The diff of the first and the second args is {float(self.first_arg) - float(self.second_arg)}")

    def multiplication(self):
        return print(f"The multiplication of the first on the second arg is {float(self.first_arg) * float(self.second_arg)}")

    def division(self):
        return print(f"The division of the first on the second arg is {float(self.first_arg) / float(self.second_arg)}")


my_obj = Calculator(10,20)
my_obj.sum()
