'''
    @ 31. 탄화수소 질량
    @ Idea.
    @ TestCase:
        input: C2H4
        output: 28

        input: CH4
        output: 16
    @ Start day: 19. 10. 09
    @ End day: 19. 10. 09
'''

a = "C2H"
a = a + "0"
result = 0
if a[1] == "H": # H
    result += 1
else:
    result += int(a[1]) * 12
if a[a.index("H") + 1] == "0": # H
    result += 1
else:
    result += int(a[a.index("H") + 1])

print(result)
