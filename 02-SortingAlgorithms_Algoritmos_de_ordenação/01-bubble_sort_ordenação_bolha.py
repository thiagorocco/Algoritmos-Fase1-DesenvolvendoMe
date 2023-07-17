'''
    Ordenação bolha - Classifica os elementos efetuando trocas entre um elemento adjacente e outro
    Fácil de entender e implementar
    Torna-se lento em uma estrutura com grandes dados

    Passos:
    1. Pegue o tamanho da lista/array
    2. Crie 2 laços de repetição, um dentro do outro
    3. O primeiro for vai percorrer de i=0 até o tamanho da lista. Crie a variável "troca" e defina como False
    4. O segundo laço vai percorrer de j=0 até (tamanho da lista - valor atual de i - 1)
    5. Dentro do segundo for haverá uma checagem se lista[j] > lista[j+1]. Se sim haverá troca e a variável "troca" se torna True
    6. Logo após a declaração do segundo for, mas agora dentro do primeiro for faça uma checagem
    se a variável troca é False, se sim dê um comando break e encerre o algoritmo
    7. Por fim retorne a nova lista ordenada 

'''
def bubbleSort(lista):
    tam = len(lista)
    for i in tam:
        troca = False
        for j in range(0,tam-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                troca = True
        if not troca:
            break
    return lista

lista = [8,14,3,25,7,16,4,33]
lista_ordenada = bubbleSort(lista)
print('Lista desordenada: ',lista)
print('Lista ORDENADA: ',lista_ordenada)