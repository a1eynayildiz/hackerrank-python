t = '-'
s = '.|.'
N, M = map(int, input().split())
for i in range(1, N, 2):
    print((s * i).center(M, t))
print("WELCOME".center(M, t))
for i in range(N - 2, 0, -2):
    print((s * i).center(M, t))
