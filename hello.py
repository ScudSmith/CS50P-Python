print("Basic examples to retrieve and display text")

# Ask user for their name
name = input("1. What's your name? ")

# Say hello to user - different methods
print("hello,")
print(name)

# String Concatenation
print("hello, " + name)

#Multiple arguments to function
print("hello,", name)

# Overrides end parameter which is default \n
print("hello, ", end="")
print(name)

#Overrides separator parameter which is default " "
print("hello,", name, sep="???")

# This is format
print(f"hello, {name}")

print("Example to handle poorly formatted input with strip, capitalize, and title")
# Prompt again for badly formatted name
name = input("2. What's your name? ")

#Remove whitespace from str
name = name.strip()

# This is format
print(f"hello, {name}")

# Capitalize first letter of text
name = name.capitalize()

# This is format
print(f"hello, {name}")

# Capitalize first letter of each word
name = name.title()

# This is format
print(f"hello, {name}")

print("Example to handle poorly formed input with strip and title combined on one line")
# Prompt again for badly formatted name
name = input("3. What's your name? ")

#Remove whitespace from str and fix capitals
name = name.strip().title()

# This is format
print(f"hello, {name}")

print("Example to handle poorly formed input with input and cleanup combined on one line")
# Prompt again for badly formatted name and clean up on one line
name = input("4. What's your name? ").strip().title()

# This is format
print(f"hello, {name}")

print("Example of splitting user name into two parts")
# Prompt again for badly formatted name
name = input("5. What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

# This is format
print(f"hello, {first}")