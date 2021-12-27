"""
In Python, use list methods append(), extend(), and insert() to add items (elements) to a list or combine other lists. 
You can also use the + operator to combine lists, or use slices to insert items at specific positions.

Add an item to the end: append()
Combine lists: extend(), + operator
Insert an item at specified index: insert()
Add another list or tuple at specified index: slice

"""

# nested for loop example
even_nums = []
odd_nums = []

for num in range(1,1_01):
    # odd numbers ~ let k be an integer such that num=2k
    if num%2==0:
        # add it to list
        even_nums.append(num)
    # even numbers ~ let k be an integer such that num=2k+1
    elif num%2==1:
        #add it to list
        odd_nums.append(num)
    
        
print("Even Numbers",even_nums)
print()
print("Odd Numbers",odd_nums)

# extending a list
even_nums.extend(odd_nums)
print(even_nums)
