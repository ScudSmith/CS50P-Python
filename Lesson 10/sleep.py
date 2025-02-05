#Example to use yield for python to incrementally return data instead of all at once
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "Sheep" * i

if __name__ == "__main__":
    main()