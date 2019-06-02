def comida():
    N = int(input())
    P = int(input())
    if N==1:
        return P
    else:
        return int(P/(2**(N-1))) + comida1(N-1,P%(2**(N-1)))
def comida1(N,P):
    if N==1:
        return P
    else:
        return int(P/(2**(N-1))) + comida(N-1,P%(2**(N-1)))
