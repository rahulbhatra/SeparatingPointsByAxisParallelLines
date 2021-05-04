def check_feasibility(number_of_coordinates: int, coordinates: [], vertical_lines: [], horizontal_lines: []):
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

    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            i_replaced_index = replaced_index[i]
            j_replaced_index = replaced_index[j]
            if x_axis_separation_map[i][j] is False and \
                    (y_axis_separation_map[i_replaced_index][j_replaced_index] is True or
                     y_axis_separation_map[j_replaced_index][i_replaced_index] is True):
                x_axis_separation_map[i][j] = True

    # print('------ X Axis Separation Map ------------')
    # for i in range(0, number_of_coordinates):
    #     print(i + 1, x_axis_separation_map[i])

    for i in range(0, number_of_coordinates):
        for j in range(i + 1, number_of_coordinates):
            if x_axis_separation_map[i][j] is False:
                return False

    return True




def find_replaced_index(number_of_coordinates: int, x_axis_sorted_coordinates: [], y_axis_sorted_coordinates: []):
    replaced_index = [-1 for _ in range(0, number_of_coordinates)]
    for x_axis_sorted_coordinate_index in range(0, number_of_coordinates):
        for y_axis_sorted_coordinate_index in range(0, number_of_coordinates):
            if x_axis_sorted_coordinates[x_axis_sorted_coordinate_index] == \
                    y_axis_sorted_coordinates[y_axis_sorted_coordinate_index]:
                # print(x_axis_sorted_coordinates[x_axis_sorted_coordinate_index])
                # print(y_axis_sorted_coordinates[y_axis_sorted_coordinate_index])

                replaced_index[x_axis_sorted_coordinate_index] = y_axis_sorted_coordinate_index

    return replaced_index
