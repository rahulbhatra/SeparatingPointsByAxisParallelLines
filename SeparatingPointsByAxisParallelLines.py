from CheckFeasiblity import *

"""
    If number of points = n then we can restrict maximum number of axis parallel lines
    by (n - 1). Where n - 1 vertical parallel lines to separate n points. Also n - 1
    horizontal lines to separate n points. So maximum number of axis parallel lines needed
    is (n - 1).

    The first heuristics you are asked to implement is the following local-optimization procedure.
    Start with an arbitrary feasible solution. Try all combinations of two lines from the current feasible
    solution, and another line. If the removal of the two lines followed by the addition of the other line
    results in another feasible solution, then proceed and change the current feasible solution. Repeat
    trying all combinations, until no combination leads to another feasible solution. Such procedure is
    used by the meta-heuristic method Simulated Annealing.
    
    Time Analysis:-
    1. sorting of coordinates will run in O(n log n) time.
    2. simulated annealing algorithm will run in O(n ^ 6) time complexity.
    
    So total time complexity of this algorithm will be O(n ^ 6).
"""


def separating_points_by_axis_parallel_lines(number_of_coordinates: int, coordinates: []):
    coordinates = sorted(coordinates)
    vertical_lines, horizontal_lines = simulated_annealing(number_of_coordinates, coordinates)
    return vertical_lines, horizontal_lines


"""
    Here we have n = number of coordinates
    1. for loop is running for n number of times where check coordinates function have
    time complexity of O(n). So time complexity of the for loop will be O(n * (2 *n + c1))
    where c1 is constant time complexity of simple assignments. So for loop time complexity
    will be O(n^2).
    
    2. set to list conversion will be O(n) time for both vertical and horizontal line each.
    
    So total time complexity of the function is O(n ^ 2).
"""


def arbitrary_feasible_solution(number_of_coordinates: int, coordinates: []):
    vertical_lines = set()
    horizontal_lines = set()

    for index in range(0, number_of_coordinates - 1):
        if coordinates[index][0] < coordinates[index + 1][0]:
            vertical_line = (coordinates[index][0] + coordinates[index + 1][0]) / 2
            vertical_line = check_coincide(vertical_line, coordinates, False)
            vertical_lines.add(vertical_line)
        elif coordinates[index][0] == coordinates[index + 1][0]:
            horizontal_line = (coordinates[index][1] + coordinates[index + 1][1]) / 2
            horizontal_line = check_coincide(horizontal_line, coordinates, True)
            horizontal_lines.add(horizontal_line)

    return list(vertical_lines), list(horizontal_lines)


"""
    Here we first got arbitrary feasible solution and have vertical and horizontal lines out of that.
    Then getting new optimal solution by removing two lines and adding third line.
    Time Complexity Analysis:-
        1. arbitrary_feasible_solution function runs in O(n^2)
        2. while loop will run for max n number of time as we can produce new solution by removing
        two line and adding one and maximum line in the arbitrary solution is n - 1. So while loop
        can run for max n - 1 times.  
            a. optimize_feasible_solution function time complexity is O(n ^ 5).
            b. vertical_lines and horizontal_lines assignment will be done in O(n) time.
            c. other assignments are constant time complexity.
        So total time complexity of the while loop is O(n ^ 6).
        
    
    So total time complexity of the function will be O(n ^ 6).
"""


def simulated_annealing(number_of_coordinates: int, coordinates: []):
    vertical_lines, horizontal_lines = arbitrary_feasible_solution(number_of_coordinates, coordinates)
    is_feasible = True
    while is_feasible is True:
        is_feasible, simulated_vertical_lines, simulated_horizontal_lines = optimize_feasible_solution(
            number_of_coordinates, coordinates, vertical_lines, horizontal_lines)
        vertical_lines = list(simulated_vertical_lines)
        horizontal_lines = list(simulated_horizontal_lines)

    return vertical_lines, horizontal_lines


"""
    Here we are removing two lines on pair (vertical, vertical), (vertical, horizontal), (horizontal,
    horizontal) and adding third line. Third Line can ve vertical or horizontal and checking solution 
    feasibility. If solution is feasible then we are adding solution to the solution space as done in 
    stimulated annealing.
    
    1. first nested for loop run for number of vertical lines - 1 which can we max number of coordinates
        a. inner for loop run for number of vertical lines which can we max number of coordinates
            i. two_line_removed_vertical_lines assignment and removal or values is done in O(n) each
            ii. get_un_separated_coordinates function time complexity is O(n ^ 2)
            iii. third_line_simulated_annealing function time complexity is O( n ^ 3)
            iv. vertical_lines and horizontal lines assignment is O(n) each
            v. rest of the operations are constat time complexity
            So total time complexity of the inner for loop is O(n ^4)
        So total time complexity of the inner outer loop is O(n ^5)
    2. Similar to first nested while loop second and third while loop complexity will be O(n ^ 5).
    3. All other operations will be constant time complexity.
    
    So Total Time complexity of optimize_feasible_solution function is O(n ^ 5).
"""


def optimize_feasible_solution(number_of_coordinates: int, coordinates: [], vertical_lines: [],
                               horizontal_lines: []):
    for i in range(len(vertical_lines) - 1):
        for j in range(i + 1, len(vertical_lines)):
            two_line_removed_vertical_lines = list(vertical_lines)
            two_line_removed_vertical_lines.remove(vertical_lines[i])
            two_line_removed_vertical_lines.remove(vertical_lines[j])

            un_separated_coordinates = get_un_separated_coordinates(number_of_coordinates, coordinates,
                                                                    two_line_removed_vertical_lines, horizontal_lines)
            is_feasible, simulated_vertical_lines, simulated_horizontal_lines = \
                third_line_simulated_annealing(number_of_coordinates, coordinates, two_line_removed_vertical_lines,
                                               horizontal_lines, un_separated_coordinates)

            if is_feasible:
                return is_feasible, simulated_vertical_lines, simulated_horizontal_lines

    for i in range(len(vertical_lines)):
        for j in range(len(horizontal_lines)):
            one_line_removed_vertical_lines = list(vertical_lines)
            one_line_removed_vertical_lines.remove(vertical_lines[i])
            one_line_removed_horizontal_lines = list(horizontal_lines)
            one_line_removed_horizontal_lines.remove(horizontal_lines[j])

            un_separated_coordinates = get_un_separated_coordinates(number_of_coordinates, coordinates,
                                                                    one_line_removed_vertical_lines,
                                                                    one_line_removed_horizontal_lines)
            is_feasible, simulated_vertical_lines, simulated_horizontal_lines = \
                third_line_simulated_annealing(number_of_coordinates, coordinates, one_line_removed_vertical_lines,
                                               one_line_removed_horizontal_lines, un_separated_coordinates)

            if is_feasible:
                return is_feasible, simulated_vertical_lines, simulated_horizontal_lines

    for i in range(len(horizontal_lines) - 1):
        for j in range(i + 1, len(horizontal_lines)):
            two_line_removed_horizontal_lines = list(horizontal_lines)
            two_line_removed_horizontal_lines.remove(horizontal_lines[i])
            two_line_removed_horizontal_lines.remove(horizontal_lines[j])

            un_separated_coordinates = get_un_separated_coordinates(number_of_coordinates, coordinates,
                                                                    vertical_lines,
                                                                    two_line_removed_horizontal_lines)
            is_feasible, simulated_vertical_lines, simulated_horizontal_lines = \
                third_line_simulated_annealing(number_of_coordinates, coordinates, vertical_lines,
                                               two_line_removed_horizontal_lines, un_separated_coordinates)

            if is_feasible:
                return is_feasible, simulated_vertical_lines, simulated_horizontal_lines

    return False, vertical_lines, horizontal_lines


"""
    third_line_simulated_annealing function is used to for adding third line
    combination to the algorithm and then checking their feasibility. If feasible
    Solution found then returning that to the simulated annealing method to update
    current feasible solution to better optimized feasible solution.
    
    Time Complexity Analysis:-
    Maximum un separated coordinates when removing two lines will be lesser than n
    where n is number of coordinates.
        1. sorting of un_separated_coordinates will be O(n log n)
        2.  first for loop is used for checking every possible vertical line between two coordinates
            as coordinates are sorted on x axis so we just have to put vertical line between two coordinate
            in the same order. Taking combination of every two coordinate is not required.
            a. check_coincide function time complexity is O(n).
            b. assignment of simulated_vertical_lines is O(n).
            c. insert_value_in_axis_parallel_lines function time complexity is O(n).
            d. check_feasibility function time complexity is O(n ^2).
            e. rest of the operations in for loop is constant time.
        
        So total time complexity of the for loop will be O(n * (n + n + n + n ^2 + c1)) which is
        equivalent to O(n^3).
        3. sorting of un_separated_coordinates will be done on y axis in O(n log n)
        4.  second for loop is used for checking every possible horizontal line between two coordinates
            as coordinates are sorted on y axis so we just have to put horizontal line between two coordinate
            in the same order. Taking combination of every two coordinate is not required.
            a. check_coincide function time complexity is O(n).
            b. assignment of simulated_horizontal_lines is O(n).
            c. insert_value_in_axis_parallel_lines function time complexity is O(n).
            d. check_feasibility function time complexity is O(n ^2).
            e. rest of the operations in for loop is constant time.
        
        So total time complexity of the for loop will be O(n * (n + n + n + n ^2 + c1)) which is
        equivalent to O(n^3).
        5. Rest of the operations are constant time
        
    So total time complexity of the function third_line_simulated_annealing is as following:-
    = O(n log n) + O(n ^3) + O(n log n) + O(n ^3 + O(c1)
    = O(n^3)
"""


def third_line_simulated_annealing(number_of_coordinates: int,
                                   coordinates: [],
                                   vertical_lines: [],
                                   horizontal_lines: [],
                                   un_separated_coordinates: []):
    un_separated_coordinates = sorted(un_separated_coordinates)
    for index in range(len(un_separated_coordinates) - 1):
        first_coordinate = un_separated_coordinates[index]
        second_coordinate = un_separated_coordinates[index + 1]

        # Adding third vertical line to the un_separated_coordinates
        third_vertical_line = (first_coordinate[0] + second_coordinate[0]) / 2
        third_vertical_line = check_coincide(third_vertical_line, coordinates, False)

        simulated_vertical_lines = list(vertical_lines)
        insert_value_in_axis_parallel_lines(simulated_vertical_lines, third_vertical_line)
        is_vertical_simulation_feasible = check_feasibility(number_of_coordinates, coordinates,
                                                            simulated_vertical_lines,
                                                            horizontal_lines)

        if is_vertical_simulation_feasible is True:
            return True, simulated_vertical_lines, horizontal_lines

    un_separated_coordinates = sorted(un_separated_coordinates, key=lambda x: x[1])
    for index in range(len(un_separated_coordinates) - 1):
        first_coordinate = un_separated_coordinates[index]
        second_coordinate = un_separated_coordinates[index + 1]

        # Adding third horizontal line to the un_separated_coordinates
        third_horizontal_line = (first_coordinate[1] + second_coordinate[1]) / 2
        third_horizontal_line = check_coincide(third_horizontal_line, coordinates, True)
        simulated_horizontal_lines = list(horizontal_lines)
        insert_value_in_axis_parallel_lines(simulated_horizontal_lines, third_horizontal_line)

        is_horizontal_simulation_feasible = check_feasibility(number_of_coordinates, coordinates,
                                                              vertical_lines,
                                                              simulated_horizontal_lines)

        if is_horizontal_simulation_feasible is True:
            return True, vertical_lines, simulated_horizontal_lines

        # for un_separated_coordinate in un_separated_coordinates:
        #     first_coordinate = un_separated_coordinate[0]
        #     second_coordinate = un_separated_coordinate[1]
        #
        #     # Adding third vertical line to the un_separated_coordinates
        #     third_vertical_line = (first_coordinate[0] + second_coordinate[0]) / 2
        #     third_vertical_line = check_coincide(third_vertical_line, coordinates, False)
        #
        #     simulated_vertical_lines = list(vertical_lines)
        #     insert_value_in_axis_parallel_lines(simulated_vertical_lines, third_vertical_line)
        #     # simulated_vertical_lines.append(third_vertical_line)
        #     # simulated_vertical_lines.sort()
        #
        #     is_vertical_simulation_feasible = check_feasibility(number_of_coordinates, coordinates,
        #                                                         simulated_vertical_lines,
        #                                                         horizontal_lines)
        #
        #     if is_vertical_simulation_feasible is True:
        #         return True, simulated_vertical_lines, horizontal_lines
        #
        #     # Adding third horizontal line to the un_separated_coordinates
        #     third_horizontal_line = (first_coordinate[1] + second_coordinate[1]) / 2
        #     third_horizontal_line = check_coincide(third_horizontal_line, coordinates, True)
        #     simulated_horizontal_lines = list(horizontal_lines)
        #     insert_value_in_axis_parallel_lines(simulated_horizontal_lines, third_horizontal_line)
        #     # simulated_horizontal_lines.append(third_horizontal_line)
        #     # simulated_horizontal_lines.sort()
        #
        #     is_horizontal_simulation_feasible = check_feasibility(number_of_coordinates, coordinates,
        #                                                           vertical_lines,
        #                                                           simulated_horizontal_lines)
        #
        #     if is_horizontal_simulation_feasible is True:
        #         return True, vertical_lines, simulated_horizontal_lines

    return False, vertical_lines, horizontal_lines


"""
    This function is Used to insert element in sorted list of axis parallel lines.
    
    Time complexity of the function will be O(n) as maximum number of axis parallel lines
    for the solution is n - 1. Here for loops is running for the number of axis parallel lines.
    
    insertion at index n will also be O(n) time.
    
    Other operations are constant time in the algorithm.
    
    So total time complexity of the function will be O(2 * n) which is equivalent to O(n).
"""


def insert_value_in_axis_parallel_lines(axis_parallel_lines, value):
    index = len(axis_parallel_lines)
    for i in range(len(axis_parallel_lines)):
        if axis_parallel_lines[i] > value:
            index = i
            break

    axis_parallel_lines.insert(index, value)
    return axis_parallel_lines


"""
    This function will return coordinates which are not separated by axis parallel lines
"""

"""
def get_un_separated_coordinates(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    un_separated_coordinates = []
    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            vertical_separation = False
            for vertical_line in vertical_lines:
                if coordinates[i][0] < vertical_line < coordinates[j][0]:
                    vertical_separation = True
                    break

            horizontal_separation = False
            for horizontal_line in horizontal_lines:
                if coordinates[i][1] < horizontal_line < coordinates[j][1]:
                    horizontal_separation = True
                    break

            # No separation found between two pair of coordinates so solution is not feasible
            if vertical_separation is False and horizontal_separation is False:
                un_separated_coordinates.append((coordinates[i], coordinates[j]))

    # print(un_separated_coordinates)
    return un_separated_coordinates
"""

"""
    This function is used for checking if axis parallel line coincide on coordinates. And if it coincides
    with any point then we are increasing axis parallel line value to 0.25.
    Axis Parallel Line can be either horizontal or vertical depends on is_horizontal argument.
    
    Time Complexity:
        For loop runs for O(n) times where n = number of coordinates. All other assignments inside
        are constant time. So total time complexity of this function will be O(n).
"""


def check_coincide(axis_parallel_line: int, coordinates: [], is_horizontal: bool):
    for coordinate in coordinates:
        if is_horizontal is False and axis_parallel_line == coordinate[0]:
            axis_parallel_line += 0.25

        if is_horizontal is True and axis_parallel_line == coordinate[1]:
            axis_parallel_line += 0.25

    return axis_parallel_line
