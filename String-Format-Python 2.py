
#---------------------
#----Strings Formating New Ways-----
#---------------------------------


name= "Salar"
age= 28
rank= 10


print("my Name is :" +name)

print("My Name is : {}" .format(name))
print("My name is : {} and my age is : {} " .format(name,age))
print("My Name ist : {:s} and my age is : {:d} and my rank is : {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => float

n= "Salar"
l= "Python"
y = 10

print("My Name is : {:s} and i am {:s} Developer with {:d} EXP" .format(n,l,y))

# Control Floating Point Number
myNumber= 10
print("myNumber is {:d}" .format(myNumber))
print("myNumber is {:f}" .format(myNumber))
print("myNumber is {:.2f}" .format(myNumber))


#Turncate STring
myLongString= "Hello People of Elzeroo Web School I Love Python"
print("Message : {} ".format(myLongString))
print("Message : {:.5s} ".format(myLongString))
print("Message : {:.13s} ".format(myLongString))

# Format Money
myMoney = 500162198
print("My Money In The Bank is : {:d}".format(myMoney))
print("My Money In The Bank is : {:_d}".format(myMoney))
print("My Money In The Bank is : {:,d}".format(myMoney))

# ReArrnge Items

a, b, c = "One" , "Two" , "Three"
print("Hello {} {} {}".format(a,b,c)) # Hello One Two Three
print("Hello {1} {2} {0}".format(a,b,c)) # Hello Two Three One
print("Hello {2} {0} {1}".format(a,b,c)) # Hello Three One Two

x, y, z = 10,14,16
print("Hello {} {} {}" .format(x,y,z))
print("Hello {1:d} {2:d} {0:d}" .format(x,y,z))
print("Hello {2:.4f} {0:.5f} {1:.7f}" .format(x,y,z))


# Format In Version 3.6 +
myName = "Salar"
myAge = 27
print("My Name is :{myName} and My Age is : {myAge}")
print(f"My Name is :{myName} and My Age is : {myAge}")



