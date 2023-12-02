total = 0
def extract_games(text):
    split_text = text.rstrip().split(": ")
    split_text[0] = int(split_text[0].replace("Game ", ""))
    split_text[1] = split_text[1].split("; ")
    return split_text

def count_cubes(text):
    for round in text[1]:
        round = round.split(", ")
        for colour in round:
            if "green" in colour:
                green = int(colour.replace(" green", ""))
                if green > 13:
                    return text[0], False
            elif "red" in colour:
                red = int(colour.replace(" red", ""))
                if red > 12:
                    return text[0], False
            elif "blue" in colour:
                blue = int(colour.replace(" blue", ""))
                if blue > 14:
                    return text[0], False
    return text[0], True
    

total = 0
with open("2/input_2.txt", "r") as file:
    for line in file:
        game, result = count_cubes(extract_games(line))
        if result:
            total += game

print(total)
