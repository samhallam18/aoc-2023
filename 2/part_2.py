total = 0
def extract_games(text):
    split_text = text.rstrip().split(": ")
    split_text[0] = int(split_text[0].replace("Game ", ""))
    split_text[1] = split_text[1].split("; ")
    return split_text

def count_cubes(text):
    min_green = 0
    min_red = 0
    min_blue = 0
    for round in text[1]:
        round = round.split(", ")
        for colour in round:
            if "green" in colour:
                green = int(colour.replace(" green", ""))
                if green > min_green:
                    min_green = green
            elif "red" in colour:
                red = int(colour.replace(" red", ""))
                if red > min_red:
                    min_red = red
            elif "blue" in colour:
                blue = int(colour.replace(" blue", ""))
                if blue > min_blue:
                    min_blue = blue
    return min_green * min_red * min_blue
    

total = 0
with open("2/input_2.txt", "r") as file:
    for line in file:
        total += count_cubes(extract_games(line))
        
print(total)
