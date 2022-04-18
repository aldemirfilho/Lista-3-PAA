def posicao_k(A, B, k):
    if len(A) == 0:
        return B[k]
    elif len(B) == 0:
        return A[k]

    meioA = len(A) // 2
    meioB = len(B) // 2
    if meioA + meioB < k:
        if A[meioA] > B[meioB]:
            return posicao_k(A, B[meioB+1:], k - meioB - 1)
        else:
            return posicao_k(A[meioA+1:], B, k - meioA - 1)
    else:
        if A[meioA] > B[meioB]:
            return posicao_k(A[:meioA], B, k)
        else:
            return posicao_k(A, B[:meioB], k)

A=[1, 3, 5, 7]
B=[2, 4, 6, 8]
print("valor da posicao:", posicao_k(A, B, 5))