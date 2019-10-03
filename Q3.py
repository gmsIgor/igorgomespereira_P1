#questao 3
def pi():
    anterior = 0
    aux = True
    prox_imp = 1
    pi = 4*(1/prox_imp)
    anterior = pi

    while aux:

        prox_imp += 2
        pi=(pi)*(1/prox_imp)
        diferenca = abs(pi) - abs(anterior)
        dif_str = str(diferenca)

        if (len(dif_str) == 10) and (int(dif_str[len(dif_str - 1)]) > 5):
            aux = False
        elif len(dif_str) > 10:
            aux = False
        anterior = pi

    print(pi)