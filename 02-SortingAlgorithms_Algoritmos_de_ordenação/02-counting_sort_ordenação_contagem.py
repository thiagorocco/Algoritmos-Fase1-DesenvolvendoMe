# Programa para ordenação por contagem

#A função principal que ordenar deixará a string arr in ordem alfabética


def ordenacaoContagem(arr):

    # o array de saída(output) que terá arr ordenado
    output = [0 for i in range(len(arr))]

    # Crie um array contador que guarde a contagem dos caracteres individuais e inicialize a contagem do array como O
    count = [0 for i in range(256)]

    # Para armazenar o resultado resultante, pois a string é variável
    ans = ["" for _ in arr]

    # Armazena a contagem de cada caractere
    for i in arr:
        count[ord(i)] += 1

    #Mude count[i] para que count[i] agora contenha a posição atual desse caracterer no array de saída
    for i in range(256):
        count[i] += count[i-1]

    #Construa o array de caracteres de saída
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copie o array de saída para arr, de modo que arr agora contenha os caracteres ordenados
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

arr = "bananasplit"
ans = ordenacaoContagem(arr)
merge_chars = "".join(ans)

print('Array "desordenado":', arr)
print("Array \"ordenado\": % s" % (merge_chars))
