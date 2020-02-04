
def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    MAP = [[0]*(friends_nodes+1) for _ in range(friends_nodes+1)]
    num_of_edge = len(friends_from)
    max_interest = -1
    max_cord = (-1, 1)

    prev_wight = -1
    for i in range(num_of_edge):
        MAP[friends_from[i]][friends_to[i]] += 1
        #print(friends_from[i], friends_to[i])

        if MAP[friends_from[i]][friends_to[i]] >= max_interest and prev_wight != friends_weight[i]:
            max_interest = MAP[friends_from[i]][friends_to[i]]

            if friends_from[i]*friends_to[i] > max_cord[0] * max_cord[1]:
                max_cord = (friends_from[i], friends_to[i])
                #print(max_cord[0], max_cord[1])

        prev_wight = friends_weight[i]

    #for arr in MAP:
    #    print(arr)

    return max_cord[0] * max_cord[1]


print(maxShared(4,
                [1, 1, 2, 2, 2],
                [2, 2, 3, 4, 4],
                [1, 2, 1, 3, 3]))
"""

print(maxShared(3,
                [1, 1, 2],
                [3, 3, 3],
                [1, 2, 2])) # 3

print(maxShared(4,
                [1, 1, 2, 2, 2],
                [2, 2, 3, 3, 4],
                [1, 2, 1, 3, 3])) # 6
"""