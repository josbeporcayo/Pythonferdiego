print('Hello world')

#Variable types
x=1 #int
y=1.56 #float
z='String' #str
a=True #bool

print(type(x)) #What variable type are we dealing with

#Data types

#####################Lists
unalista=[8,9,10,'Diego','Junior'] # This is a list

# lists are indexed from 0 to n

print(unalista[3])

#list slices

listslice=unalista[1:3] #slice list from 1 to but not including 3

print(listslice)

print(unalista[0:-4])  #backward indeces 

#functions that operate over lists

unalista.append('Nuevo') # append new element to end of list

print(unalista)

unalista.pop(4) #eliminate list element

print(unalista)

print(len(unalista))

######################Dictionaries

undiccio={'llave1':'valor','llave2':[1,2,3,4],'llave3':9.0} 

print(undiccio)

print(undiccio['llave1'])

print(undiccio['llave2'])

#######################Tuples

x,y,z=(1,2,3)

print(x+z)

u=(1,'dos',3)

print(u[1]) # get the 2nd element of the tuple u



