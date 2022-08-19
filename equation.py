from __future__ import division
       
while True:
       
       a = int(input("Entrer la valeur de a"))
       b = int(input("Entrer la valeur de b"))
       c = int(input("Entrer la valeur de c"))
       k=0
       w=0
       z=0
       y=0
       x=0
       
       k= (b*b) - 4*(a*c)
       

       if k<0:
              print("Pas de racine")
       elif k>0:
              w=k**0.5
              z= (-b+w)/(2*a)
              y=(-b-w)/(2*a)
              print(z)
              print (y)
       if k==0:
              x=-b/(2*a)
              print(x)
