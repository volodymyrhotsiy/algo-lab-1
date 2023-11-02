from collections import deque


class Graph:
    def __init__(self, color, values):
        self.color = color
        self.values = values


class Solution(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.ROWS, self.COLS = len(matrix), len(matrix[0])

    def bfs(self, sr, sc):
        visited = set()
        queue = deque([(sr, sc)])
        values = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        target_color = self.matrix[sr][sc]

        while queue:
            currentRow, currentCol = queue.popleft()
            values.append((currentRow, currentCol))
            visited.add((currentRow, currentCol))

            for rowOffset, colOffset in directions:
                neighborRow = currentRow + rowOffset
                neighborCol = currentCol + colOffset
                pos = (neighborRow, neighborCol)

                if (
                    self.isInBounds(neighborRow, neighborCol)
                    and pos not in visited
                    and self.matrix[neighborRow][neighborCol] == target_color
                ):
                    queue.append(pos)

        return Graph(target_color, values)

    def get_sections(self):
        visited = set()
        graphs = []

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if (r, c) not in visited:
                    graph = self.bfs(r, c)
                    visited.update(graph.values)
                    graphs.append(graph)

        return graphs

    def isInBounds(self, row, col):
        return 0 <= row < self.ROWS and 0 <= col < self.COLS

    def recolor(self, sr, sc, newc):
        graphs = self.get_sections()
        oldc = self.matrix[sr][sc]

        if oldc == newc:
            return self.matrix

        for graph in graphs:
            if graph.color == oldc:
                for row, col in graph.values:
                    self.matrix[row][col] = newc

        return self.matrix

def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            row = line.strip().split(',')
            cleaned_row = [value.strip() for value in row] 
            matrix.append(cleaned_row)
    return matrix

def write_matrix_to_file(file_path, matrix):
    with open(file_path, 'w', encoding='utf-8') as file:
        for r in matrix:
            file.write(str(r) + '\n')



if __name__ == "__main__":
    file_path = r'C:\Users\HOME1\OneDrive\Desktop\random code\__pycache__\matrix.txt'
    matrix = read_matrix_from_file(file_path)
    solution = Solution(matrix)
    sr = 9
    sc = 9
    newColor = "A"
    solution.recolor(sr, sc, newColor)
    for row in solution.matrix:
        print(row)
    write_matrix_to_file(r"C:\Users\HOME1\OneDrive\Desktop\random code\__pycache__\output.txt", solution.matrix)    