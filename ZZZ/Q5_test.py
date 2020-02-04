

def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    MAP = [[0]*(friends_nodes+1) for _ in range(friends_nodes+1)]
    max_W = max(friends_weight)
    num_of_edge = len(friends_from)

    for i in range(num_of_edge):
        if MAP[friends_from[i]][friends_to[i]] == 0:
            MAP[friends_from[i]][friends_to[i]] = [friends_weight[i]]
            MAP[friends_to[i]][friends_from[i]] = [friends_weight[i]]

        else:
            if friends_weight[i] not in MAP[friends_from[i]][friends_to[i]]:
                MAP[friends_from[i]][friends_to[i]].append(friends_weight[i])
                MAP[friends_to[i]][friends_from[i]].append(friends_weight[i])

    max_interest = -1
    max_cord = (-1, 1, -1) # x, y, len

    for i in range(1, friends_nodes+1):
        for j in range(1, friends_nodes+1):
            if MAP[j][i] != 0 and len(MAP[j][i]) >= max_interest:
                max_interest = len(MAP[j][i])
                if max_interest >= max_cord[2] and i*j > max_cord[0] * max_cord[1]:
                    max_cord = (i, j, max_interest)

    for arr in MAP:
        print(arr)
    print(max_cord)
    return max_cord[0] * max_cord[1]


if __name__ == '__main__':
    #fptr = open(r'C:\Users\djsdi\Desktop\git-project\LevelUp-Algorithm\ZZZ\Q5_test\est5.txt', 'w')

    friends_nodes, friends_edges = map(int, input().rstrip().split())

    friends_from = [0] * friends_edges
    friends_to = [0] * friends_edges
    friends_weight = [0] * friends_edges

    for i in range(friends_edges):
        friends_from[i], friends_to[i], friends_weight[i] = map(int, input().rstrip().split())

    result = maxShared(friends_nodes, friends_from, friends_to, friends_weight)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()