# Definition of function Hello() has the parameter 'name'
def hello(name):
    # Prints Hello with a parameter 'name' when called
    # Parameter is a variable stored in function until next call
    print('Hello ' + name)

hello('Christian')
# Parameter 'name' is replaced with 'General'
hello('General')

# Parameters are stored in called function memory, cannot be called
# 'name' undefined term
# print(name)
