from input import input

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
57 56 57 59 60 63 64 65"""

report_list = input.split("\n")
safe_count = 0

for report in report_list:
    level_list = report.split(" ")
    increase = None
    unsafe = False
    unsafe_index = None
    print("\nlevel list:" , level_list)
    for level_index in range(len(level_list)-1):
        difference = int(level_list[level_index + 1]) - int(level_list[level_index])
        if increase is None:
            if difference > 0:
                increase = True
            elif difference < 0:
                increase = False
            elif difference == 0:
                print("difference is 0")
                unsafe = True
                unsafe_index = level_index
                break
        if increase is True and difference < 0:
            print("increase true, difference negative")
            unsafe = True
            unsafe_index = level_index
            break
        if increase is False and difference > 0:
            print("increase false, difference positive")
            unsafe = True
            unsafe_index = level_index
            break
        if difference > 3 or difference < -3 or difference == 0:
            print("difference is too high, too low, or 0")
            unsafe = True
            unsafe_index = level_index
            break
        if level_index == len(level_list) - 2:
            print("safe count increased")
            safe_count += 1
    if unsafe is True:
        print("unsafe is true")
        print("unsafe index:", unsafe_index)
        original_level_list = list(level_list)
        original_level_list_2 = list(level_list)
        level_list.pop(unsafe_index)
        increase = None
        check_one_unsafe = False
        print("popped level list:", level_list)
        for level_index in range(len(level_list)-1):
            difference = int(level_list[level_index + 1]) - int(level_list[level_index])
            if increase is None:
                if difference > 0:
                    increase = True
                elif difference < 0:
                    increase = False
                elif difference == 0:
                    check_one_unsafe = True
                    break
            if increase is True and difference < 0:
                print("unsafe is true & increase is true, difference is negative")
                check_one_unsafe = True
                break
            if increase is False and difference > 0:
                print("unsafe is true & increase is false, difference is positive")
                check_one_unsafe = True
                break
            if difference > 3 or difference < -3 or difference == 0:
                print("unsafe is true & difference is too high, too low, or 0")
                check_one_unsafe = True
                break
            if level_index == len(level_list) - 2:
                print("safe count increased")
                safe_count += 1
        if check_one_unsafe and unsafe_index < len(original_level_list) - 1:
            print("check one unsafe")
            original_level_list.pop(unsafe_index + 1)
            increase = None
            check_two_unsafe = False
            print("popped original level list:", original_level_list)
            for level_index in range(len(original_level_list)-1):
                difference = int(original_level_list[level_index + 1]) - int(original_level_list[level_index])
                if increase is None:
                    if difference > 0:
                        increase = True
                    elif difference < 0:
                        increase = False
                    elif difference == 0:
                        check_two_unsafe = True
                        break
                if increase is True and difference < 0:
                    print("check two unsafe is true & increase is true, difference is negative")
                    check_two_unsafe = True
                    break
                if increase is False and difference > 0:
                    print("check two unsafe is true & increase is false, difference is positive")
                    check_two_unsafe = True
                    break
                if difference > 3 or difference < -3 or difference == 0:
                    print("check two unsafe is true & difference is too high, too low, or 0")
                    check_two_unsafe = True
                    break
                if level_index == len(level_list) - 2:
                    print("safe count increased")
                    safe_count += 1
            if check_two_unsafe and unsafe_index != 0:
                print("check two unsafe")
                original_level_list_2.pop(unsafe_index - 1)
                increase = None
                print("popped original level list 2:", original_level_list_2)
                for level_index in range(len(original_level_list_2)-1):
                    difference = int(original_level_list_2[level_index + 1]) - int(original_level_list_2[level_index])
                    if increase is None:
                        if difference > 0:
                            increase = True
                        elif difference < 0:
                            increase = False
                        elif difference == 0:
                            break
                    if increase is True and difference < 0:
                        print("check three unsafe is true & increase is true, difference is negative")
                        break
                    if increase is False and difference > 0:
                        print("check three unsafe is true & increase is false, difference is positive")
                        break
                    if difference > 3 or difference < -3 or difference == 0:
                        print("check three unsafe is true & difference is too high, too low, or 0")
                        break
                    if level_index == len(level_list) - 2:
                        print("safe count increased")
                        safe_count += 1


print(safe_count)
