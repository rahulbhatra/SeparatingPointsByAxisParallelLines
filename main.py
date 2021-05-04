# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from InputOutput import *
from SeparatingPointsByAxisParallelLines import *
import time
import datetime
import matplotlib.pyplot as plt
from CheckFeasiblity import *
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    number_of_files = 1
    if len(sys.argv) == 2:
        number_of_files = int(sys.argv[1])

    inputs = read_inputs(1)

    i = 1
    for input in inputs:
        starting_time = time.time_ns()

        print("Starting File: ", input.file_name)
        print("Starting Time: ", datetime.datetime.now())
        vertical_lines, horizontal_lines = separating_points_by_axis_parallel_lines(input.number_of_coordinates, input.coordinates)
        # vertical_lines = [3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
        # horizontal_lines = [7.25]
        output_file_name = 'local_solution'
        if i < 10:
            output_file_name += str(0)
        output_file_name += str(i) + ".txt"
        i += 1
        number_of_vertical_lines = len(vertical_lines)
        number_of_horizontal_lines = len(horizontal_lines)
        output = Output(number_of_horizontal_lines + number_of_vertical_lines, vertical_lines, horizontal_lines)
        print("Starting Writing in File: ", output_file_name)
        write_output(output_file_name, output)

        ending_time = time.time_ns()

        time_taken = (ending_time - starting_time) / (10 ** 9)
        print("Time Taken: ", time_taken, "Seconds")

        x_axis = []
        y_axis = []
        for coordinate in input.coordinates:
            x_axis.append(coordinate[0])
            y_axis.append(coordinate[1])

        print('x_axis', x_axis)
        print('y_axis', y_axis)
        print('vertical lines', vertical_lines)
        print('horizontal lines', horizontal_lines)

        is_feasible = check_feasibility(input.number_of_coordinates, input.coordinates, vertical_lines, horizontal_lines)
        print(is_feasible)
        is_feasible = check_is_feasible(input.number_of_coordinates, input.coordinates, vertical_lines, horizontal_lines)
        print(is_feasible)

        plt.figure(figsize=(30, 25))
        plt.scatter(x_axis, y_axis)
        for vertical_line in vertical_lines:
            plt.axvline(vertical_line)

        for horizontal_line in horizontal_lines:
            plt.axhline(horizontal_line)

        plt.savefig(output_file_name[0:-4])

