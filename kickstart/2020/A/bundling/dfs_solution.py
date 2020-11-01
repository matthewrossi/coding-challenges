class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.valid_word = False
        self.counter = 1
    

def add(root, word):
    node = root
    for char in word:
        if char in node.children:
            node = node.children[char]
            node.counter += 1
        else:
            node.children[char] = TrieNode()
            node = node.children[char]
    node.valid_word = True


def walk(node, k):
    answer = 0
    for child in node.children.values():
        answer += int(child.counter / k) + walk(child, k)
    return answer


tests = int(input())
for test in range(1, tests + 1):
    n, k = map(int, input().split())
    trie = TrieNode()
    for _ in range(n):
        add(trie, input())
    print("Case #{}: {}".format(test, walk(trie, k)))
    