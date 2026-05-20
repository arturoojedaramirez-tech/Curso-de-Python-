n = int(input("Introduce un número entero: "))

primos = []
for num in range(2, n):
    es_primo = True
    for i in range(2, int(num0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

print("Los números primos menores que", n, "son:")
print(primos)
