#Defining function
def hello():
    print("Hello")

def hello_param(to="world"):
    print("Hello,", to)


print("Calling parameter function with default name")
hello_param()

# Ask user for their name
name = input("What's your name? ")

hello()

print(name)

print("Using function with input parameter")
hello_param(name)

