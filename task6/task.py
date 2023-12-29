import json
import numpy as np

def task(f):
    data = [json.load(item) for item in f]
    ranking = [[] for _ in f]

    for i, sublist in enumerate(data):
        weight = 1
        for item in sublist:
            if isinstance(item, list):
                for el in item:
                    ranking[i].append(weight)
            else:
                ranking[i].append(weight)
            weight += 1

    ranking = np.array(ranking)
    rank_sum = ranking.sum(axis=0)
    dif_sq = []
    for i in range(len(rank_sum)):
        dif_sq.append(np.power(rank_sum[i] - rank_sum.sum()/len(rank_sum), 2))
    disp = sum(dif_sq)/len(rank_sum)-1
    return disp

def main():
    d1 = task([open("Ранжировка  A.json"), open("Ранжировка  B.json")])
    d2 = task([open("Ранжировка  A.json"), open("Ранжировка  C.json")])
    W1 = d1 / max(d1, d2)
    W2 = d2 / max(d1, d2)
    print(W1)
    print(W2)

if __name__ == "__main__":
    main()