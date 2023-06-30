#2: implemente uma função que, dado uma matriz A e uma submatriz B (dimensões menores que A), 
#esta função retorne quantas vezes esta submatriz B pode ser encontrada na matriz A.

def contar_ocorrencias_submatriz(matriz_principal, submatriz):
    ocorrencias = 0
    linhas_principal = len(matriz_principal)
    colunas_principal = len(matriz_principal[0])
    linhas_submatriz = len(submatriz)
    colunas_submatriz = len(submatriz[0])

    # Percorre todas as posições possíveis na matriz principal
    for i in range(linhas_principal - linhas_submatriz + 1):
        for j in range(colunas_principal - colunas_submatriz + 1):
            # Verifica se a submatriz é igual à submatriz correspondente na matriz principal
            if matriz_principal[i:i+linhas_submatriz] == submatriz:
                ocorrencias += 1

    return ocorrencias


# Exemplo de uso
matriz_principal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]

submatriz = [
    [1, 2],
    [5, 6]
]

# Chamando a função para contar a ocorrência da submatriz na matriz principal
ocorrencias = contar_ocorrencias_submatriz(matriz_principal, submatriz)

#resultado
print("A submatriz ocorre", ocorrencias, "vezes na matriz principal.");
