def subsets(nums):
    res = []
    sub_set = []

    def dfs(i):
        if i >= len(nums):
            res.append(sub_set.copy())
            return

        sub_set.append(nums[i])
        dfs(i + 1)

        sub_set.pop()
        dfs(i + 1)

    dfs(0)
    return res[::-1]


def solution(N, B, workers):
    res = B
    workers = workers.split(" ")
    chosen_subset = []
    bears_subsets = subsets([i for i in range(B)])

    for subset in bears_subsets:
        zerous = [0 for _ in range(N)]

        for i, val in enumerate(workers):
            for j in range(len(val)):
                if val[j] == "Y" and j in subset:
                    zerous[i] += 1

        if 0 not in zerous:
            res = min(res, len(subset))
            if res == len(subset):
                chosen_subset = subset

    return res, [val + 1 for val in chosen_subset]


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        N, B = map(int, lines[0].split())
        workers = " ".join(lines[1:]).strip()

    result = solution(N, B, workers)

    with open("output.txt", "w") as output_file:
        output_file.write(f"{result[0]}\n")
        output_file.write(" ".join(map(str, result[1])))


if __name__ == "__main__":
    main()
