def solution(goods, boxes):
    answer = 0
    goods.sort(reverse=True)
    boxes.sort(reverse=True)
    answer_box_idx = []
    answer_goods_idx = []


    for i in range(len(boxes)):
        for j in range(len(goods)):
            if boxes[i] >= goods[j] and (i not in answer_box_idx) and (j not in answer_goods_idx):
                answer_box_idx.append(i)
                answer_goods_idx.append(j)

    return len(answer_box_idx)


a = solution([5,3,7], [3,7,6])
a = solution([5,3,7], [3,7,6])
print(a)