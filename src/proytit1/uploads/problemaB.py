def partida():
    aux = input().split(" ")
    aux1 = input().split(" ")
    N=int(aux[0])
    P=int(aux[1])
    A=int(aux1[0])
    B=int(aux1[1])
    puntajeA=0
    puntajeB=0
    turno=0
    if P==1:
        while puntajeA<N and puntajeB<N:
            if turno%2==0:
                puntajeA=puntajeA+A
                if puntajeA<N:
                    puntajeB=puntajeB+1
            else:
                puntajeB=puntajeB+B
                if puntajeB<N:
                    puntajeA=puntajeA+1
            if puntajeA<N and puntajeB<N:
                turno=turno+1
        if puntajeA>=N:
            print("1")
        else:
            print("2")
    else:
        while puntajeA<N and puntajeB<N:
            if turno%2==0:
                puntajeB=puntajeB+B
                if puntajeB<N:
                    puntajeA=puntajeA+1
            else:
                puntajeA=puntajeA+A
                if puntajeA<N:
                    puntajeB=puntajeB+1
            if puntajeA<N and puntajeB<N:
                turno=turno+1
        if puntajeB>=N:
            print("2")
        else:
            print("1")
