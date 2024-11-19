def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    if is_even_simple(x):
        print("Even")
    else:
        print("Odd")
    if is_even_simpler(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def is_even_simple(n):
    return True if n % 2 == 0 else False

def is_even_simpler(n):
    return n % 2 == 0

main()