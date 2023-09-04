def pyramid(i,j):
    while i<=10:
        j=1
        while j<=i:
          print("*",end="")
          j+=1
        i+=1
        print()
        
i=1
j=1
pyramid(i,j)
