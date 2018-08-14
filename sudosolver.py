import time


def sudosetup():
    """
    Creates the necessary global variables for the sudosolve function.
    """

    global ROWS, COLS, DIGITS, squares, units, unit, lines, peers

    # DIGITS and UNITS, while not strictly necessary should make it clearer why
    # values are significant rather than reusing COLS itself for DIGITS or UNITS
    ROWS = "ABCDEFGHI"
    COLS = "123456789"
    DIGITS = COLS
    squares = [r + c for r in ROWS for c in COLS]

    # Creating a list of square's units in order, this will later be used to
    # join the two together
    unitrows = []
    for r in range(3):

        for i in range(3):
            unitrows.append(

                list(map(lambda x: x + r * 3, [1, 1, 1, 2, 2, 2, 3, 3, 3])))
    unitlist = [j for i in unitrows for j in i]

    # Creating a dict called 'units' containing all squares for each unit.
    units = {}

    for i in range(1, 10):
        units.setdefault(i, [])

    for (i, s) in enumerate(squares):
        units[unitlist[i]].append(s)

    # Unlike units, this will only return the unit of one square, however this
    # is still very useful for quickly finding a square's peers
    unit = {}
    for i in range(81):
        unit[squares[i]] = unitlist[i]

    # This dictionary will contain rows and columns as keys with their items
    # being the squares contained withing those rows and columns.
    lines = {}
    for row_or_col in ROWS + COLS:

        members = []
        for s in squares:

            if row_or_col in s:
                members.append(s)

        lines[row_or_col] = members

    # A 'peer' is a square that influences another square, simply put it is one
    # in the same row, col, or unit, it is extremely advantageous to save this
    # info as it will drastically improve run time compared to recalculating it.
    peers = {}
    for s in squares:
        # Getting squares in the same unit, row, and col.
        peerlist = [units[unit[s]], lines[s[0]] + lines[s[1]]]
        peerlist = set([p for p in [j for i in peerlist for j in i] if p != s])

        peers[s] = peerlist


def sudoprint():
    for i in range(81):
        print(values[squares[i]], end="")
        if (i + 1) % 9 == 0:
            print()


def sudo_validate():
    # Immediately check for an unknown to lessen performance costs
    if "0" in values.values():
        return False

    # Here i will check if each line contains only one of each digit.
    for l in lines.keys():
        if set([values[s] for s in lines[l]]) != set(d for d in DIGITS):
            print("".join([values[s] for s in lines[l]]))
            return False

    # Here i will check if each unit contains only one of each digit.
    for u in units.keys():
        if set([values[s] for s in units[u]]) != set(d for d in DIGITS):
            return False

    return True


def sudo_brute_force():
    # Testing for break condition
    if sudo_validate():
        return True

    # Here i went for the simple method of picking just the first square that
    # is unknown, this is more efficient than it seems as it is seemingly
    # paradoxically cheaper on processing speed to work out a difficult square
    # than to pick a easier one

    for (s, v) in values.items():
        if v == "0":
            current_square = s

    # Calculating the digits that cs_peer could be
    cs_peer_values = [values[s] for s in peers[current_square]]
    cs_possibilities = [d for d in DIGITS if d not in cs_peer_values]

    # Checking if this square isn't impossible to solve, if so , backtrack
    if not cs_possibilities:
        return False

    # For each possible value, set it as that value then continue until the
    # grid is finished, if the wrong value is picked, the function backtracks
    for d in cs_possibilities:

        values[current_square] = d

        if sudo_brute_force():
            return True

    # Resetting value of chosen square to "0" again if a mistake was made and
    # the grid is now unsolvable ,
    values[current_square] = "0"
    return False


def sudosolve(string, report=True, string_is_list=False):
    """
    Solves a string Sudoku grid input with 0 representing unknowns.
    if report is True it will also print a log.
    If string_is_list is True it will solve a list of Sudoku strings.
    """

    # Assigning input string values to the square
    global values
    values = {}
    for (i, v) in enumerate([c for c in string]):
        values[squares[i]] = v

    if report:
        startingpoint = time.time()
        sudo_brute_force()
        endingpoint = time.time()
        timer = (endingpoint - startingpoint)

    else:
        sudo_brute_force()

    solved_string = "".join([i for i in values.values()])

    if report:

        if not string_is_list:

            print("Sudoku string solved! it taken {}ms"
                  .format(round(timer)))
            return solved_string

        else:

            return solved_string, timer

    else:

        return solved_string


def sudoparse(file, outputfile=False):
    """
    Returns a file of valid sudoku strings of length 81 with one sudoku
    string per line as a solved long string, .
    """

    with open(file) as f:
        sudostrings = f.readlines()

    solved_strings = []
    total_time = 0

    for string in sudostrings:
        sudostring = [c for c in string if c in "0123456789"]
        solved_string, timer = sudosolve(sudostring, True, string_is_list=True)

        solved_strings.append(solved_string)
        total_time += timer

    if outputfile:

        with open(outputfile) as ofile:

            for solved_string in solved_strings:
                ofile.write(solved_string + "\n")
                print(solved_string)

    else:

        for solved_string in solved_strings:
            print(solved_string)

    time_per_sudoku = total_time / len(solved_strings)

    print("{:^40}\n".format("Report - Parsing completed") + "-" * 40 + "\n",
          "Total time for Sudoku file to be solved = {}s\n"
          .format(round(total_time, 2)),

          "Average time spent per Sudoku = {}s"
          .format(round(time_per_sudoku, 2)))


sudosetup()
