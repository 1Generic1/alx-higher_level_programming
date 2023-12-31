#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                    if element_2 == 0:
                        result_list.append(0)
                        print("division by 0")
                    else:
                        result = element_1 / element_2
                        result_list.append(result)
                else:
                    result_list.append(0)
                    print("wrong type")
            except IndexError:
                result_list.append(0)
                print("out of range")
    finally:
        return result_list
