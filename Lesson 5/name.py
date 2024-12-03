import sys

#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few arguments")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too many arguments")
    
#print("hello, my name is", sys.argv[1])

#This would print multiple lines for 
#names given, but includes python file name
for arg in sys.argv:
    print("hello, my name is", arg)

#This skips the file name
for arg in sys.argv[1:]:
    print("hello, my name is", arg)