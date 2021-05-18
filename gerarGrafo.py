from random import randrange

print("Seu grado possui apenas 6.\nOs valores serão gerados aleatoriamente")
r_gen = lambda : randrange(10,25)
matrix = {(i, j) : str(r_gen()) for i in range(6) for j in range(6)}
matrix = {(i, j) : "00" if i == j else value for (i, j), value in matrix.items()}
for (i, j), value in matrix.items():
    if i > j:
        matrix[(i, j)] = matrix[(j,i)]

try:
    arquivo = input("Digite o nome que vai dar ao seu arquivo: ")
    with open(arquivo, 'w') as f:
        for (i,j), value in matrix.items():
            if i == 5 and j == 5:
                f.write("0" + str(i+1) + ";0"+ str(j+1) + ";" + matrix[(i,j)])
            else:
                f.write("0" + str(i+1) + ";0"+ str(j+1) + ";" + matrix[(i,j)] + "\n")
    print("Grafo gerado com sucesso!")
except IOError:
    print("Erro inexperado!")
