#questao 3
def pi():
    anterior = 0
    prox_imp = 1
    pi = 4*(1/prox_imp)
    anterior = -1000000
    while abs(pi-anterior) > (5*pow(10,-8)):
        anterior = pi
        
        if(prox_imp < 0):
            prox_imp = (abs(prox_imp) + 2)
        else:
            prox_imp = -(prox_imp + 2)
        
        pi = pi + (4 * (1/(prox_imp)))
    print(pi)
#fim