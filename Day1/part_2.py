from input import input

input_list = input.split("\n")

comparison_list = [item.split("   ") for item in input_list]

left_list = []
right_list = []
for pair in comparison_list:
    left_list.append(int(pair[0]))
    right_list.append(int(pair[1]))

occurrence_count_dict = {}

similarity_score = 0

for num in left_list:
    if num not in occurrence_count_dict:
        occurrence_count_dict[num] = right_list.count(num)
    similarity_score += num * occurrence_count_dict[num]

print(similarity_score)
