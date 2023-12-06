def nested_to_linear(nested_list, result=[]):

    for i in nested_list:
        if type(i) == list:
            nested_to_linear(i, result)
        else:
            result.append(i)
    return result

print(nested_to_linear(["start", 10, [4, 2, [11, [9, "mid", 3, [1, 0], 6]], 8], "Done"]))
