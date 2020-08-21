"""
    T-Q2
    Start: 20. 08. 21.
    End:  20. 08. 21.
"""

data = {"(": ")",
       "{": "}",
       "[": "]"}

S = list(input())
for i, ch in enumerate(S):
    if ch == "-":
        S[i] = S[i-1]
S = S[::-1]

for i, ch in enumerate(S):
    if ch == "+":
        S[i] = S[i-1]
S = S[::-1]
print(S)


stack = []
for ch in S:
    if ch in data:
        stack.append(ch)
    else:
        if data[stack[-1]] == ch:
            stack.pop()

print(True if len(stack) == 0 else False)


"""
()((({})({}[]]
False

((((--+++)))(())
True
"""