##########################################

# Funcion que recibe un string y lo devuelve al reves 
def alreves(string):
    lista = []
    backwards = []
    reverse = ''
    for i in string:
        lista.append(i)   # Lo convertimos a una lista de caracteres 
    for i in range(len(lista) -1, -1, -1):  # Recorre la lista de caracteres de atras hacia adelante, de uno en uno, hasta la posicion -1 (se detiene en 0)
        backwards.append(lista[i])
    reverse = ''.join(backwards)  # Con join, unimos la lista de caracteres en un string 
    return reverse

print(alreves('hola'))


##########################################

# Crea un programa que cuente cuántas vocales hay en un texto.

def vocales(texto):
    cantidad_vocales = 0
    for i in texto.lower():
        if i in {'a', 'e', 'i', 'o', 'u'}: # se instancia un set con los valores a buscar 
            cantidad_vocales += 1
    return cantidad_vocales

print(vocales('AEIOU'))

def vocales_2(texto):
    # list comprenhension 
    return sum(1 for i in texto.lower() if i in {'a', 'e', 'i', 'o', 'u'})
    # Esto lo que hace es devolver un 1 cada vez que encuentra una vocal -> [1, 1, 1] y al final sum() hace la suma total 

print(vocales_2("Mi nombre es Johel"))

##########################################

def max_min(n1,n2,n3,n4,n5):
    
    numeros = [n1, n2, n3, n4, n5]
    maximo = None
    for i in range(len(numeros)):
        if i >= numeros[i]:
            maximo = i
    return maximo

    # maximo = max(numeros)
    # minimo = min(numeros)
print(max_min(1,2,3,4,5))

    
    