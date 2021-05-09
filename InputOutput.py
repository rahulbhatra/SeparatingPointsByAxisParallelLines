import matplotlib.pyplot as plt

"""
    Class Input is used to read input file and keep input of a file in a object
"""


class Input:
    def __init__(self, number_of_coordinates: int, coordinates: [], file_name: str):
        self.number_of_coordinates = number_of_coordinates
        self.coordinates = coordinates
        self.file_name = file_name

    def add_coordinate(self, x: int, y: int):
        if len(self.coordinates) > self.number_of_coordinates:
            return Exception("Wrong number of inputs added in the file please check the file provided :)")

        coordinate = (x, y)
        self.coordinates.append(coordinate)


"""
    Class output is used to store output of a input file and use them to write in the output file
"""


class Output:
    def __init__(self, number_of_lines: int, vertical_lines: [], horizontal_lines: []):
        self.number_of_lines = number_of_lines
        self.vertical_lines = vertical_lines
        self.horizontal_lines = horizontal_lines


"""
    read_inputs function read files and store input in a object and return all those
    inputs in a list 
"""


def read_inputs(number_of_files: int):
    inputs = []
    for i in range(1, number_of_files + 1):
        file_name = 'instance'
        if i < 10:
            file_name += str(0)
        file_name += str(i) + ".txt"
        input = read_input(file_name)
        inputs.append(input)
    return inputs


"""
    read_input function is used for reading a file input in a object and return that object    
"""


def read_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    input = Input(int(lines[0]), [], file_name)

    for i in range(1, len(lines)):
        x, y = lines[i].split()
        x, y = int(x), int(y)
        input.add_coordinate(x, y)
    return input


"""
    write output function is used for writing data into the output file
"""


def write_output(file_name, output: Output):
    file = open(file_name, 'w')
    lines = str(output.number_of_lines) + '\n'

    for i in range(0, len(output.horizontal_lines)):
        lines += "h " + str(output.horizontal_lines[i]) + "\n"

    for i in range(0, len(output.vertical_lines)):
        lines += "v " + str(output.vertical_lines[i]) + "\n"

    file.writelines(lines)


"""
    prepare_plot function is built to visualize the solution if it is correct or not.
"""


def prepare_plot(coordinates: [], vertical_lines: [], horizontal_lines: [], output_file_name):
    x_axis = []
    y_axis = []
    for coordinate in coordinates:
        x_axis.append(coordinate[0])
        y_axis.append(coordinate[1])

    # print('x_axis', x_axis)
    # print('y_axis', y_axis)
    # print('vertical lines', vertical_lines)
    # print('horizontal lines', horizontal_lines)

    plt.figure(figsize=(max(x_axis) // 2, max(y_axis) // 2))
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Separating Points by Axis Parallel Lines')
    plt.scatter(x_axis, y_axis, color='black')
    for vertical_line in vertical_lines:
        plt.axvline(vertical_line)

    for horizontal_line in horizontal_lines:
        plt.axhline(horizontal_line)

    plt.savefig(output_file_name[0:-4])
