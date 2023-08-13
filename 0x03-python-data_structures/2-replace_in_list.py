#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = list.copy(my_list)
    if idx < 0 or idx > len(new_list):
        return new_list
    new_list[idx] = element
    return new_list[idx]
