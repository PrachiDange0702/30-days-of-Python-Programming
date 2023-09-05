#write a function in python to count and display the total number of words in a text file.

def countfun():   
	count = 0
	file = open("hello.txt", "r")  
	for line in file:  
	    words = line.split(" ")  
	    count = count + len(words)
	print("Number of words present in given file: " + str(count))
	file.close()
countfun()
