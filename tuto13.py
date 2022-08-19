""" try:
    a = int(input("Saisissez un nombre: "))
    b = int(input("Saisissez un autre nombre: "))
    div = a/b
except ValueError:
    print("Valeur siyo")
    a = int(input("Saisissez un nombre: "))
    b = int(input("Saisissez un autre nombre: "))

except ZeroDivisionError:
    print("Division par 0 inexistante")
else:
    print(a, "/", b, "=", div)
finally:
    print("Merci beaucoup") """

try:
    a = int(input("Andika igiharuro kiri >0: "))
    assert a < 0
except AssertionError:
    print("Le nombre saisi ne remplit pas les conditions")
else:
    print(a)
finally:
    print("Merci")
