# script for getting started with using basic API calls with requests

# Import statements is a important part of any programming language
# It allows you to use code that has already been written by other developers
# In this case, we are using the requests library to make API calls, and this wheel is allready invented
import requests

# in python, it is also possible to import specific functions from a library
# this is to avoid namespace collisions, and to make the code more readable
# also, some packages are huge, and you might not need all of it

# this is the base url for the API
# it is a good idea to store this in a variable, so you can easily change it later
base_url = "https://api.github.com"

# this is the endpoint we want to call
# in this case, we want to get information about the user "torvalds"
# we are using string formatting to insert the username into the url
# the {} is a placeholder for the username, and the .format() function will insert the username into the placeholder
# the .format() function can take multiple arguments, and will insert them in the order they are given
# in this case, we only have one argument, but it is still a good idea to use .format() instead of just inserting the username into the url
name = "torvalds"
endpoint = "/users/{}".format(name)

# Welcome to programming where everyone has a solution, and in most cases, there is no right or wrong
# the .format() function is not the only way to insert a variable into a string
# i will now illustrate some ways that are also valid, 
# and evaluating which one is best is up to the use case, and personal preference of the developer and/or team
# 1. concatenation
# this is the most basic way of inserting a variable into a string
# it is also the most error prone, as you have to remember to add spaces and other characters
# it is also the least readable, and should be avoided
endpoint = "/users/" + name

# 2. % operator
# this is a bit more readable than concatenation, but still not very readable
# it is also not very flexible, and should be avoided
endpoint = "/users/%s" % name

# 3. f-strings
# this is the newest way of inserting variables into a string
# it is also the most readable, and should be used if you are using python 3.6 or newer
# it is also the most flexible, as you can do calculations and other things inside the curly brackets
# it is also the fastest way of inserting variables into a string
endpoint = f"/users/{name}"

# now that we have the endpoint, we can make the API call
# we are using the requests library to make the call
# the .get() function takes the url as an argument, and returns a response object
# the response object contains the response from the API call
# we are storing the response object in a variable called response
response = requests.get(base_url + endpoint, timeout=5)

# now that we have the response, we can print it to the console
# the .text attribute of the response object contains the response as a string
# we are using the print() function to print the response to the console
# in a more rigid application, 
# you would probably want to do something with the response, 
# like storing it in a database
# and for printing or logging to the console, 
# you would probably want to use the logging module and loggers, 
# they are more flexible and powerful than the print() function
# but for this example, we are just printing the response to the console
print(response.text)

# now that we have the response, we can also convert it to a python dictionary
# This is done because in python, it is easier to work with dictionaries than strings
# because dictionaries can be accessed using keys
# the .json() function of the response object converts the response to a python dictionary
# we are storing the dictionary in a variable called data
data = response.json()

# now that we have the data, we can print it to the console

print("This is the data as a dictionary")
print(data)

# Now that you got the basics of get requests,
# you can try to make some more requests to the Github api
# Then we need to cover CRUD (Create, Read, Update, Delete)
# and then we can move on to authentication (basics)
# and then we can move on to the Tripletex
# here are their examples for python https://github.com/Tripletex/tripletex-api2/tree/master/examples/python
# Happy coding! :) 