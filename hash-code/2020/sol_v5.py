from collections import defaultdict
from operator import attrgetter

class Library(object):
    def __init__(self, idx, nof_books, signup, rate, books):
        self.idx = idx
        self.nof_books = nof_books
        self.signup = signup
        self.rate = rate
        self.books = books
        self.sent = set()
        self.compute_score(0)
        self.done = False

    def compute_score(self, startup):
        till = min((nof_days - startup - self.signup) * self.rate, self.nof_books)
        self.score = 0
        valid_books = [book_idx for book_idx in self.books if book_idx != -1]
        for book_idx in valid_books[:till]:
            self.score += values[book_idx]

nof_books, nof_libs, nof_days = map(int, input().split())
values = tuple(map(int, input().split()))
libs = []
book_loc = defaultdict(dict)
for lib_idx in range(nof_libs):
    books_in_lib, signup, rate = map(int, input().split())
    books = list(map(int, input().split()))
    books.sort(key=lambda x: values[x], reverse=True)
    # construct data structure to update books availability on libs
    for loc in range(len(books)):
        book_idx = books[loc]
        book_loc[book_idx][lib_idx] = loc
    lib = Library(idx=lib_idx, nof_books=books_in_lib, signup=signup, rate=rate, books=books)
    libs.append(lib)

score = startup = 0
lib = max(libs, key=lambda x: x.score / x.signup)
libs_order = []
while lib.score:
    libs_order.append(lib)
    startup += lib.signup
    nof_sent = min((nof_days - startup) * lib.rate, lib.nof_books)
    for book_idx in lib.books:
        # stop sending books on saturation
        if len(lib.sent) == nof_sent:
            break
        # consider only books not removed
        if book_idx != -1:
            lib.sent.add(book_idx)
            score += values[book_idx]
            # remove book from other libs
            for other_lib_idx, loc in book_loc[book_idx].items():
                libs[other_lib_idx].books[loc] = -1             # invalidate book sent
                libs[other_lib_idx].nof_books -= 1              # update books count
    lib.done = True
    lib.score = 0
    for lib in libs:
        if not lib.done:
            lib.compute_score(startup)
    lib = max(libs, key=lambda x: x.score / x.signup)

sending_libs = [lib for lib in libs_order if lib.sent]
print(len(sending_libs))
for lib in sending_libs:
    print(f"{lib.idx} {len(lib.sent)}")
    print(" ".join(map(str, list(lib.sent))))

# a: any order just avoid duplicate books
# b: books have equal values, libraries have same number of books and rate (order on signup)
# c: number of books between 10 and 20, rate always > 210, so all books are sents within a day (order on signup and books value)
#    books reps goes from 0 to 9, from 1 to 9 reps decreases
# d: books, signup, rate equal, libraries have number of books from 1 to 14 so all books are sents within a day
#    books reps from 2 to 3 (only repetition problem)
# e: multiple book values and number of books per lib, signup 1 to 10 (~100), 1/2 rate (~500), reps 0 to 18
# f: multiple book values, number of books per lib and singup, rate 5-10 (~160), reps 0 to 17

# APPROXIMATELY SOLVES E, F (solves knapsack with score density)
