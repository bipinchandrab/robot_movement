# Manual Test Data 
Input and Output:
###Test-1

    PLACE 0,0,NORTH
    MOVE
    LEFT
    RIGHT
    REPORT

Output: `0,1,NORTH`

###Test-2
    PLACE 4,5 EAST

Output: `Re-Run the program and input the values in Correct Format`

###Test-3
    PLACE 0,0 NORTH
    MOVE
    MOVE
    MOVE
    MOVE
    LEFT
    MOVE
    MOVE
    MOVE
    MOVE
    MOVE
    REPORT

Output: `0,4,WEST`

###Test-4
    PLACE 3,2 NORTH
    EAST
    MOVE
    MOVE
    LEFT
    RIGHT
    MOVE
    PLACE 1,1,EAST
    MOVE
    REPORT
Output: `2,1,EAST`

###Test-5
    PLACE 0,4 EAST
    MOVE
    MOVE
    LEFT
    MOVE
    LEFT
    MOVE
    REPORT

Output: `1,4,WEST`

###Test-6
    PLACE 4,4 NORTH
    MOVE
    LEFT
    LEFT
    MOVE
    MOVE
    RIGHT
    MOVE
    MOVE
    LEFT
    PLACE 1,1 EAST
    MOVE
    MOVE
    LEFT
    MOVE
    RIGHT
    REPORT   

Output: `3,2,EAST`