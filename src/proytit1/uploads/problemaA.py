def Ajedrez():
    P=int(input())
    aux = input().split(" ")
    aux1= input().split(" ")
    x1 = int(aux[0])
    y1 = int(aux[1])
    x2 = int(aux1[0])
    y2 = int(aux1[1])
    if P == 1:
        if x1-x2==0 or y1-y2==0:
            return 1
        else:
            return 2

    elif P == 2:
        if ((x1+y1)%2==0 and (x2+y2)%2==1) or ((x1+y1)%2==1 and (x2+y2)==0):
            return -1
        elif abs(x1-x2)==abs(y1-y2):
            return 1
        else:
            return 2
            
    elif P == 3:
        if x1-x2==0 or y1-y2==0 or abs(x1-x2)==abs(y1-y2):
            return 1
        else:
            return 2
        
    elif P == 4:
        if x1-x2 == 0 and not (y1-y2 == 0):
            return abs(y1-y2)
        elif not (x1-x2==0) and y1-y2==0:
            return abs(x1-x2)
        elif abs(x1-x2)==abs(y1-y2) or abs(x1-x2)>abs(y1-y2):
            return abs(x1-x2)
        elif abs(x1-x2)<abs(y1-y2):
            return abs(y1-y2)
        else:
            return -1

    else:
        i = 0
        aux = 0
        while not x1==x2 and y1==y2:
            if x1+1==x2:
                if y1+2==y2:
                    i=i+1
                    x1=x1+1
                    y1=y1+2
                elif y1-2==y2:
                    i=i+1
                    x1=x1+1
                    y1=y1-2

            elif x1+2==x2:
                if y1+1==y2:
                    i=i+1
                    x1=x1+2
                    y1=y+1
                elif y1-1==y2:
                    i=i+1
                    x1=x1+2
                    y1=y1-1

            elif x1-2==x2:
                if y1+1==y2:
                    i=i+1
                    x1=x1-2
                    y1=y1+1
                elif y1-1==y2:
                    i=i+1
                    x1=x1-2
                    y1=y1-1

            elif x1-1==x2:
                if y1+2==y2:
                    i=i+1
                    x1=x1+1
                    y1=y1+2
                elif y1-2==y2:
                    i=i+1
                    x1=x1-1
                    y1=y1-2
            
            return i
