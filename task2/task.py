
def task(graph: str):
    res = [[], [], [], [], []]

    rdr = [line.split(',') for line in graph.split('\n')]
    lst = []
    #print(rdr)
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

    res = [list(set(el)) for el in res]
    inner_strings = [",".join(str(num) for num in el) for el in res]
    stree = "\n".join(inner_strings)
    return stree


print(task('1,2 \n 1,3 \n 3,4 \n 3,5 \n 4,6'))
