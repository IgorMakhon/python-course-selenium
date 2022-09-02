# try:
#     a=5/0
# except:
#     print("don't divide by 0")

##catch specific exception
# try:
#     a=5/0
# except KeyError:
#     print("don't divide by 0")

##catch the specific error
# try:
#     a=5/0
# except ZeroDivisionError as e:
#     print(f"Error has happend: {e}")


##print the actual error
# try:
#    print(foo)
# except Exception as e:
#     print(f"Error has happend: {e}")


##another example with several errors
# try:
#    a = 5/0
#    b={"name":"foo", "age":2}
#    x = b["school"]
# except (KeyError, ZeroDivisionError):
#     print("Error has happend:")


##example with multiple blocks
# try:
#    # a = 5/0
#    b={"name":"foo", "age":2}
#    x = b["school"]
# except KeyError:
#     print("key issue")
# except ZeroDivisionError:
#     print("divding by zero")

##raise an exception
# raise ZeroDivisionError("foo bar")


#another exception
#
# try:
#    print(foo)
# except Exception as e:
#     print(f"Error has happend: {e}")
#     raise Exception("something went wrong")

##reraise the exception
try:
   print(foo)
except Exception as e:
   print(f"Error has happend: {e}")
   raise
