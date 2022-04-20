import csv
import difflib

SCRIPT_FILE = "script.csv"
SRT_FILE = "srt-English.csv"


def get_script():
    with open(SCRIPT_FILE, newline='') as f:
        return csv.reader(f)

def get_srt():
    with open(SRT_FILE , newline='') as f:
        srt_arr = []
        r = csv.reader(f)

        dict_srt = {} 
        for row in r:
            key =  row[2] # key = text
            value = (row[0], row[1])
            dict_srt[key]=value    
    # print(script_arr)

    return dict_srt

def slice_to_4(to_slice):
    return to_slice[0:len(to_slice)//4], to_slice[len(to_slice)//4:len(to_slice)//2], to_slice[len(to_slice)//2:len(to_slice)//4*3], to_slice[len(to_slice)//4*3:]

def get_closest_match(text, srt_arr):
    matches = difflib.get_close_matches(text, srt_arr, n=1)
    if matches:
        return matches[0]
    parts = slice_to_4(text)
    broken = ""
    for part in parts:
        matches = difflib.get_close_matches(part, srt_arr, n=1)
        if matches:
            return matches[0]


def main():
    with open(SCRIPT_FILE, newline='') as f:
        # handler for script (csv)
        script_reader = csv.reader(f)
    

        # handler for srt (list)
        dict_srt = get_srt()

        for line in script_reader:
            found_match = get_closest_match(line[2], dict_srt.keys())
            print(str(dict_srt[found_match]) + "   " + found_match + "  " + line[1]  )





def ddmain():
    with open("srt-script.csv", "w", newline='') as srt_csv:
        csvwriter = csv.writer(srt_csv)
        csvwriter.writerow(["Begin", "Disapear", "Text", "Speaker"])
        script_reader, srt_reader  = get_lines()
        # in_interval = False
        # text = ""

        for line in lines:
            if not line.isnumeric(): # skip on the index number
                if '-->' in line:
                    begin = line.split(' --> ')[0] # parse the begin time
                    end = line.split(' --> ')[1] # parse the end time
                    in_interval = True  # now the following lines till \n\n are the content
                
                elif in_interval:
                    if line == "\n":
                        in_interval = False
                        csvwriter.writerow([begin, end, text.strip()])
                        text = ""
                    else:
                        text += line.strip() + " "


if __name__ == "__main__":
    main()
