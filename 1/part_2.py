final = 0
numbers = {
      "one": "o1e",
      "two": "t2o",
      "three": "t3e",
      "four": "f4r",
      "five": "f5e",
      "six": "s6x",
      "seven": "s7n",
      "eight": "e8t",
      "nine": "n9e"
}

def replace_words(text):
    for k, v in numbers.items():
        text = text.replace(k, v)
    return text

with open("input_1.txt", "r") as input_1:
    for line in input_1:
        cal_value = list(filter(str.isdigit, replace_words(line)))
        actual = str(cal_value[0]) + str(cal_value[-1])
        final += int(actual)
                

print(final)