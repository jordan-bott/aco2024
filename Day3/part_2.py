from input import input
import re

input_split_by_dont = input.split("don't()")

do_inputs = []
muls_in_string_before_first_dont = re.findall("mul[(][0-9]{1,3}[,][0-9]{1,3}[)]", input_split_by_dont[0])
do_inputs += muls_in_string_before_first_dont
for s in input_split_by_dont:
    if "do()" in s:
        dont_inputs_split_by_do = s.split("do()")
        for index in range(1, len(dont_inputs_split_by_do)):
            list_of_do_muls = re.findall("mul[(][0-9]{1,3}[,][0-9]{1,3}[)]", dont_inputs_split_by_do[index])
            do_inputs += list_of_do_muls

mul_total = 0

for mul in do_inputs:
    mul_without_beginning = mul.replace("mul(", "")
    mul_without_beg_or_end = mul_without_beginning.replace(")", "")
    mul_num_list = mul_without_beg_or_end.split(",")
    mul_total += int(mul_num_list[0]) * int(mul_num_list[1])


print(mul_total)
