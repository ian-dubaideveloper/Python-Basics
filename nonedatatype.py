

#None is used to make an object eligibe for garbage collection

a = 10

print (type(a))

a = None

print(a)

#a is an object
#None is an object

#if its an object it must have an address
#we use Id() to get an address

print(id(a))

print(type(a))

#we got only one None object