from disjoint_set import DisjointSet

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_cherries, nof_black = map(int, input().split())

    forest = DisjointSet()
    count = 0
    for i in range(nof_black):
        c, d = map(int, input().split())
        forest.find(c)
        forest.find(d)
        if not forest.connected(c,d):
            forest.union(c,d)
            count += 1

    nof_sets = 0
    nof_vertex = 0
    for subset in forest.itersets():
        nof_sets += 1
        nof_vertex += len(subset)
    
    print("Case #{}: {}".format(test, count + 2 * ((nof_sets - 1) + (nof_cherries - nof_vertex))))
