# %%

print(type(1244))

# %%

print(type("hello"))

# %%

print(type(True))

# %%

print(type(3.5))

# %%

score = 0
height = 1.8
is_winning = True

print(f"your score = {score}. \n your height is {1.8}. \n you are winning:{is_winning}")

# tip calculator
#  %%

print("welcome to the tip calculator")

bill = int(input("what was the total bill? "))
tip = int(input("how much tip would you like to give? 10,12 or 15? "))
split = int(input("how many people split to split the bill? "))

individual_cost = round((bill + (tip / 100 * bill)) / split, 2)
print(f"each person should pay {individual_cost}")
