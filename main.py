# print the sudoku
def draw(puzzle):
    line = "+-------+-------+-------+"

    for i in range(9):
        if i % 3 == 0:
            print(line)

        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")

            value = puzzle[i][j]
            print(value if value != 0 else ".", end=" ")

        print("|")

    print(line)


# find and return zeros
def find_free(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return [i, j]

    return None


def is_valid(puzzle, n, x, y):
    # check in row and column
    for i in range(9):
        if puzzle[x][i] == n or puzzle[i][y] == n:
            return False

    # check in square
    x_square = (x // 3) * 3
    y_square = (y // 3) * 3

    for i in range(x_square, x_square + 3):
        for j in range(y_square, y_square + 3):
            if puzzle[i][j] == n:
                return False

    return True


def solve(puzzle):
    free = find_free(puzzle)

    # if there is no zero, puzzle is solved
    if free is None:
        return True

    x, y = free

    for i in range(1, 10):
        if is_valid(puzzle, i, x, y):
            puzzle[x][y] = i

            if solve(puzzle):
                return True

            # backtracking
            puzzle[x][y] = 0

    return False


def main():
    puzzle = []

    for i in range(1, 10):
        while True:
            try:
                raw = input(f"Enter line {i}: ").strip()
                parts = raw.split()

                # checking the length of the row
                if len(parts) != 9:
                    print(
                        f"ERROR: the length of line is {len(parts)}. "
                        "It must be 9..."
                    )
                    continue

                line = list(map(int, parts))

                # checking the range
                if not all(0 <= x <= 9 for x in line):
                    print("ERROR: numbers must be between 0-9...")
                    continue

                puzzle.append(line)
                break

            except ValueError:
                print("ERROR: just enter numbers...")

    if solve(puzzle):
        print("\n")
        draw(puzzle)
    else:
        print("I can't solve it...\n")


if __name__ == "__main__":
    main()