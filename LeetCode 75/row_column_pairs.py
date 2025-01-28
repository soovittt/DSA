class Solution:
    def equalPairs(self, grid):
        """
        Find the number of pairs (ri, cj) such that row ri and column cj are equal.

        Parameters
        ----------
        grid : List[List[int]]
            The input n x n integer matrix.

        Returns
        -------
        int
            The number of equal row and column pairs.
        """
        n = len(grid)  # Get the size of the matrix (number of rows/columns)
        count = 0  # Initialize the counter for the number of equal pairs
        row_count = {}  # Dictionary to count the occurrences of each row
        column_count = {}  # Dictionary to count the occurrences of each column
        
        # Count the occurrences of each row
        for row in grid:
            row_tuple = tuple(row)  # Convert the row to a tuple (hashable type)
            if row_tuple in row_count:
                row_count[row_tuple] += 1  # Increment the count if the row already exists in the dictionary
            else:
                row_count[row_tuple] = 1  # Initialize the count if the row does not exist in the dictionary
        
        # Count the occurrences of each column
        for j in range(n):
            col_tuple = tuple(grid[i][j] for i in range(n))  # Convert the column to a tuple (hashable type)
            if col_tuple in column_count:
                column_count[col_tuple] += 1  # Increment the count if the column already exists in the dictionary
            else:
                column_count[col_tuple] = 1  # Initialize the count if the column does not exist in the dictionary
        
        # Compare rows and columns
        for row_tuple, row_tuple_count in row_count.items():
            if row_tuple in column_count:  # Check if the row tuple exists in the column dictionary
                count += row_tuple_count * column_count[row_tuple]  # Add the product of their counts to the total count
        
        return count  # Return the total count of equal row and column pairs