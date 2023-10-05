#def my_function():
   #print("Hello from a function")
#my_function()
"""def my_function(fname):
    print(fname+"Refsnes")
my_function("email")
my_function("tobias")     arguments function
my_function("linus")"""
def my_function(*kids):
    print("the youngest child is " + kids[2])   #arbitrary arguments, args
my_function("email","tobias","linus")