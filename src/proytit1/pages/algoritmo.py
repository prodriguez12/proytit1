import os

def organizador(ruta_entrada, ruta_salida):
    archivo = open(ruta_entrada,'r')
    linea = archivo.readline()
    aux=linea.split(" ")
    horaTotal=int(aux[0])
    minutoTotal=int(aux[1])
    h = 0
    m = 0
    s = 0
    linea = archivo.readline()
    N = int(linea)
    M = 0
    while N>0:
        N = N-1
        M = M+1
        linea = archivo.readline()
        aux = linea.split(" ")
        s = s + int(aux[1])
        if s > 60:
            m = m + 1
            s = s - 60

        if int(aux[0])>60:
            h = h + int(aux[0])/60
            m = m + int(aux[0])%60
        else:
            m = m + int(aux[0])
        if m > 60:
            h = h + 1
            m = m - 60

        if horaTotal<h and minutoTotal<m:
            N=0
    salida = open(ruta_salida, 'w')
    salida.write("Despues de "+str(M)+" vueltas el tiempo total del recorrido es: "
                 +str(h)+":"+str(m)+":"+str(s)+".")
