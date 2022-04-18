def hanoi(n, a, d, b, c):
    if n == 0:
        return
    if n == 1:
        print("Mova o disco", n, "da torre", a, "para torre", d)
        return
   
    hanoi(n-2, a, b, c, d)
    
    print("Mova o disco", n-1, "da torre", a, "para torre", c)
    
    print("Mova o disco", n, "da torre", a, "para torre", d)
    
    print("Mova o disco", n-1, "da torre", c, "para torre", d)
    
    hanoi(n-2, b , d, a, c)


print("Insira o número de discos")
n = int(input())
print("Número de discos:",n)
hanoi(n,'A','D','B','C')
