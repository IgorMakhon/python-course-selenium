
class  MyClass1:

    def __init__(self, cls1_input_1):
        print('__init__ of class 1')
        self.prop_cls = 10
        self.cl11_in_1 = cls1_input_1
        print(self.cl11_in_1)

    def method_1_class_1(self):
        print('method_1_class_1')

class MyClass2(MyClass1):     ###several classes can be inherit

    def __init__(self, cl1in1, cl2in1):
        super().__init__(cl1in1)      ###apply init from the 1 class
        print('__init__ of class 2')
        self.cl2in1 = cl2in1

    def method_1_class_2(self):
        print('method_1_class_2')

#
# obj1 = MyClass1()
# obj1.method_1_class_1()

obj2 = MyClass2('abc','87')
# obj2.method_1_class_2()
# obj2.method_1_class_1()