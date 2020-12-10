# x = input().split()
# n, k = map(int, x)
# print(n + k)
# 'аналогично'
# n, k = (int(i) for i in x)
# print(n + k)

x = input().split()
xs = map(int, x)
def even(x):
    return x % 2 == 0
evens = filter(even, xs)
print([i for i in evens])
