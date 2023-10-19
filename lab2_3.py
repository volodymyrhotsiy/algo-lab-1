def FindSquare(N, W, H):
    i = 1

    j = max(W, H) * N

    while i < j:
        mid = i + (j - i) // 2

        if (mid // W) * (mid // H) >= N:
            j = mid

        else:
            i = mid + 1

    return j


N, W, H = 9000, 1000000000, 999999999
print(FindSquare(N, W, H))  