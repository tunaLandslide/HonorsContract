import numpy as np
import random as rn

def portText(file):
    """This function imports a text file as a reference"""
    with open(file,'r') as tex:
        ref = tex.read().split()
    return ref

def portMat(file):
    """This funciton imports an already existing matrix to describe the
    probabilities of each word occuring with relation to each other"""
    with open(file,'r') as t:
        q = t.read().split("\n")
    l = len(q) - 1
    voc = q[-1].split()
    M = np.zeros((l,l))
    for i in range(l):
        for j in range(l):
            M[i,j] = q[i].split()[j]

    return voc,M

def expMat(name,voc,M):
    """This funciton exports an already existing matrix to describe the
    probabilities of each word occuring with relation to each other"""
    doc = open(name,'w+')
    s = ""
    for i in range(len(M)):
        for j in range(len(M)):
            s += str(M[i,j])
            s += " "
        s += "\n"
    for i in range(len(voc)):
        s += voc[i]
        s += " "
    doc.write(s)
    doc.close()
    print("{0} created.".format(name))

def getMat(ref):
    """Creates the matrix to get the probabilities needed to generate sentences"""
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
    """Generates a sentence based on a given vocabulary and matrix"""
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
