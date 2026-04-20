import random

lst = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
n = len(lst)
index = random.randint(0, n - 1)
print(index)
bill_payer = lst[index]
print(bill_payer)
