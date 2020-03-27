"""
    Ref. https://deque.tistory.com/78
         https://www.youtube.com/watch?v=cH-5KcgUcOE
    2020. 03. 27
"""

def KMP():
    M = len(pat)
    N = len(txt)

    i = 0
    j = 0
    while i < N:
        if pat[j] == txt[i]:
            j += 1
            i += 1

        if j == M:
            # Found pattern i - j index
            print("count")
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArr():
    l = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        elif pat[i] != pat[l]:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1

txt = input()
pat = input()
lps = [0] * len(pat)

computeLPSArr()
KMP()


"""
baekjoon
aek
>
1
-----------------
baekjoon
bak
>
0
"""