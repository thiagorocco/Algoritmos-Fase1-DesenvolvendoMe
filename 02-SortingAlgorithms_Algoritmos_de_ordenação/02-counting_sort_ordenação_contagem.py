# Programa para ordenação por contagem

#A função principal que ordenar deixará a string arr in ordem alfabética


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
