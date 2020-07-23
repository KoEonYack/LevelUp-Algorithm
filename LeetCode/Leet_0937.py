"""
    @ 937. Reorder Data in Log Files
    @ Prob. https://leetcode.com/problems/reorder-data-in-log-files/
     Ref.
    @ Algo: 구현
    @ Start day: 20. 07. 23.
    @ End day: 20. 07. 23.
"""

def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    l, d = [], []
    for log in logs:
        if log.split()[1].isdigit():
            d.append(log)
        else:
            l.append(log)
    l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return l + d

reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])