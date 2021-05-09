a. Following dependencies should be installed in the System:-
    1. Python3
    2. Matplotlib

b. How to execute the code
    1. All the files to run should be in the same folder as code and output will also be available in the same folder.
    2. Input file should be named as instance01, instance02, instance03 and so on.
    Install the above dependencies then run the command as below:-
        python3 main.py <number of files>
        
c. Number of files should be correct and should be in the following format (File should be in txt format only):-
    i. file name should be in this format “instance01” where 01 represents file number
    ii. file should have at most 100 points.
    iii. Each input file starts with n, the number of points, followed by n lines, each containing two
    integers: the x and y coordinates of the point. The points are sorted by the x coordinates.

d. Output file will be present in the format of "local_solution01" where 01 represents file number (output file will be txt).
    The output file should contain in the first line m, the number of axis-parallel lines used by the
    solution, follow by another m lines, each describing one axis-parallel line as follows: the characters
    ’h’ or ’v’ are used to describe if the axis-parallel line is horizontal or vertical, and a floating point
    gives the coordinate where this line crosses the axis. For example:
        local_solution01:
        3
        v 2.5
        v 3.5
        h 2.5

e. To visulaize the output there are png files created with name "local_solution01.png" where 01 represents corrosponding file number.
                