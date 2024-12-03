from input import input

report_list = input.split("\n")
safe_count = 0

for report in report_list:
    level_list = report.split(" ")
    increase = None
    for level_index in range(len(level_list)-1):
        difference = int(level_list[level_index + 1]) - int(level_list[level_index])
        if increase is None:
            if difference > 0:
                increase = True
            elif difference < 0:
                increase = False
            elif difference == 0:
                break
        if increase is True and difference < 0:
            break
        if increase is False and difference > 0:
            break
        if difference > 3 or difference < -3 or difference == 0:
            break
        if level_index == len(level_list) - 2:
            safe_count += 1

print(safe_count)
