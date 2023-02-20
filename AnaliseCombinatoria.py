import itertools


def QtdeModelos():
    modelo = ["central multimídia", "rodas de liga leve", "bancos de couro"]
    arr = []

    for r in range(0, len(modelo) + 1):
        comb = itertools.combinations(modelo, r)


        for c in comb:
            arr.append(c)

    return arr


calculo = 1000 / (len(QtdeModelos()) * 2 * 7)

print("Com a utilização da biblioteca itertools podemos visualizar exatamente as combinações")
number = 0
for i in QtdeModelos():
    number = number + 1
    print(number, i)

print("______________________________________________________________________________________________________")
print("Resposta: ")
print("Portanto:  1000 / (", len(QtdeModelos()), "x 7 x 2) = ", calculo)
print("São necessárias ", round(calculo), "cores")
print("_______________________________________________________________________________________________________")
