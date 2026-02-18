def buscaBinaria(numeroProcurado):
    vector = [1,4,8,22,76,89,99]
    inicio = 0
    fim = len(vector) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vector[meio] == numeroProcurado:
            return meio
        elif vector[meio] > numeroProcurado:
            fim = meio -1
        else:
            inicio = meio + 1

    return -1                

print(buscaBinaria(45))
