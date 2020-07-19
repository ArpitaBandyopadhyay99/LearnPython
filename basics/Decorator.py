# decorator - user can pass first < second but you need to pass first > second in div()
# without touching the original div()


def div(a, b):
    return a/b


def decorator_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


first = int(input("First element: "))
second = int(input("Second element: "))
div = decorator_div(div)
result = div(first, second)
print(first, " / ", second, " = ", result)
