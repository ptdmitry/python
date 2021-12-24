class Matrix:
    def __init__(self, matrix):
        self.matrix_ = '\n'.join(['\t'.join([str(j) for j in i]) for i in matrix])
        matrix_3 = []
        for i in matrix:
            matrix_3.append([j for j in i])
        self.matrix = matrix_3

    def __str__(self):
        self.str = str(self.matrix_)
        return self.str

    def __add__(self, other):
        num_rows = len(self.matrix)
        num_columns = len(other.matrix[0])
        for i in range(num_rows):
            for j in range(num_columns):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            result = self.matrix
        return Matrix(result)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(f'matrix 1:\n{matrix_1}\n')
print(f'matrix 2:\n{matrix_2}\n')
print(f'matrix_1 + matrix_2:\n{matrix_1 + matrix_2}')
