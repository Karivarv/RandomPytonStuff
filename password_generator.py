import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "123456789"
symboler = "!?"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers
if syms:
    all += symboler

lenght = 10
amount = 100

for x in range(amount):
    password = "".join(random.sample(all, lenght))
    print(password)