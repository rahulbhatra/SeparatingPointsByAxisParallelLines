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
"""


def separating_points_by_axis_parallel_lines(number_of_coordinates: int, coordinates: []):
    coordinates = sorted(coordinates)
    # coordinates = sorted(coordinates, key=itemgetter(1))
    # coordinates = sorted(coordinates, key=itemgetter(0))
    vertical_lines, horizontal_lines = arbitrary_feasible_solution(number_of_coordinates, coordinates)
    # print(coordinates)
    is_feasible = is_solution_feasible(number_of_coordinates, coordinates, vertical_lines, horizontal_lines)
    print(is_feasible)
    vertical_lines, horizontal_lines = simulated_annealing(number_of_coordinates, coordinates, vertical_lines,
                                                           horizontal_lines)
    return vertical_lines, horizontal_lines


"""
    Here we have n = number of coordinates
    for loop is running for n number of times where check coordinates function have
    time complexity of O(n). So time complexity of the for loop will be O(n * (2 *n + c1))
    where c1 is constant time complexity of simple assignments. So for loop time complexity
    will be O(n^2).
    
    Other than for loop all work is done in constant time. So total time complexity of this
    function will be O(n^2).
"""


def arbitrary_feasible_solution(number_of_coordinates: int, coordinates: []):
    vertical_lines = set()
    horizontal_lines = set()

    for index in range(0, number_of_coordinates - 1):
        if coordinates[index][0] < coordinates[index + 1][0]:
            vertical_line = (coordinates[index][0] + coordinates[index + 1][0]) / 2
            vertical_line = check_coordinates(vertical_line, coordinates, False)
            vertical_lines.add(vertical_line)
        elif coordinates[index][0] == coordinates[index + 1][0]:
            horizontal_line = (coordinates[index][1] + coordinates[index + 1][1]) / 2
            horizontal_line = check_coordinates(horizontal_line, coordinates, True)
            horizontal_lines.add(horizontal_line)

    # for index in range(0, number_of_coordinates - 1):
    #     if coordinates[index][1] < coordinates[index + 1][1]:
    #         horizontal_line = (coordinates[index][1] + coordinates[index + 1][1]) / 2
    #         horizontal_line = check_coordinates(horizontal_line, coordinates, False)
    #         horizontal_lines.add(horizontal_line)
    #     elif coordinates[index][0] == coordinates[index + 1][0]:
    #         vertical_line = (coordinates[index][1] + coordinates[index + 1][1]) / 2
    #         vertical_line = check_coordinates(vertical_line, coordinates, True)
    #         vertical_lines.add(vertical_line)

    # print("vertical lines", vertical_lines)
    # print("horizontal lines", horizontal_lines)
    return list(vertical_lines), list(horizontal_lines)


"""
    Solution will be feasible if every two points are separated by a line in the solution space.
    So if every pair of two points are separated by a axis parallel line in between them then
    the solution is feasible.
    
    Here we have n = number of coordinates
    At most there can be n - 1 number of vertical lines or n - 1 horizontal lines to separate every
    point with each other.
    
    So Nested loop time complexity will be O(n^3) as most outer loop will run for n times, second outer
    loop will also run for n times and most inner loop also run for max n - 1 times.
    
    All other operations in loop and outside will be constant time. So total time complexity of checking
    solution feasibility will be O(n^3).
"""


def is_solution_feasible(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    # is_feasible = True
    # for i in range(0, number_of_coordinates):
    #     for j in range(i + 1, number_of_coordinates):
    #         vertical_separation = False
    #         for vertical_line in vertical_lines:
    #             if coordinates[i][0] < vertical_line < coordinates[j][0]:
    #                 vertical_separation = True
    #                 break
    #
    #         horizontal_separation = False
    #         for horizontal_line in horizontal_lines:
    #             if coordinates[i][1] < horizontal_line < coordinates[j][1]:
    #                 horizontal_separation = True
    #                 break
    #
    #         # No separation found between two pair of coordinates so solution is not feasible
    #         if vertical_separation is False and horizontal_separation is False:
    #             is_feasible = False
    #             return is_feasible
    #
    # # Every pair found a separation between so it is a feasible solution
    # return is_feasible

    # first = check_is_feasible(number_of_coordinates, coordinates, vertical_lines, horizontal_lines)
    second = check_feasibility(number_of_coordinates, coordinates, vertical_lines, horizontal_lines)

    # if first != second:
    #     print(first, second)
    #     print(vertical_lines, horizontal_lines)
    return second


def check_is_feasible(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):

    # print(coordinates)
    is_feasible = True
    for i in range(0, number_of_coordinates - 1):
        for j in range(i + 1, number_of_coordinates):
            vertical_separation = False
            for vertical_line in vertical_lines:
                if coordinates[i][0] < vertical_line < coordinates[j][0]:
                    vertical_separation = True
                    break

            horizontal_separation = False
            for horizontal_line in horizontal_lines:
                if coordinates[i][1] < coordinates[j][1] and coordinates[i][1] < horizontal_line < coordinates[j][1]:
                    horizontal_separation = True
                    break

                if coordinates[j][1] < coordinates[i][1] and coordinates[j][1] < horizontal_line < coordinates[i][1]:
                    horizontal_separation = True
                    break

            # No separation found between two pair of coordinates so solution is not feasible
            if vertical_separation is False and horizontal_separation is False:
                is_feasible = False
                return is_feasible

    # Every pair found a separation between so it is a feasible solution
    return is_feasible


"""
    Here we first got arbitrary feasible solution and have vertical and horizontal lines out of that.
    Then we are removing two lines on pair (vertical, vertical), (vertical, horizontal), (horizontal,
    horizontal) and adding third line can ve vertical or horizontal and checking solution feasibility.
    If solution is feasible then we are adding solution to the solution space as done in stimulated 
    annealing.
    
    Here we have 3 nested loops
"""


def simulated_annealing(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    # print("starting vertical_lines", vertical_lines)
    # print("starting horizontal_lines", horizontal_lines)
    i = 0
    j = i + 1
    reset_count = 0
    while i < len(vertical_lines):
        while j < len(vertical_lines):
            # print(i, j)
            two_line_removed_vertical_lines = []

            for k in range(0, len(vertical_lines)):
                if k != i and k != j:
                    two_line_removed_vertical_lines.append(vertical_lines[k])

            un_separated_coordinates = get_un_separated_coordinates(number_of_coordinates, coordinates,
                                                                    two_line_removed_vertical_lines, horizontal_lines)
            is_feasible, simulated_vertical_lines, simulated_horizontal_lines = \
                third_line_simulated_annealing(number_of_coordinates, coordinates, two_line_removed_vertical_lines,
                                               horizontal_lines, un_separated_coordinates)

            if is_feasible:
                # print("vertical_lines", simulated_vertical_lines)
                # print("horizontal_lines", simulated_horizontal_lines)
                vertical_lines = list(simulated_vertical_lines)
                horizontal_lines = list(simulated_horizontal_lines)
                i = 0
                j = 0
                reset_count += 1
                print("reset", reset_count)
            j += 1
        i += 1
        j = i + 1

    i = 0
    j = i + 1
    while i < len(vertical_lines):
        while j < len(horizontal_lines):
            # print(i, j)
            one_line_removed_vertical_lines = []
            one_line_removed_horizontal_lines = []

            for k in range(0, len(vertical_lines)):
                if k != i:
                    one_line_removed_vertical_lines.append(vertical_lines[k])

            for k in range(0, len(horizontal_lines)):
                if k != j:
                    one_line_removed_horizontal_lines.append(horizontal_lines[k])

            un_separated_coordinates = get_un_separated_coordinates(number_of_coordinates, coordinates,
                                                                    one_line_removed_vertical_lines,
                                                                    one_line_removed_horizontal_lines)
            is_feasible, simulated_vertical_lines, simulated_horizontal_lines = \
                third_line_simulated_annealing(number_of_coordinates, coordinates, one_line_removed_vertical_lines,
                                               one_line_removed_horizontal_lines, un_separated_coordinates)

            if is_feasible:
                # print("vertical_lines", simulated_vertical_lines)
                # print("horizontal_lines", simulated_horizontal_lines)
                vertical_lines = list(simulated_vertical_lines)
                horizontal_lines = list(simulated_horizontal_lines)
                i = 0
                j = 0
                reset_count += 1
                print("reset", reset_count)

            j += 1
        i += 1
        j = i + 1

    i = 0
    j = i + 1
    while i < len(horizontal_lines):
        while j < len(horizontal_lines):
            # print(i, j)
            two_line_removed_horizontal_lines = []

            for k in range(0, len(horizontal_lines)):
                if k != i and k != j:
                    two_line_removed_horizontal_lines.append(horizontal_lines[k])

            un_separated_coordinates = get_un_separated_coordinates(number_of_coordinates, coordinates,
                                                                    vertical_lines,
                                                                    two_line_removed_horizontal_lines)
            is_feasible, simulated_vertical_lines, simulated_horizontal_lines = \
                third_line_simulated_annealing(number_of_coordinates, coordinates, vertical_lines,
                                               two_line_removed_horizontal_lines, un_separated_coordinates)

            if is_feasible:
                vertical_lines = list(simulated_vertical_lines)
                horizontal_lines = list(simulated_horizontal_lines)
                i = 0
                j = 0
                reset_count += 1
                print("reset", reset_count)

            j += 1
        i += 1
        j = i + 1

    return vertical_lines, horizontal_lines


def third_line_simulated_annealing(number_of_coordinates: int,
                                   coordinates: [],
                                   vertical_lines: [],
                                   horizontal_lines: [],
                                   un_separated_coordinates: []):
    # print("un_separated_coordinates", len(un_separated_coordinates))
    for un_separated_coordinate in un_separated_coordinates:
        first_coordinate = un_separated_coordinate[0]
        second_coordinate = un_separated_coordinate[1]

        # Adding third vertical line to the un_separated_coordinates
        third_vertical_line = (first_coordinate[0] + second_coordinate[0]) / 2
        third_vertical_line = check_coordinates(third_vertical_line, coordinates, False)

        simulated_vertical_lines = list(vertical_lines)
        simulated_vertical_lines.append(third_vertical_line)
        simulated_vertical_lines.sort()

        is_vertical_simulation_feasible = is_solution_feasible(number_of_coordinates, coordinates,
                                                               simulated_vertical_lines,
                                                               horizontal_lines)

        if is_vertical_simulation_feasible is True:
            return True, simulated_vertical_lines, horizontal_lines

        # Adding third horizontal line to the un_separated_coordinates
        third_horizontal_line = (first_coordinate[1] + second_coordinate[1]) / 2
        third_horizontal_line = check_coordinates(third_horizontal_line, coordinates, True)
        simulated_horizontal_lines = list(horizontal_lines)
        simulated_horizontal_lines.append(third_horizontal_line)
        simulated_horizontal_lines.sort()

        is_horizontal_simulation_feasible = is_solution_feasible(number_of_coordinates, coordinates,
                                                                 vertical_lines,
                                                                 simulated_horizontal_lines)

        if is_horizontal_simulation_feasible is True:
            return True, vertical_lines, simulated_horizontal_lines

    return False, vertical_lines, horizontal_lines


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


def check_coordinates(axis_parallel_line: int, coordinates: [], is_horizontal: bool):
    for coordinate in coordinates:
        if is_horizontal is False and axis_parallel_line == coordinate[0]:
            axis_parallel_line += 0.25

        if is_horizontal is True and axis_parallel_line == coordinate[1]:
            axis_parallel_line += 0.25

    return axis_parallel_line
