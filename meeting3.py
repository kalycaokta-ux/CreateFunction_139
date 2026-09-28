#def printme( text1 ): #This is a print function
 #   print(text1)
#    return

#printme("I'm first call to user defined function!")
#printme(text1="Again second call to the same function")

def changeme( mylist ): #This changes a passed list# 
	mylist = [1,2,3,4]; 
	return 
mylist = [10,20,30]; 
changeme( mylist ); 
print ("Values outside the function: ", mylist)

def printinfo( name, age=35 ): #"Test function" 
	print ("Name: ", name); 
	print ("Age ", age); 
	return; 
printinfo( age=50, name="miki" );
printinfo( 30, "kelly");
printinfo (name="kalyca");
	
# def printinfo( arg1, *vartuple ): #"This is test" 
#  	print("Output is: ")
#     for var in vartuple: 
#  			print (var) 
#     return; 
#  printinfo( 10 ); 
#  printinfo( 70, 60, 50 ) 

sum = lambda arg1, arg2: arg1 + arg2;
print ("Value of total : ", sum( 10, 20 )) 
print ("Value of total : ", sum( 20, 20 ) )
print ("Value of total : ", sum( 60000, 7000 ) )


total = 0; # This is global variable. 
def sum( arg1, arg2 ): 
	"Add both the parameters"
	total = arg1 + arg2; 
	print "Inside the function local total : ", total 
	return total; 
# Now you can call sum function 
sum( 10, 20 ); 
print "Outside the function global total : ", total


