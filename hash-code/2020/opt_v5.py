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

        # position of the first book not in the score
        self.till = min((nof_days - signup) * self.rate, self.nof_books)
        # number of books in score
        self.in_score = self.till
        # initialize lib value
        self.score = 0
        for book_idx in books[:self.till]:
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
                other_lib = libs[other_lib_idx]
                other_lib.books[loc] = -1             # invalidate book sent
                other_lib.nof_books -= 1              # update books count
                if loc < other_lib.till:
                    other_lib.score -= values[book_idx]   # update lib score
                    other_lib.in_score -= 1               # update books in score count

    lib.score = 0
    for other_lib in libs:
        # update libs we didn't submit yet
        if not other_lib.sent:
            to_capacity = (nof_days - startup - other_lib.signup) * other_lib.rate - other_lib.in_score # number of books to add to meet capacity
            available = other_lib.nof_books - other_lib.in_score                        # number of books available to add
            # move till right when there is room to increase the score
            if to_capacity > 0 and available > 0:
                to_add = min(available, to_capacity)
                offset = 0
                for book_idx in other_lib.books[other_lib.till:]:
                    # stop adding books when we don't need more
                    if not to_add:
                        break
                    # consider only books not removed
                    if book_idx != -1:
                        other_lib.score += values[book_idx] # update lib score
                        other_lib.in_score += 1             # update number of books in score
                        to_add -= 1
                    offset += 1
                other_lib.till += offset
            # move till left based on the lower number of days available
            if to_capacity < 0:
                to_unscore = -to_capacity
                offset = 0
                for book_idx in other_lib.books[:other_lib.till:-1]:
                    # stop unscoring books when we don't need more
                    if not to_unscore:
                        break
                    # consider only books not removed
                    if book_idx != -1:
                        other_lib.score -= values[book_idx] # update lib score
                        other_lib.in_score -= 1             # update number of books in score
                        to_unscore -= 1
                    offset -= 1
                other_lib.till += offset

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
