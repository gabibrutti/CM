#Questão 1: implemente uma função que inverta as diagonais de uma matriz quadrada.

def inverter_diagonais(matriz):
    tamanho = len(matriz)
    for i in range(tamanho):
        diagonal_principal = matriz[i][i]
        diagonal_secundaria = matriz[i][tamanho - i - 1]
        matriz[i][i] = diagonal_secundaria
        matriz[i][tamanho - i - 1] = diagonal_principal
    return matriz

# Exemplo de matriz 3x3
matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Chamando a função para inverter as diagonais
matriz_invertida = inverter_diagonais(matriz_original)

#resultado
for linha in matriz_invertida:
    print(linha);