jump_path = [(0, 2), (3, 4), (5, 7)]  # Replace with your actual jump path

move_path = []

for i in range(len(jump_path) - 1):
    r0, c0 = jump_path[i]
    r1, c1 = jump_path[i + 1]
    print(i)
    

    # Determine the direction of the move
    move_direction = (r1 - r0, c1 - c0)

    # Add 1 to either the row or column based on the move direction
    new_row = r1 + move_direction[0]
    new_col = c1 + move_direction[1]

    move_path.append((new_row, new_col))

print(move_path)