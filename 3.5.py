def busca_binaria_recursiva_i(A, esquerda, direita):
    if direita < esquerda:
        return -1
    i = (esquerda + direita) // 2
    if A[i] == i:
        return i
    elif A[i] > i:
        return busca_binaria_recursiva_i(A, esquerda, i - 1)
    else:
        return busca_binaria_recursiva_i(A, i + 1, direita)

A = [-293, - 200, -42, -12, -2, 5, 89, 50]

a = busca_binaria_recursiva_i(A, 0, len(A))
print("Elemento: ", a, "\nPosição: A[", a, "]")
