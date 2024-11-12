print("Examples using integers")
x = input("What is x?")
y = input("What is y?")

# This concatenates the entries because input is string
z = x + y
print(z)

#convert string to integers
z = int(x) + int(y)
print(z)

print("Example removing intermediate variable")
#Remove use of z variable
x = int(input("What is x?"))
y = int(input("What is y?"))

print(x + y)

print("Example using float")
x = float(input("What is x?"))
y = float(input("What is y?"))

print(x + y)

print("Example using float and rounding result")
x = float(input("What is x?"))
y = float(input("What is y?"))

z = round(x + y)

print(z)

print("Example for formatting large numbers")
x = float(input("What is x?"))
y = float(input("What is y?"))

z = round(x + y)

print(f"{z:,}")

print("Example for dividing numbers")

x = float(input("What is x?"))
y = float(input("What is y?"))

z = x / y

print(z)

print("Example for rounding divided numbers")

x = float(input("What is x?"))
y = float(input("What is y?"))

z = round(x / y, 2)

print(z)

print("Example for rounding using format string")

x = float(input("What is x?"))
y = float(input("What is y?"))

z = round(x / y, 2)

print(f"{z:.2f}")