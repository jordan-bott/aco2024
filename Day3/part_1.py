from input import input
import re

list_of_muls = re.findall("mul[(][0-9]{1,3}[,][0-9]{1,3}[)]", input)

mul_total = 0

for mul in list_of_muls:
    mul_without_beginning = mul.replace("mul(", "")
    mul_without_beg_or_end = mul_without_beginning.replace(")", "")
    mul_num_list = mul_without_beg_or_end.split(",")
    mul_total += int(mul_num_list[0]) * int(mul_num_list[1])

print(mul_total)
