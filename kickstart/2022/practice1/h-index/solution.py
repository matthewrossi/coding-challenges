def solve(citations):
    h_indexes = []
    h_index = 0
    counter = [0 for _ in range(10**5 + 1)]
    interesting_papers = 0

    for citation in citations:
        if citation > h_index:
            counter[citation] += 1
            interesting_papers += 1
        if interesting_papers == h_index + 1:
            h_index += 1
            interesting_papers -= counter[h_index]
        h_indexes.append(h_index)
    return h_indexes


if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        nof_pubs = int(input())
        citations = map(int, input().split())
        h_indexes = solve(citations)
        print("Case #{}: {}".format(test, " ".join(map(str, h_indexes))))