# Programa para ordenação por contagem

#A função principal que ordenar deixará a string arr in ordem alfabética
'''
    Passos para ordenar por contagem
    1. Obtenha o tamanho do vetor desordenado
    2. Crie um vetor de contagem de 0 a 9 para elementos números ou 0 a 255 para caracteres
    3. Inicialize o vetor de contagem com todos os elementos em 0 ou vazio
    4. Percorra cada elemento do array desordenado, ao encontrar o elemento incremente
    a posição correspondente ao seu valor em +1. Ex: Achou 2 incremente a posição 2 com +1
    5. Agora esse array de contagem precisa ter cada um dos seus termos somados com a 
    posição anterior respectivamente. Ex: 0,2,2,0 -> 0,2,4,4
    6. Crie um novo array de resultado com o mesmo número de elementos do array desordenado
    7. Percorra cada elemento do array desordenado de trás para frente. A cada elemento
    checado verifique qual o valor está associado no array de contagem.
    Ex: Elemento 2 do array desordenado possui no array de contagem o valor 4.
    Dessa forma o valor 2 será inserido na posição 4 do array resultado.
    8. Depois de inserir o valor no array resultado é preciso decrementar em -1
    o valor associado no array de contagem, então se na posição 2 tinha-se 4, agora terá 3
'''


def ordenacaoContagem(arr):

    # o array de saída(output) que terá arr ordenado
    output = [0 for i in range(len(arr))]

    # Crie um array contador que guarde a contagem dos caracteres individuais e inicialize a contagem do array como O
    count = [0 for i in range(256)]

    # Para armazenar o resultado resultante, pois a string é variável
    #Nesse caso "ans" terá o mesmo número de elementos de "arr"
    #e iniciará todos eles com vazio("")  
    ans = ["" for _ in arr]

    #Varra o array "arr" pegando cada elemento dele com i
    #A cada interação uma posição de count será incrementada, essa posição será com base
    #no código ascii do valor de i. Pois um array pode conter números, letras e caracteres
    for i in arr:
        count[ord(i)] += 1

    #Mude count[i] para que count[i] agora tenha a posição atual desse caracterer no array de saída
    for i in range(256):
        count[i] += count[i-1]

    #Construa o array de caracteres de saída
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copie o array de saída para arr, 
    # de modo que arr agora contenha os caracteres ordenados
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "abacate"
ans = ordenacaoContagem(arr)
merge_chars = "".join(ans)

print('Array "desordenado":', arr)
print("Array \"ordenado\": % s" % (merge_chars))
