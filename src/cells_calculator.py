def compute_cells(data, n_cells):
    # Initialize the dictionary to store the number of objects in each cell
    cells = {}

    # Loop over the data
    for point in data:
        # Get the cell coordinates for the point
        cell = tuple([min(int(point[i] // (100 / n_cells)), n_cells - 1) for i in range(len(point))])

        # If the cell is not in the dictionary, add it
        if cell not in cells:
            cells[cell] = 1
        # Otherwise, increment the count
        else:
            cells[cell] += 1

    return cells


def compute_objects(cells, n_cells, dim):
    # Initialize the dictionary to store the number of cells covering each number of objects
    objects = {}

    # Loop over the cells
    for cell in cells:
        # Get the number of objects in the cell
        n_objects = cells[cell]

        # Loop over the range from 1 to n_objects
        for i in range(1, n_objects + 1):
            # If i is not in the dictionary, add it
            if i not in objects:
                objects[i] = 1
            # Otherwise, increment the count
            else:
                objects[i] += 1
    
    # Now compute the amount of cells covering 0 objects
    # There is a total of n_cells ** dim cells in the space
    # The number of cells covering 0 objects is the difference between the total number of cells and the number of cells covering at least 1 object
    objects[0] = n_cells ** dim - objects[1]

    return objects