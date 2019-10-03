#questao 4
def nob(num_a, num_b):
    a = num_a//10
    b = num_a%10
    c = num_b//10
    d = num_b%10

    resposta = a + b + c+ d

    return resposta

def main():
    resp = nob(21,36)

    print(resp)

main()