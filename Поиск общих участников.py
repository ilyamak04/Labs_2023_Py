def find_common_participants(str1, str2, separator=','):
    str1_list = str1.split(separator)
    str2_list = str2.split(separator)
    str2_new_set = set(str2_list)
    intersection_str = str2_new_set.intersection(str1_list)
    common = list(intersection_str)
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
