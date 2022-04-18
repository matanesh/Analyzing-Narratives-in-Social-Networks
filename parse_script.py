import csv
SCRIPT_FILE = "Script.txt"

def get_lines():
    with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def isSpeaker(line):
    return line.isupper() and line.startswith(" "*16) and "CUT TO" not in line and "DISSOLVE" not in line

def main():
    people = set()
    with open("script.csv", "w", newline='') as script_csv:
        csvwriter = csv.writer(script_csv)
        csvwriter.writerow(["Response number", "Speaker", "Content"])
        index = 1
        lines = get_lines()
        in_speaker = False
        text = ""
        for line in lines:
            if in_speaker:
                if line == "\n":
                    in_speaker = False
                    csvwriter.writerow([index, speaker, text.strip()])
                    text = ""
                    index += 1 
                else:
                    text += line.strip() + " "

            elif isSpeaker(line):
                in_speaker = True
                speaker = line.strip()
                if "(" in speaker:
                    speaker = speaker.split("(")[0].strip()
                people.add(speaker)

if _name_ == "_main_":
    main()