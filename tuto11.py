napoleon = [12, 32, 92, 19,  "Exc",  16.3]

for a in napoleon:
       print(a,  end=" ")


pivoine = ["a" , -15.8]
napis = napoleon + pivoine

print (napis)
del napis [4]   #pour supprimer un élément tout en sachant sa position
print (napis)
napis.remove(16.3) #pour supprimer un élément sans savoir sa position
print(napis)

#print(len(napoleon))
#print(napoleon[3])    #pour afficher la valeur qui se trouve dans la position 3
#print(type(napoleon))
#napoleon.append(5)   # pour ajouter une variable dans la liste


#napoleon.insert(2, "b")   #pour inserer b dans la position 2

#print (napoleon)

nom="Napoleon Simbandumwe"
#lnom=nom.split(" ")
lnom=" ".join(nom)

print(type(nom), nom)
