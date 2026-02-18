def bubblesort(vector):
    n = len(vector)

    for i in range(n):
        control = True

        for j in range(n-1):
            if vector[j] < vector[j+1]:
                aux = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = aux
                control = False

        if control:
            break;        

vector = [5,8,2,4,9]
bubblesort(vector)

for value in vector:
    print(value)