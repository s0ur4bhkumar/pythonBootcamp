# %%

print("welcome to the rollercoster!")
height = int(input("enter your height: "))

if height > 120:
    print("you can ride the rollercoster")
    age = int(input("enter your age: "))
    if age <= 18:
        print("please pay 7 dollars")
    else:
        print("please pay 8 dollars")
else:
    print("you cannot ride the rollercoster")

# %%

number = int(input("enter the number: "))

if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# %%

a = int(input("enter the first number: "))
b = int(input("enter the secont number: "))

if not a < 0 and not b < 0:
    if a % 2 == 0 or b % 2 == 0:
        print("there's an even number")
    elif a % 2 == 0 and b % 2 == 0:
        print("both are even")
    else:
        print("both are odd")
else:
    print("numbers should not be less than zero")
