
carros = [['SUV', 3, '1320', 23455], ['Ambulancia', 1, '1640', 65243 ]]




def insertion_sort(lista):

    for i in range(1, len(lista)):
        valorActual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] >valorActual:
            lista[j + 1] = lista [j]
            j -=1
        lista[j + 1] = valorActual
    
    return lista

print(insertion_sort(carros))