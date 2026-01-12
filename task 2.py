# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)
    set1 = set(participants1)
    set2 = set(participants2)
    common_participants = set1.intersection(set2)
    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common)

participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"
common_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma)
print(common_comma)

# TODO Провеьте работу функции с разделителем отличным от запятой
