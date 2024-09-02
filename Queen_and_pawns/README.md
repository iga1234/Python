Generating the Board

The first step of the task is to generate an 8x8 chessboard. The board includes:

    A number of queens (up to a maximum of 5) randomly placed on the board.
    One pawn, also randomly placed on the board.

Each piece must be positioned on a unique square, with no two pieces occupying the same position. When the program is run, the board's layout should be displayed to the user.
Checking for Threats

The program should determine whether the pawn is under threat of being captured by any of the queens. Additionally, the program should display the positions of all queens that have the ability to capture the pawn, if any exist.
Additional Features

After displaying the results regarding potential captures, the user should have the option to:

    Randomly generate a new position for the pawn while keeping the queens in their original positions.
    Remove any queen by specifying its position.
    Re-check for threats after making these changes.

Notes

    A queen can move vertically, horizontally, or diagonally.
    The maximum number of queens (k) is 5.
