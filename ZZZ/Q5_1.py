
def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    max_W = max(friends_weight)
    num_of_edge = len(friends_from)
    #MAP = [[False]*(friends_nodes+1) for _ in range(max_W)]

    Connections = []
    for i in range(max_W+1):
        Connections.append([])
    for i in range(num_of_edge):
        if friends_from[i] not in Connections[friends_weight[i]]:
            Connections[friends_weight[i]].append(friends_from[i])
        if  friends_to[i] not in Connections[friends_weight[i]] :
            Connections[friends_weight[i]].append(friends_to[i])

    max_len = -1
    ans = -1
    for i in range(1, max_W+1):
        if len(Connections[i]) > max_len:
            max_len = len(Connections[i])
            if Connections[i][-2] * Connections[i][-1] > ans:
                ans = Connections[i][-2] * Connections[i][-1]

        print(Connections[i])

    #for arr in MAP:
    #    print(arr)

    return ans








print(maxShared(3,
                [1, 1, 2],
                [3, 3, 3],
                [1, 2, 2])) # 3

"""
print(maxShared(4,
                [1, 1, 2, 2, 2],
                [2, 2, 3, 4, 4],
                [1, 2, 1, 3, 3]))


print(maxShared(4,
                [1, 1, 2, 2, 2],
                [2, 2, 3, 3, 4],
                [2, 3, 1, 3, 4])) # 6


print(maxShared(5,
                [1, 1, 2, 2, 2, 4, 4],
                [2, 2, 3, 3, 4, 5, 5],
                [1, 2, 1, 3, 3, 1, 2])) # 20
"""
