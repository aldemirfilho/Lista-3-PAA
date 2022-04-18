def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)
        i = 0
        j = 0
        k = 0
        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1
        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1
        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista
    
def investimento(lista, j):
    if(lista[0][1] < lista[j][1]):
        print("Compre em: ", lista[0][0], "\nVenda em: ", lista[j][0])
        return
    else:
        investimento(lista,j-1)
        
lista = [[100,0], [180,1], [260,2], [310,3], [40,4], [535,5], [695,6]]
mergeSort(lista)
investimento(lista, len(lista)-1)

