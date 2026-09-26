
def main():

    result_array = []

    for i in range(100, 1000):

        string_num = ""

        sum_of_digits = 0
        sum_of_digits_after_del = 0

        if (i % 3 != 0):
            continue

        string_num = str(i)

        for digit in string_num:
            sum_of_digits += int(digit)

        for chastnoe in str(int(string_num) // 3):
            sum_of_digits_after_del += int(chastnoe)

        if sum_of_digits > sum_of_digits_after_del:
            result_array.append(i)

    print(result_array)


if __name__ == "__main__":
    main()
