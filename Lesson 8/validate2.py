import re

email = input("What's your email? ").strip()

#Hand-coded method to check for email address with only letters, numbers and underscore
#must include 1 @ and .com
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
    print("Valid")
else:
    print("Invalid")

#Same method, using built in code to allow only word characters
# a-z, numbers and underscore
if re.search(r"^(\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
