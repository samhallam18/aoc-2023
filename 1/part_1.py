final = 0
with open("input_1.txt", "r") as input_1:
        for line in input_1:
            cal_value = list(filter(str.isdigit, line))
            actual = str(cal_value[0]) + str(cal_value[-1])
            final += int(actual)

print(final)