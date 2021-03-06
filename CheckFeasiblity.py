"""
    Method is used to check if the separating n points using axis parallel lines is feasible solution or not.
        - axis parallel lines are represented by vertical_lines and horizontal_lines

    Logic:-
        Using both x_axis_separation_map and y_axis_separation_map checking if there is any combination between
    two coordinates which is yet not separated. If combination is present like that then solution is not feasible.

    Total time complexity is as following:-
        1. time complexity of the generate_separation_maps function is O(n ^ 2).
        2. nested for loop have inner for loop and both run for n = number of coordinates. So time
        complexity of the nested for loop will be O(n ^2 ).
        3. un_separated_coordinates set to list conversion is O(n).

    So total time complexity of the function is O(n ^ 2).
"""


def check_feasibility(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    x_axis_separation_map, y_axis_separation_map, replaced_index = generate_separation_maps \
        (number_of_coordinates, coordinates, vertical_lines, horizontal_lines)

    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            i_replaced_index = replaced_index[i]
            j_replaced_index = replaced_index[j]
            if x_axis_separation_map[i][j] is False and \
                    (y_axis_separation_map[i_replaced_index][j_replaced_index] is True or
                     y_axis_separation_map[j_replaced_index][i_replaced_index] is True):
                x_axis_separation_map[i][j] = True

            if x_axis_separation_map[i][j] is False:
                return False

    return True


"""
    Method is used for getting not separated points by axis parallel lines.
    Total time complexity is as following:-
        1. time complexity of the generate_separation_maps function is O(n ^ 2).
        2. nested for loop have inner for loop and both run for n = number of coordinates. So time
        complexity of the nested for loop will be O(n ^2 ).
        3. un_separated_coordinates set to list conversion is O(n).

    So total time complexity of the function is O(n ^ 2).
"""


def get_un_separated_coordinates(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    x_axis_separation_map, y_axis_separation_map, replaced_index = generate_separation_maps \
        (number_of_coordinates, coordinates, vertical_lines, horizontal_lines)
    un_separated_coordinates = set()
    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            i_replaced_index = replaced_index[i]
            j_replaced_index = replaced_index[j]
            if x_axis_separation_map[i][j] is False and \
                    (y_axis_separation_map[i_replaced_index][j_replaced_index] is True or
                     y_axis_separation_map[j_replaced_index][i_replaced_index] is True):
                x_axis_separation_map[i][j] = True

            if x_axis_separation_map[i][j] is False:
                un_separated_coordinates.add(coordinates[i])
                un_separated_coordinates.add(coordinates[j])

    return list(un_separated_coordinates)


"""
    Following function is used to prepare vertical lines separation map and horizontal line separation map.
    Separation map is 2d array which denotes combination of two coordinate and if value is true then it is
    separated by a line.
    
    Logic:-
        First sort coordinates on the basis of x axis then updating x_axis_separation_map
        which update separation relation between two coordinates.
            - As points are sorted on x axis if first_x_axis coordinate and second_x_axis coordinate
            is separated using vertical line then we can say first_x_axis coordinate is separated
            to bigger_x_axis coordinates.

        With same logic as above now sorting coordinates on y_axis and producing y_axis_separation_map
        
    Time Complexity Analysis:-
    n = number of coordinates
    1. x_axis_sorted_coordinates is sorted in O(n log n) time
    2. x_axis_separation_map initialization is O(2 * n ^ 2) time
        a. O(n ^ 2) time to initiate value to None
        b. O(n ^ 2) time to update value as True

    3.After x_axis_separation_map initialization we update the coordinates combination which are
    not separated by vertical lines
        a. first we see separation between i and i + 1 coordinates in x_axis_sorted_coordinates
        this step take O(n) time as there can only be max n - 1 number of vertical lines

        b. if there is no separation then need to update previous coordinates eg.
            let's say if we have
            i. 2, 3 coordinate as not separated
            ii. we found out that 3, 4 coordinate is also not separated
            iii. now we need to update that 2, 4 is also not separated
        This step take O(n) time as there can be max n - 1 coordinate before current coordinate.
    This step in total take time complexity of O(n ^2) as outer loop also runs n times.

    4. This step will be similar to step 1, 2, 3 combined but we will get y_axis_separation_map
    Time complexity will be equivalent to step 1, 2, 3

    5. find_replaced_index run for O(n ^ 2) time to find new index after sorting coordinates on y_axis
    
    So total Time complexity of this function is O(n ^ 2).
"""


def generate_separation_maps(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    x_axis_sorted_coordinates = sorted(coordinates)

    # assume all coordinates are separated at first
    # is first line and second line is divided then first line is divided to every other line
    # so update all combination with first coordinate as separated

    x_axis_separation_map = [[None for _ in range(0, number_of_coordinates)] for _ in range(0, number_of_coordinates)]
    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            x_axis_separation_map[i][j] = True
        # print(i, x_axis_separation_map[i])

    for i in range(0, number_of_coordinates - 1):
        first_x_axis = x_axis_sorted_coordinates[i][0]
        second_x_axis = x_axis_sorted_coordinates[i + 1][0]

        separation = False
        for vertical_line in vertical_lines:
            if first_x_axis < vertical_line < second_x_axis:
                separation = True
                break

        x_axis_separation_map[i][i + 1] = separation

        if separation is False:
            for j in range(i - 1, -1, -1):
                if x_axis_separation_map[j][j + 1] is False:
                    x_axis_separation_map[j][i + 1] = False
                else:
                    break

    # print('------ X Axis Separation Map ------------')
    # for i in range(0, number_of_coordinates):
    #     print(i + 1, x_axis_separation_map[i])

    y_axis_separation_map = [[None for _ in range(0, number_of_coordinates)] for _ in range(0, number_of_coordinates)]
    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            y_axis_separation_map[i][j] = True
        # print(i, y_axis_separation_map[i])

    y_axis_sorted_coordinates = sorted(coordinates, key=lambda x: x[1])
    for i in range(0, number_of_coordinates - 1):
        first_y_axis = y_axis_sorted_coordinates[i][1]
        second_y_axis = y_axis_sorted_coordinates[i + 1][1]

        separation = False
        for horizontal_line in horizontal_lines:
            if first_y_axis < horizontal_line < second_y_axis:
                separation = True
                break

        y_axis_separation_map[i][i + 1] = separation

        if separation is False:
            for j in range(i - 1, -1, -1):
                if y_axis_separation_map[j][j + 1] is False:
                    y_axis_separation_map[j][i + 1] = False
                else:
                    break

    # print('------ Y Axis Separation Map ------------')
    # for i in range(0, number_of_coordinates):
    #     print(i + 1, y_axis_separation_map[i])

    replaced_index = find_replaced_index(number_of_coordinates, x_axis_sorted_coordinates, y_axis_sorted_coordinates)
    return x_axis_separation_map, y_axis_separation_map, replaced_index


"""
    To find the replaced indexes we are using two for loops which leads to time complexity of O(n ^ 2).
    All other things are constant time in this function.
"""


def find_replaced_index(number_of_coordinates: int, x_axis_sorted_coordinates: [], y_axis_sorted_coordinates: []):
    replaced_index = [-1 for _ in range(0, number_of_coordinates)]
    for x_axis_sorted_coordinate_index in range(0, number_of_coordinates):
        for y_axis_sorted_coordinate_index in range(0, number_of_coordinates):
            if x_axis_sorted_coordinates[x_axis_sorted_coordinate_index] == \
                    y_axis_sorted_coordinates[y_axis_sorted_coordinate_index]:
                replaced_index[x_axis_sorted_coordinate_index] = y_axis_sorted_coordinate_index

    return replaced_index


"""
    Solution will be feasible if every two points are separated by a line in the solution space.
    So if every pair of two points are separated by a axis parallel line in between them then
    the solution is feasible.

    Here we have n = number of coordinates
    At most there can be n - 1 number of vertical lines or n - 1 horizontal lines to separate every
    point with each other.
    
    Sorting the coordinates will be done in time complexity of O(n).

    So Nested loop time complexity will be O(n^3) as most outer loop will run for n times, second outer
    loop will also run for n times and most inner loop also run for max n - 1 times.

    All other operations in loop and outside will be constant time. So total time complexity of checking
    solution feasibility will be O(n^3).
"""


def check_is_feasible(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
    coordinates = sorted(coordinates)
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
    This algorithm is used to compare the result of both feasibility checking algorithms
    for assurance of the output produced.
    
    First Algorithm check_feasibility is O(n^2) and second algorithm is O(n^3).   
"""


def compare_feasibility_algorithms(number_of_coordinates: int, coordinates: [], vertical_lines: [],
                                   horizontal_lines: []):
    is_feasible_first = check_feasibility(number_of_coordinates, coordinates, vertical_lines,
                                          horizontal_lines)
    is_feasible_second = check_is_feasible(number_of_coordinates, coordinates, vertical_lines,
                                           horizontal_lines)
    print('Check Feasibility Function Output:', is_feasible_first)
    print('Check Is Feasible Function Output:', is_feasible_second)

    if is_feasible_first == is_feasible_second:
        print("Both Feasibility Checking Algorithm is producing similar output. Happy Coding :)")
        return True
    else:
        print("Both Feasibility Checking Algorithm is Not producing similar output Please Check your code")
        return False
