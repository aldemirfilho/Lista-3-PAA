def potencia(a,n):
    if (n < 1):
        return 1
    if (a == 0):
        return 0
    if (n%2 == 0):
        return potencia(a*a,n/2)
    else:
        return a * potencia(a*a, n//2)

print("Divisão e conquista para a^n")
print("Insira a")
a = int(input())
print("Insira n")
n = int(input())
r = potencia(a,n)
print("Resultado:",r)