Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=9
>>> while a<=29:
	a+=1
	if a == 21: break
	print(a)

	
10
11
12
13
14
15
16
17
18
19
20
>>> a=0
>>> while a<=29:
	a+=1
	if a == 21: continue
	print(a)
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> a= 0
>>> print("hj32")
hj32
>>> from math import sqrt
>>> sqrt(144)
12.0
>>> 