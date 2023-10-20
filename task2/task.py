
def task(graph: str) -> list:
    res = [[], [], [], [], []]

    rdr = [line.split(',') for line in graph.split('\n')]
    lst = []
    for i in range(len(rdr)):
        node1 = int(rdr[i][0])
        node2 = int(rdr[i][1])
        lst.append((node1, node2))
        res[0].append(node1)  # родители
        res[1].append(node2)  # дети

    for i in range(len(lst)):
        node1, node2 = lst[i]
        if node2 in res[0]:
            res[2].append(node1)  # есть внуки
        if node1 in res[1]:
            res[3].append(node2)  # есть прародители
        if res[0].count(node1) > 1:
            res[4].append(node2)  # >1 детей

    return [list(set(el)) for el in res]


print(task('1,2 \n 1,3 \n 3,4 \n 3,5 \n 4,6'))
