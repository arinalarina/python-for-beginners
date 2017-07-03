N = int(input())
M = N % 60
H = int(((N - M)/60) % 24)
print(H, M)
