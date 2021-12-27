# For loop example
nums = [500,7,1,3,82,6,9,4,8,100]

for num in nums:
    if num in range(50,1_000):
        print(num)
print("Loop terminated")

# Break example
nums = [500,7,1,3,82,6,9,4,8,100]

for num in nums:
    if num == 8:
        # breaks when condition is met
        print(num)
        break
print("Found!")

# Continue example
nums = [500,7,1,3,82,6,9,4,8,100]

for num in nums:
    if num == 8:
        # continue ignores 8 and prints numbers afterwards
        continue
    print(num)
