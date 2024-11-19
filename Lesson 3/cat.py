while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

i = 0

while i < 3:
    print("MEOW")
    i += 1

# _ can be used in place of a variable 
# that is needed of for counting, etc
for _ in range(3):
    print("meow")

# end="" removes extra new line that would get printed
# This is a Python only structure
print("MEOW\n" * 3, end="")