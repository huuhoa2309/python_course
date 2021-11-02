import sys
try:
    x= int(input("Enter a number: "))
    y= int(input("Enter another number: "))
except ValueError:
    print("dm hieu tieng anh khong")
    sys.exit(1)
#result= x/y
try:
    result= x/y
except ZeroDivisionError:
    print("dm k chia duoc")
    sys.exit(1)


print(f"{x} divide {y} result : {result}")