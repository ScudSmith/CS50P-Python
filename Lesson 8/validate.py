email = input("What's your email? ").strip()

#bad way to check if email is valid
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

#better method to check still not thorough
username, domain = email.split("@")

if username and domain.endswith(".com"):
    print("Valid")
else:
    print("Invalid")



