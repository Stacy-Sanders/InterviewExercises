total = 0
for number in range(0, 101, 2):  # can start at 2
    total += number
print(total)

# my second option
total = 0
for number in range(0, 101):
    if number % 2 == 0:
        total += number
print(total)

# my third option
evens = []
for number in range(2, 101, 2):
    evens.append(number)
print(sum(evens))
