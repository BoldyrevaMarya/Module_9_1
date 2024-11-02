def apply_all_func(int_list, *functions):
    results = {}
    for funct in functions:
        results[funct.__name__] = funct(int_list)
    return results


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
