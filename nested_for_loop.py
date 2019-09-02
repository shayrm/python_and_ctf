number_grid = [
    [1, 2, 3, 4],
    [9, 8, 7, 6],
    [0, 0, 0, 0]
]

# pars through two dim list

for row in number_grid:
    print(row)

# or

for row in number_grid:
    for col in row:
        print(col)
        