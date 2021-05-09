# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from InputOutput import *
from SeparatingPointsByAxisParallelLines import *
import time
import datetime
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    number_of_files = 6
    print(len(sys.argv))
    if len(sys.argv) == 2:
        number_of_files = int(sys.argv[1])

    print("\nPlease See if Number of Files Provided is Correct ! The number of files is: ", number_of_files)

    inputs = read_inputs(number_of_files)

    i = 1
    for input in inputs:
        starting_time = time.time_ns()

        print("\nStarting File: ", input.file_name, "Starting Time: ", datetime.datetime.now())
        vertical_lines, horizontal_lines = separating_points_by_axis_parallel_lines(input.number_of_coordinates,
                                                                                    input.coordinates)
        output_file_name = 'local_solution'
        if i < 10:
            output_file_name += str(0)
        output_file_name += str(i) + ".txt"
        i += 1

        output = Output(len(vertical_lines) + len(horizontal_lines), vertical_lines, horizontal_lines)
        print("Starting Writing in File: ", output_file_name)
        write_output(output_file_name, output)
        ending_time = time.time_ns()

        time_taken = (ending_time - starting_time) / (10 ** 9)
        print("Time Taken: ", time_taken, "Seconds\n\n")

        compare_feasibility_algorithms(input.number_of_coordinates, input.coordinates, vertical_lines, horizontal_lines)
        prepare_plot(input.coordinates, vertical_lines, horizontal_lines, output_file_name)
