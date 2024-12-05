from input import input
import re

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

splitput = input.split("\n")

# print(splitput)


# find horizontal front & back
def Find_Horizontal(input):
    xmas_and_samx_count = 0
    for line in input:
        xmas_and_samx_list = re.findall(r'(?=(XMAS|SAMX))', line)
        xmas_and_samx_count += len(xmas_and_samx_list)
    return xmas_and_samx_count


# find vertical front & back
def Find_Vertical(input):
    rotated_input = list(zip(*reversed(input)))

    xmas_and_samx_count = 0
    for line in rotated_input:
        line_string = "".join(line)
        xmas_and_samx_list = re.findall(r'(?=(XMAS|SAMX))', line_string)
        xmas_and_samx_count += len(xmas_and_samx_list)
    return xmas_and_samx_count

# find diagonal front & back
def Find_Right_To_Left_Diagonal(input):
    left_side_diagonal_2d_array = []
    right_side_diagonal_2d_array = []
    width = len(input[0])
    height = len(input)
    left_side_counter = 0
    right_side_counter = 0
    # make left side & center diagonal lines
    for w_index in range(width):
        for h_index in range(height):
            if w_index == 0:
                left_side_diagonal_2d_array.append([input[h_index][w_index]])
            elif left_side_counter + h_index < len(input):
                left_side_diagonal_2d_array[h_index].append(input[h_index + left_side_counter][w_index])
            else:
                break
        left_side_counter += 1
    # make right side only diagonals
    for h_index in range(height):
        for w_index in range(1, width):
            if h_index == 0:
                right_side_diagonal_2d_array.append([input[h_index][w_index]])
            elif right_side_counter + w_index < width:
                right_side_diagonal_2d_array[w_index - 1].append(input[h_index][w_index + right_side_counter])
            else:
                break
        right_side_counter += 1

    diagonal_2d_array = left_side_diagonal_2d_array + right_side_diagonal_2d_array

    xmas_and_samx_count = 0
    for line in diagonal_2d_array:
        line_string = "".join(line)
        xmas_and_samx_list = re.findall(r'(?=(XMAS|SAMX))', line_string)
        xmas_and_samx_count += len(xmas_and_samx_list)
    return xmas_and_samx_count

def Find_Left_To_Right_Diagonal(input):
    rotated_input = list(zip(*reversed(input)))
    left_side_diagonal_2d_array = []
    right_side_diagonal_2d_array = []
    width = len(rotated_input[0])
    height = len(rotated_input)
    left_side_counter = 0
    right_side_counter = 0
    # make left side & center diagonal lines
    for w_index in range(width):
        for h_index in range(height):
            if w_index == 0:
                left_side_diagonal_2d_array.append([rotated_input[h_index][w_index]])
            elif left_side_counter + h_index < len(rotated_input):
                left_side_diagonal_2d_array[h_index].append(rotated_input[h_index + left_side_counter][w_index])
            else:
                break
        left_side_counter += 1
    # make right side only diagonals
    for h_index in range(height):
        for w_index in range(1, width):
            if h_index == 0:
                right_side_diagonal_2d_array.append([rotated_input[h_index][w_index]])
            elif right_side_counter + w_index < width:
                right_side_diagonal_2d_array[w_index - 1].append(rotated_input[h_index][w_index + right_side_counter])
            else:
                break
        right_side_counter += 1

    diagonal_2d_array = left_side_diagonal_2d_array + right_side_diagonal_2d_array

    xmas_and_samx_count = 0
    for line in diagonal_2d_array:
        line_string = "".join(line)
        xmas_and_samx_list = re.findall(r'(?=(XMAS|SAMX))', line_string)
        xmas_and_samx_count += len(xmas_and_samx_list)
    return xmas_and_samx_count

#find total
total_count = 0
horizontal_count = Find_Horizontal(splitput)

vertical_count = Find_Vertical(splitput)

rtl_diagonal_count = Find_Right_To_Left_Diagonal(splitput)

ltr_diagonal_count = Find_Left_To_Right_Diagonal(splitput)


total_count += horizontal_count
total_count += vertical_count
total_count += rtl_diagonal_count
total_count += ltr_diagonal_count
print(total_count)
