
#
# def fib(n):
#     numbers = []
#     current, nxt = 0, 1
#     while len(numbers) < n:
#         current, nxt = nxt, current + nxt
#         numbers.append(current)
#
#     return numbers
#
#
# print(fib(10))


def fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


for item in fib():
    print(item, end=',')
    if item > 1000:
        break


