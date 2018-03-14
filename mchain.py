import numpy as np
import random as rn

def portText(file):
    tex = open(file,'r')
    ref = tex.read().split()
    tex.close()
    return ref

def portMat(file):
    return "Uh... I'll work on this..."

def getMat(ref):
    voc = list(set(ref))
    M = np.zeros((len(voc),len(voc)))

    for n in range(len(ref) - 1):
        for m in range(len(voc)):
            if ref[n] == voc[m]:
                M[voc.index(ref[n + 1]),m] += 1

    for n in range(len(voc)):
        if sum(M[:,n]) == 0:
            M[:,n] += 1

    return voc,M

def genSent(voc,M,N = 1):
    s = ""
    q = 0

    caps = []
    W = np.zeros((len(voc)))
    for n in range(len(voc)):
        W[n] = sum(M[:,n])
        if voc[n][0].isupper():
            caps.append(n)

    a = caps[rn.randint(0,len(caps) - 1)]

    while q < N:
        s += voc[a]
        s += " "

        if voc[a][-1] in ['.','?','!']:
            q += 1

        b = rn.randint(1,W[a])
        c = 0
        while b > 0:
            b -= M[c,a]
            c += 1
        a = c - 1

    return s
