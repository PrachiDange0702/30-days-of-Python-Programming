# Program to find or search a element in a list 
list=[1,2,3,4,5]
find=int(input("Enter number to find:"))
for i in range(len(list)):
         if find==i:
            break
print("Number found at index",i)
