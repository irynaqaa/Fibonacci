import numpy as np

# Define a function to implement algorithm X

def algorithm_x(matrix):
    # Initialize an empty list to store the solutions
    solutions = []

    # Define a recursive function to find all solutions
    def find_solutions(matrix, solution):
        # If the matrix is empty, it means we have found a solution
        if matrix.size == 0:
            solutions.append(solution)
            return

        # Find the column with the fewest ones
        column_counts = np.sum(matrix, axis=0)
        min_count = np.min(column_counts)
        min_columns = np.where(column_counts == min_count)[0]

        # Try each column with the fewest ones
        for column in min_columns:
            # Find the rows that have a one in the current column
            rows = np.where(matrix[:, column] == 1)[0]

            # Try each row
            for row in rows:
                # Create a new matrix by removing the current row and column
                new_matrix = np.delete(np.delete(matrix, row, axis=0), column, axis=1)

                # Recursively find all solutions with the new matrix
                find_solutions(new_matrix, solution + [row])

    # Start the recursion with an empty solution
    find_solutions(matrix, [])

    return solutions

# Example usage:
matrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 1]
])
solutions = algorithm_x(matrix)
print("Solutions:")
for i, solution in enumerate(solutions):
    print("Solution {}:{}".format(i+1, solution))