from collections import defaultdict

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Library(object):
    def __init__(self, idx, nof_books, signup, rate, books):
        self.idx = idx
        self.nof_books = nof_books
        self.signup = signup
        self.rate = rate
        self.books = books
        self.startup = float("inf")

nof_books, nof_libs, nof_days = map(int, input().split())
values = tuple(map(int, input().split()))
libs = []
for lib_idx in range(nof_libs):
    books_in_lib, signup, rate = map(int, input().split())
    books = map(int, input().split())

    lib = Library(idx=lib_idx, nof_books=books_in_lib, signup=signup, rate=rate, books=books)
    libs.append(lib)

# a: any order just avoid duplicate books
# b: books have equal values, libraries have same number of books and rate (order on signup)
# c: number of books between 10 and 20, rate always > 210, so all books are sents within a day (order on signup and books value)
#    books reps goes from 0 to 9, from 1 to 9 reps decreases
# d: books, signup, rate equal, libraries have number of books from 1 to 14 so all books are sents within a day
#    books reps from 2 to 3 (only repetition problem)
# e: multiple book values and number of libs, signup 1 to 10 (~100), 1/2 rate (~500), reps 0 to 18
# f: multiple book values, number of libs and singup, rate 5-10 (~160), reps 0 to 17

total = 0
for lib in libs:
    total += lib.signup
print(f"days = {nof_days} total = {total}")

# DISTRIBUTION
values_distrib = {}
for v in values:
    values_distrib[v] = values_distrib.get(v, 0) + 1
#print(f"values_distrib = {values_distrib}")
print(f"len(values_distrib) = {len(values_distrib)}")

nof_books_distrib = {}
for lib in libs:
    nof_books_distrib[lib.nof_books] = nof_books_distrib.get(lib.nof_books, 0) + 1
#print(f"nof_books_distrib = {nof_books_distrib}")
print(f"len(nof_books_distrib) = {len(nof_books_distrib)}")
print(f"max(nof_books_distrib) = {max(nof_books_distrib)}")

signup_distrib = {}
for lib in libs:
    signup_distrib[lib.signup] = signup_distrib.get(lib.signup, 0) + 1
#print(f"signup_distrib = {signup_distrib}")
print(f"len(signup_distrib) = {len(signup_distrib)}")

rate_distrib = {}
for lib in libs:
    rate_distrib[lib.rate] = rate_distrib.get(lib.rate, 0) + 1
print(f"rate_distrib = {rate_distrib}")
print(f"len(rate_distrib) = {len(rate_distrib)}")
print(f"min(rate_distrib) = {min(rate_distrib)}")

# BOOKS OVERLAP
books_rep = defaultdict(set)
for lib in libs:
    for book_idx in lib.books:
        books_rep[book_idx].add(lib.idx)

rep_distrib = {}
for key, value in books_rep.items():
    rep_distrib[len(value)] = rep_distrib.get(len(value), 0) + 1
print(f"rep_distrib = {rep_distrib}")
print(f"not_repeated = {nof_books - sum(rep_distrib.values())}")
print(f"len(rep_distrib) = {len(rep_distrib)}")
