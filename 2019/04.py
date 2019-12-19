def get_possible_password_values_count(max_len, start, end):
    def does_value_increment(val):
        str_val = str(val)
        for i in range(0, len(str_val) - 1):
            a = str_val[i]
            b = str_val[i + 1]
            if b < a:
                return False

        return True

    def does_value_contain_duplicate(val):
        str_val = str(val)
        for i in range(0, len(str_val)-1):
            a = str_val[i]
            b = str_val[i+1]
            if a == b:
                return True

        return False

    total = 0
    for i in range(start, end + 1):
        incremental_number = does_value_increment(i)
        contains_duplicate = does_value_contain_duplicate(i)

        if incremental_number and contains_duplicate:
            total += 1

    return total


result = get_possible_password_values_count(6, 387638, 919123)
print(result)


