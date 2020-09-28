"""
    @Baek 11426 접두사 찾기
    @Prob. https://www.acmicpc.net/problem/14426
    @Source. https://www.acmicpc.net/source/22249026
    @Algo. Tire
"""


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[
                char]
        curr_node.data = string

    def starts_with(self, prefix):
        curr_node = self.head
        subtrie = None

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                subtrie = curr_node
            else:
                return None
        if subtrie == None:
            return False
        else:
            return True

import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))
ans = 0

trie = Trie()

for i in range(n):
    trie.insert(sys.stdin.readline().strip())
for j in range(m):
    if trie.starts_with(sys.stdin.readline().strip())==True:
        ans+=1
print(ans)