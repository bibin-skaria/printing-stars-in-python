#!/usr/bin/python

a =int(input ('enter a no.'))
b=a-1
c= a/2
d=1
for x in range(a/2)  :
	x +=1
	print ('*'* x)+(' '* b)+(' ')+('*'* x)
	b -= 2	

if not (a%2==0):

	print ( '*'*c)+(' ')+('*')+(' ')+('*'*c)
	d +=1
	for y in range(a/2) :
      		 print ('*'*(c))+(' '* d)+(' ')+('*'*(c))
      		 c -= 1
		 d += 2
     		 
else :
	for y in range(a/2) :
      		 print ('*'*(c))+(' '* d)+(' ')+('*'*(c))
      		 c -= 1
		 d += 2	
      		 


