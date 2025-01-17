import numpy as np
from numpy.linalg import norm

def irls(x,D,p,eps=10**-4,iterMax=100):
    n,k=np.shape(D)
    alpha=np.eros(k)
    Q=np.zeros((k,k))
    it=0
    #initialisation de alpha
    alpha0=D.T@np.inv(D@D.T)@x
    test=True
    #Boucle principale
    while test and it<iterMax:
        #construction de la matrice Q
        for i in range(k):
            z=(np.abs(alpha0[i])**2+eps)**(p/2-1)
            Q[i,i]=1/z
            #calcul du nouvel alpha
            alpha=Q@D.T@np.inv(D@D@D.T)@x
            #critère d'arrêt:
            if norm(alpha-alpha0)<np.sqrt(eps)/100 and eps<10**(-8):
                test= False
            else:
                eps=eps/10
                alpha0=alpha
                it=+1

    return alpha, it