B=[1,2,3]
A=[]
E=[]
def TOI(N,B,A,E):
    if(N==1):
        print str(B)+' '+str(A)+' '+str(E)
    else:
        TOI(N-1,B,E,A)
        if(B):
            TOI(1,B,A,E)
        TOI(N-1,A,B,E)
TOI(3,B,A,E)