from task2.task import task as t
import numpy as np


def task(str_csv: str):
    lines = str_csv.split("\n")
    lst = [list(map(int, line.split(","))) for line in lines]

    enthropy = 0
    n = len(lst)
    for el in lst:
        for num in el:
            p = num / (n-1)
            if p > 0:
                enthropy -= p * np.log2(p)

    return enthropy


res = t('1,2 \n 1,3 \n 3,4 \n 3,5 \n 4,6')
res2 = task(res)
print(res2)
