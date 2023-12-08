import numpy as np

def task() -> list:

    A, B = [], []
    for i in range(1,7):
        for j in range(1,7):
            A.append(i*j)
            B.append(i+j)
    B=list(sorted(set(B)))
    A=list(sorted(set(A)))

    keys_B, keys_A = len(B), len(A)
    A_dict, B_dict = {}, {}
    for i in range(keys_A): 
        A_dict[A[i]] = i
    for i in range(keys_B):
        B_dict[B[i]] = i

    matrix = np.zeros((len(B), len(A)))
    for i in range(1, 7):
        for j in range(1, 7):
            matrix[B_dict[i + j], A_dict[i * j]] += 1
    probs = matrix / 36


    # H(AB) - энтропия двух связанных (совместных) событий;
    Hab = 0
    for i in range (len(probs)):
        for j in range (len(probs[0])):
            if probs[i][j] != 0:
                Hab += - probs[i][j] * np.log2(probs[i][j])

    # H(A) - энтропия события А;
    Ha = 0
    A_probs =[]
    for i in range (len(probs)):
        A_probs.append(sum(probs[i]))
    for x in A_probs:
        Ha += - x * np.log2(x)

    # H(B) - энтропия события B;
    Hb = 0
    B_probs = np.sum(probs, axis=0)
    for x in B_probs:
        Hb += - x * np.log2(x)

    # Ha(B) - условная энтропия события B связанного с событием A;
    HaB = Hab - Ha

    # I(A,B) - информация в событии A о событии B.
    Iab = Hb - HaB

    return[round(Hab, 2), round(Ha, 2), round(Hb, 2), round(HaB, 2), round(Iab, 2)]
