import csv
SRT_FILE = "The.Trial.of.the.Chicago.7.2020.720p.WEBRip.800MB.x264-GalaxyRG.srt"

def get_lines():
    with open(SRT_FILE, "r", encoding="utf-8") as f:
        return f.readlines()

def main():
    with open("srt-English.csv", "w", newline='') as srt_csv:
        csvwriter = csv.writer(srt_csv)
        csvwriter.writerow(["Begin", "Disapear", "Text"])
        lines = get_lines()
        in_interval = False
        text = ""
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
