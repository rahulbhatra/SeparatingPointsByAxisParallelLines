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


class Output:
    def __init__(self, number_of_lines: int, vertical_lines: [], horizontal_lines: []):
        self.number_of_lines = number_of_lines
        self.vertical_lines = vertical_lines
        self.horizontal_lines = horizontal_lines


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


def read_input(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    input = Input(int(lines[0]), [], file_name)
    # print(lines[0])

    for i in range(1, len(lines)):
        x, y = lines[i].split()
        x, y = int(x), int(y)
        # print(x, y)
        input.add_coordinate(x, y)
    return input


def write_output(file_name, output: Output):
    file = open(file_name, 'w')
    lines = str(output.number_of_lines) + '\n'

    for i in range(0, len(output.horizontal_lines)):
        lines += "h " + str(output.horizontal_lines[i]) + "\n"

    for i in range(0, len(output.vertical_lines)):
        lines += "v " + str(output.vertical_lines[i]) + "\n"

    file.writelines(lines)
