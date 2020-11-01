from queue import Queue

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


tests = int(input())
for test in range(1, tests + 1):
    n, k = map(int, input().split())
    trie = TrieNode()
    for _ in range(n):
        add(trie, input())
    # avoid counting the empyy prefix
    trie.counter = 0

    answer = 0
    to_walk = Queue()
    to_walk.put(trie)
    while not to_walk.empty():
        node = to_walk.get()
        answer += int(node.counter / k)
        for child in node.children.values():
            to_walk.put(child)
    print("Case #{}: {}".format(test, answer))
    