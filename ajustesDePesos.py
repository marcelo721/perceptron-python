import numpy as np

#Testar operador and
#entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#saidas = np.array([0, 0, 0, 1])

#Testar operador and
#entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#saidas = np.array([0, 1, 1, 1])

#Testar operador and
#entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#saidas = np.array([0, 1, 1, 1])

#Testar operador XOR
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 1, 1, 0])

pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(sum):
    if sum >= 1:
        return 1
    else:
        return 0

def sum(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    errorTotal = 1
    while(errorTotal != 0):
        errorTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = sum(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            errorTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('pesso atualizado : ' + str(pesos[j]))
            print('total de erros = ' + str(errorTotal))


treinar()

print("rede neural treinada")
print(sum(entradas[0]))
print(sum(entradas[1]))
print(sum(entradas[2]))
print(sum(entradas[3]))