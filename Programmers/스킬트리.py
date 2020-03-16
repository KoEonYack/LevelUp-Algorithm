def solution(skill, skill_trees):
    ans = 0

    for skill_tree in skill_trees:
        tmp = []
        fine = True
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
               tmp.append(skill_tree[i])

        for i in range(len(tmp)):
            if tmp[i] != skill[i]:
                fine = False
                break

        if fine is True:
            ans += 1

    return ans


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))