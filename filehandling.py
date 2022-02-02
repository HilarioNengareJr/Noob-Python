#with open('test.txt','r') as f:
   #for line in f:
        #print(line)
    #f_contents = f.read() //for reading file contents
    #print(f_contents)

print(" Please enter something ")

with open('test.txt', 'r') as rf:
    with open('test2.txt','w') as f:
        f_contents = f.write(input())
        print("Check test2.txt")
        
   
    
'''

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a:  open an existing file for append operation. It won’t override existing data.
 r+:  To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

'''
