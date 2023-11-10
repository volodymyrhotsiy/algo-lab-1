import math

def min_square_size(N, W, H):
    count = 0
    left, right = 1, max(W, H) * N

    while left < right:
        count += 1
        mid = (left + right) // 2
        sheets_per_row = mid // W
        sheets_per_col = mid // H
        total_sheets = sheets_per_row * sheets_per_col

        if total_sheets >= N:
            right = mid
        else:   
            left = mid + 1 


    return left, count

# 11 3 1
def min_square_size_2(N, W, H):
    if max(H, W) <= 2 * N:
        return max(H, W)
    sqr = math.sqrt(N)
    root = math.floor(sqr)
    left = True if sqr - root > 0 else False
    max_width = root * W + W if left and W <= H else root * W
    max_height = root * H + H if left and W >= H else root * H
    return max(max_width, max_height)


# Test cases
N, W, H = 10, 2, 3
print(min_square_size_2(N, W, H))  # Output: 9

N, W, H = 4, 1, 1
print(min_square_size_2(N, W, H))  # Output: 2

N, W, H = 5, 1, 1
print(min_square_size_2(N, W, H))  # Output: 3

N, W, H = 4, 2, 4
print(min_square_size_2(N, W, H))  # Output: 8

N, W, H = 3, 5, 2
print(min_square_size_2(N, W, H))  # Output: 6

N, W, H = 2, 1000000000, 999999999
print(min_square_size_2(N, W, H))  #Output: 1999999998

N, W, H = 1, 2, 2
print(min_square_size_2(N, W, H))  # Output: 2

N, W, H = 6, 2, 2
print(min_square_size_2(N, W, H))  # Output: 6

N, W, H = 7, 4, 2
print(min_square_size_2(N, W, H))  # Output: 8

N, W, H = 3, 3, 1
print(min_square_size_2(N, W, H))  # Output: 3

N, W, H = 3, 5, 2
print(min_square_size_2(N, W, H))  # Output: 5

N, W, H = 3, 1, 10
print(min_square_size_2(N, W, H))  # Output: 10

N, W, H = 3, 6, 2
print(min_square_size_2(N, W, H))  # Output: 6

N, W, H = 9, 7, 1
print(min_square_size_2(N, W, H))  # Output: 6

N, W, H = 11, 3, 1
print(min_square_size_2(N, W, H))  # Output: 6

W = 2
H = 3
N = 10
print(min_square_size(N, W, H))


