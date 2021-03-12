"""
    @ Baek 1786 찾기 [Fail]
    @ Prob. https://www.acmicpc.net/problem/1786
      Ref.  https://github.com/jms7446/hackerrank/blob/master/baekjoon/alg-study/w18/p16916.py
    @ Algo: String
    @ Start day: 20. 09. 09.
    @ End day: 20. 09. 09.
"""

import sys


class KMP:
    def __init__(self, ptn):
        self.ptn = ptn
        self.table = self.make_partial_match_table(ptn)

    @staticmethod
    def make_partial_match_table(ptn):
        table = [0] * len(ptn)
        cnd = 0
        for pos in range(1, len(ptn)):
            while cnd > 0 and ptn[pos] != ptn[cnd]:
                cnd = table[cnd - 1]
            if ptn[pos] == ptn[cnd]:
                cnd += 1
                table[pos] = cnd
        return table

    def search(self, in_str):
        ptn = self.ptn
        table = self.table
        len_ptn_minus1 = len(ptn) - 1
        j = 0
        for i, c in enumerate(in_str):
            while j > 0 and c != ptn[j]:
                j = table[j-1]
            if c == ptn[j]:
                if j == len_ptn_minus1:
                    yield i - len(ptn) + 1
                    j = table[j]
                else:
                    j += 1

def main():
    # S = "ABC ABCDAB ABCDABCDABDE"
    # P = "ABCDABD"

    S = input()
    P = input()
    
    kmp = KMP(P)
    
    # T 중간에 P가 몇 번 등장하는지 
    # P가 나타내는 위치 차례대로  
    ans = kmp.search(S)
    res = []
    for a in ans:
        res.append(a)
        
    print(len(res))
    if len(res) == 0: print(0)
    else:
        print(" ".join([str(s+1) for s in res]))


if __name__ == "__main__":
    main()

    
"""
ABC ABCDAB ABCDABCDABDE
ABCDABD
>
1 
16
"""
