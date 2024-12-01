from input import input

input_list = input.split("\n")

comparison_list = [item.split("   ") for item in input_list]

left_list = []
right_list = []
for pair in comparison_list:
    left_list.append(int(pair[0]))
    right_list.append(int(pair[1]))

left_list.sort()
right_list.sort()

total_difference = 0

for index in range(len(left_list)):
    difference = left_list[index] - right_list[index]
    total_difference += abs(difference)

print(total_difference)
