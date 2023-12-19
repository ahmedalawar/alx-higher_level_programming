#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                val1 = my_list_1[i] if i < len(my_list_1) else None
                val2 = my_list_2[i] if i < len(my_list_2) else None

                if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                    if val2 != 0:
                        result = val1 / val2
                        result_list.append(result)
                    else:
                        result_list.append(0)
                        print("division by 0")
                else:
                    result_list.append(0)
                    print("wrong type")

            except TypeError:
                result_list.append(0)
                print("wrong type")
            except IndexError:
                result_list.append(0)
                print("out of range")

    finally:
        return result_list[:list_length]

