"""If you do not know how many arguments that will be passed into your function, add a * before the parameter name in
the function definition. This way the function will receive a tuple of arguments, and can access the items
accordingly: """


def my_function(*kids):
    print("The youngest child is " + str(kids[2]))


my_function("Emil", "Tobias", "Linus")

"""If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before 
the parameter name in the function definition. This way the function will receive a dictionary of arguments, 
and can access the items accordingly: """


def my_function(**kid):
    print("His last name is " + kid["fname"])


my_function(fname="Tobias", lname="Refsnes")
