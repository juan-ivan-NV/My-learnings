def matrix_mult(a, b):
    return [[sum(i*j for i,j in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]