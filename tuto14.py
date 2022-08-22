# abc = dict() c'est la même chose que abc={}
abc = {'un': 'kimwe', 'trois': 'gatatu', 23: 'Vingt-Trois'}

for x in abc.items():
    print(x)
print(abc)


# Pour récupérer les valeurs d'un dictionnaire à partir d'une fonction

def fonction(**abc):
    print(abc)


fonction(a=5, b=8, c=10)
