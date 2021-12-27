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
    
        
even_nums.extend(odd_nums)

# using the sort() function vs the sorted(arg) method

# using the sorted(arg) method returns a New sorted list/more flexible..can use sorted on lists,tuples,dictionaries etc
New_list = sorted(even_nums)
print(New_list)

# whereas the sort() function returns none in place if assigned to a variable
Nl = even_nums.sort()
print(Nl)

# To return a sort in descending order
New_list = sorted(even_nums,reverse=True)
print(New_list)

# sorted() sorting a tuple will return a list of the sorted tuple 
tup = (2,6,9,8,54,69,45,7,2,3,6)
New_tup=sorted(tup)
print(New_tup)
