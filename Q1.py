#questao 1
def eq_qua(a,b,c):
    delta = (b * b) - (4*a*c)
    xi = 0
    xii = 0
    if delta < 0:
        print('a funcao possui raizes complexas')
        return 0
    xi = ((-b) + pow(delta,(1/2)))/(2*a)
    xii = ((-b) - pow(delta,(1/2)))/(2*a)

    print('as raizes sao: ', xi, ' e ', xii)
    return 1
#fim
