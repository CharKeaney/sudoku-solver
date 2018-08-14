# sudoku-solver
A simple recursive backtracking algorithm for solving Sudoku puzzles when given a 81 character string.

# Features
- Ability to solve a given sudoku string when given as a string argument via 'sudosolve()'
- Ability to solve and save a file of sudokus when given a filename argument via 'sudoparse()'

# Important info

##### How to format an input Sudoku string
To write a Sudoku grid as a valid Sudoku string input, simply type the square values left to right, top to bottom , while writing unknown values as "0", it is important you type the entire grid in quotes so Python recognises it as a string input rather than variable, 
here is an example grid:
```"000075400000000008080190000300001060000000034000068170204000603900000020530200000"```

##### How to solve an input string
To solve an input Sudoku string, simply type into the python console ```sudosolve(sudokustring)```
Optional arguments include 'report', which is enabled by default and will print a report of the solving process, and 'string_is_list' which is disabled by default, set this argument to true if you wish for `sudosolve()` to not print a report but still return the time taken alongside the solved grid, e.g if it is part of a wider function.
here is an example of how you can solve your string
```sudosolve("000075400000000008080190000300001060000000034000068170204000603900000020530200000")```

##### How to format an input Sudoku file
The file should contain one properly formatted sudoku string on each line, if spread across multiple lines the program will not work,
in the included `sample_grid` file you can see what a properly formatted Sudoku input file looks like

##### How to solve an input Sudoku file
With `sudosolver.py` being ran in the Python console, type ```sudoparse(filename)```
Optional arguments include 'outputfile' , if this argument is specified the solved grid will be saved to the outputfile given to it as an argument. Here is an example of how you can solve a sudoku file from `sample_grids`                                                
`sudoparse("sample_grids/sample-25clues.txt")`

##### How to view a solved or unsolved Sudoku
To view the current state of the Sudoku grid, type in the `sudosolver.py` Python console `sudoprint()`, this is a simple function that will display the grid in text square form


# How it works
This Sudoku solver is made fairly simply using recursive backtracking, so the process of solving a grid essentially looks a little like this

- Check if the grid is already solved, if so return the grid
- Pick the first square that is unknown (contains a 0)
- If no digit can be placed in this square, return to the calling function False
- If digit(s) can be placed in this square, try them in order 
- call this function (go back to step 1) and if it returns False set the squares value to 0 again and try the next digit
- if no digit is found that does not return false then return False

# Issues
- When given an input Sudoku string containing less than 20~ clues, the time taken exponentially increases, sometimes to around 2.5 minutes, this is due to inefficiencies in the algorithm used and i may try fix this in the future with a faster algorithm
- It seems unclear if the program is broken or just taking a while to solve a difficult Sudoku puzzle so i could include a progress bar of some sort to indicate progress
- Its important to remember that it is not possible to have a unique Sudoku with less than 17 clues and this function will not return all solutions, just the first one it finds, one issue here is with input validation , it's hard for the program to know an extremely difficult Sudoku from an impossible one
- It would make the program more usable if i included a GUI so i may look into that in the future
