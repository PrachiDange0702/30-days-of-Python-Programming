#swap using temporary variable
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
temp=a
a=b
b=temp
print("After swap:")
print(a)
print(b)

#swap without using temporary variable
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a=a+b
b=a-b
a=a-b
print("After swap:")
print(a)
print(b)
