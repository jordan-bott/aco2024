from input import input

splitput = input.split("\n")
width = len(splitput[0])
height = len(splitput)

x_mas_count = 0

for h_index in range(1, height - 1):
    for w_index in range(1, width - 1):
        if splitput[h_index][w_index] == "A":
            # check left to right x
            left_to_right = False
            if splitput[h_index - 1][w_index - 1] == "S" and splitput[h_index + 1][w_index + 1] == "M":
                left_to_right = True
            elif splitput[h_index - 1][w_index - 1] == "M" and splitput[h_index + 1][w_index + 1] == "S":
                left_to_right = True
            right_to_left = False
            if splitput[h_index - 1][w_index + 1] == "S" and splitput[h_index + 1][w_index - 1] == "M":
                right_to_left = True
            elif splitput[h_index - 1][w_index + 1] == "M" and splitput[h_index + 1][w_index - 1] == "S":
                right_to_left = True
            if left_to_right is True and right_to_left is True:
                x_mas_count += 1

print(x_mas_count)
