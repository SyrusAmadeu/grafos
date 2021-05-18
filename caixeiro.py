from math import sqrt
from itertools import permutations

arquivo = input("Informe o nome do arquivo: ")
try:

    with open(arquivo, 'r') as f:
        lines = f.read().split('\n')
    parsed_lines = [list(map(int, line.split(';'))) for line in lines if line != '']
    matrix = {(line[0], line[1]): line[2] for line in parsed_lines}
    tam = int(sqrt(len(matrix)))

    try:

        inicio = int(input("Digite a aresta inicial: "))
        if inicio > tam or inicio < 1:
            print("Aresta não existente")
        else:

            atual = inicio
            n_usados = [i+1 for i in range(tam)]
            n_usados.remove(atual)
            menor_valor = 999
            menor_caminho = 0

            print("   Trajeto  |   Valor")
            for i in permutations(list(n_usados)):
                valor = 0
                for j in range(tam-1):
                    prox = i[j]
                    valor += matrix[(atual,prox)]
                    atual = prox
                if (valor < menor_valor):
                    menor_valor = valor
                    menor_caminho = str(inicio)+''.join(map(str, i))
                print("    "+str(inicio) + ''.join(map(str, i)) + "  |    " + str(valor))
            print('\nMenor caminho: ' + str(menor_caminho) + '\nValor: ' + str(menor_valor))

    except ValueError:
        print("\nCaractere inválido!")

except IOError:
    print("Erro: o arquivo \"%s\" não existe" % arquivo)
