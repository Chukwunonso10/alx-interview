def pascal_triangle(n):
    if n <= 0:
        return []

    p_triangle = [1]
    for i in range(i, n):
        new_row = [1]
        for j in range(1, i):
            new_row.append(p_triangle[i-1][j-1] + p_triangle[i-1][j])
        new_row.append(1)
        p_triangle.append(new_row)

    return p_triangle
