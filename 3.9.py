def maximo(seq, menor, maior):
    if menor == maior:                                      
        return seq[menor]
    if maior == menor + 1 and seq[menor] >= seq[maior]:
       return seq[menor];
    if maior == menor + 1 and seq[menor] < seq[maior]:
        return seq[maior]
    meio = (menor + maior)//2
    if seq[meio] > seq[meio + 1] and seq[meio] > seq[meio - 1]:
        return seq[meio]
    if seq[meio] > seq[meio + 1] and seq[meio] < seq[meio - 1]:
        return maximo(seq, menor, meio-1)
    else: # se seq[meio-1] < seq[meio] < seq[meio+1] (Ex: 38, 46, 57)
        return maximo(seq, meio + 1, maior)

seq = [1, 24, 25, 38, 46, 57, 41, 29, 26, 13]
#seq = [1, 3, 50, 10, 9, 7, 6]
n = len(seq)
print ("O ponto de máximo P é: %d"% maximo(seq, 0, n-1))
