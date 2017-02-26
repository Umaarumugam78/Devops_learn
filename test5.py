
def total(num):
    "this holds number"
    print (num)
    return;

total("789")
total("67.90")


def changeme( mylist ):
   "This changes a passed list into this function"
   mylist=[1,2,3,4];
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)


def general( task1, *strtuple ):
   "This prints a variable passed arguments"
   print ("List is: ")
   print (task1)
   for var in strtuple:
      print (var)
   return;

general("cap")
general(2,6,12)

add=lambda t1,t2,t3: (t1+t2)*t3;

print ("final value:" , add(2,3,4))
print ("final value:" , add(1,2,4))

models=3456
def newmodels():
    modles=models+10

print (models)
newmodels()
print (models)
    
