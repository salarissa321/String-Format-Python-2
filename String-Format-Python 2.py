
#---------------------
#----Strings Formating New Ways-----
#---------------------------------


name= "Salar"
age= 28
rank= 10


print("my Name is :" +name) # my Name is :Salar

print("My Name is : {}" .format(name)) # My Name is : Salar
print("My name is : {} and my age is : {} " .format(name,age)) # My name is : Salar and my age is : 28
print("My Name ist : {:s} and my age is : {:d} and my rank is : {:f}".format(name, age, rank)) # My Name ist : Salar and my age is : 28 and my rank is : 10.000000

# {:s} => String
# {:d} => Number
# {:f} => float

n= "Salar"
l= "Python"
y = 10

print("My Name is : {:s} and i am {:s} Developer with {:d} EXP" .format(n,l,y)) # My Name is : Salar and i am Python Developer with 10 EXP

# Control Floating Point Number
myNumber= 10
print("myNumber is {:d}" .format(myNumber)) # myNumber is 10
print("myNumber is {:f}" .format(myNumber)) # myNumber is 10.000000
print("myNumber is {:.2f}" .format(myNumber)) # myNumber is 10.00


#Turncate STring
myLongString= "Hello People of Elzeroo Web School I Love Python"
print("Message : {} ".format(myLongString)) # Message : Hello People of Elzeroo Web School I Love Python
print("Message : {:.5s} ".format(myLongString)) # Message : Hello
print("Message : {:.13s} ".format(myLongString)) # Message : Hello People

# Format Money
myMoney = 500162198
print("My Money In The Bank is : {:d}".format(myMoney)) # My Money In The Bank is : 500162198
print("My Money In The Bank is : {:_d}".format(myMoney)) # My Money In The Bank is : 500_162_198
print("My Money In The Bank is : {:,d}".format(myMoney)) # My Money In The Bank is : 500,162,198

# ReArrnge Items

a, b, c = "One" , "Two" , "Three"
print("Hello {} {} {}".format(a,b,c)) # Hello One Two Three
print("Hello {1} {2} {0}".format(a,b,c)) # Hello Two Three One
print("Hello {2} {0} {1}".format(a,b,c)) # Hello Three One Two

x, y, z = 10,14,16
print("Hello {} {} {}" .format(x,y,z)) # Hello 10 14 16
print("Hello {1:d} {2:d} {0:d}" .format(x,y,z)) # Hello 14 16 10 
print("Hello {2:.4f} {0:.5f} {1:.7f}" .format(x,y,z)) # Hello 16.0000 10.00000 14.0000000


# Format In Version 3.6 +
myName = "Salar"
myAge = 27
print("My Name is :{myName} and My Age is : {myAge}") # My Name is :{myName} and My Age is : {myAge}
print(f"My Name is :{myName} and My Age is : {myAge}") # My Name is :Salar and My Age is : 27



