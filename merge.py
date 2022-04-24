import csv
import difflib

from line import Line

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
        return matches
    bunches = []
    parts = slice_to_4(text)
    for part in parts:
        matches = difflib.get_close_matches(part, srt_arr, n=1)
        if matches:
            bunches.append(matches[0])
    return bunches

def main():
    with open(SCRIPT_FILE, newline='') as f:
        # handler for script (csv)
        script_reader = csv.reader(f)
        results = []
        
        # handler for srt (list)
        dict_srt = get_srt()
        index = 0
        for line in script_reader:
            if index%10 == 0:
                print (f"{index/1303*100}%", end="\r")
            found_matches = get_closest_match(line[2], dict_srt.keys())
            for match in found_matches:
                results.append(Line(dict_srt[match][0], dict_srt[match][1].strip(), match, line[1]))
            index += 1 

    print("Finished processing. Now sorting")
    results.sort(reverse=True)
    results.reverse()
    with open("merge.csv", "w", newline='') as merge_csv:
        csvwriter = csv.writer(merge_csv)
        csvwriter.writerow(["Begin", "dissapear", "Content", "speaker"])
        for res in results:
            csvwriter.writerow(res.to_csv())



if __name__ == "__main__":
    main()
