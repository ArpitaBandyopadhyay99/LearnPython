from functools import reduce

nums = [2, 5, 4, 7, 6]


# use normal function
def is_even(n):
    return n % 2 == 0


even_s = list(filter(is_even, nums))
print(even_s)

# use lambda for this method
odd_s = list(filter(lambda n: n % 2 != 0, nums))
print("lambda: ", odd_s)
doubles = list(map(lambda i: i * 2, odd_s))
print("map: ", doubles)


def fetch_sum(a, b):
    return a + b


# sum = reduce(fetch_sum, odd_s)
sum = reduce(lambda i, j: i+j, odd_s)
print("list: ", odd_s, "sum: ", sum)
