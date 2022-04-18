def check(n, caixas):
    if n == 0:
        return True
    elif n < 0:
        return False
    if check(n - 20, caixas):
        caixas[3] = caixas[3]+1
        return True
    if check(n - 9, caixas):
        caixas[2] = caixas[2]+1
        return True
    if check(n - 6, caixas):
        caixas[1] = caixas[1]+1
        return True
    if check(n - 4, caixas):
        caixas[0] = caixas[0]+1
        return True
    else:
        return False
        
caixas = [0, 0, 0, 0]
nugg = 43
if check(nugg, caixas):        
    print("Quantidade de caixas:\n\n-Caixas de 4 Unid:  ", caixas[0], 
          "\n-Caixas de 6 Unid:  ", caixas[1], "\n-Caixas de 9 Unid:  ", caixas[2], 
          "\n-Caixas de 20 Unid: ", caixas[3])
    print("\nTotal de caixas: ", caixas[0]+caixas[1]+caixas[2]+caixas[3], " caixas para", nugg, "nuggets")
else:
    print("Pedido não pode ser atendido!")