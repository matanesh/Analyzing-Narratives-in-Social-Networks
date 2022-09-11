
class Line:
    def __init__(self, begin, end, text, speaker):
        self.begin = begin
        self.end = end
        self.text = text
        self.speaker = speaker

    def __lt__(self, other):
        # compare hours
        if int(self.begin[:2]) < int(other.begin[:2]):
            return True
        elif int(self.begin[:2]) > int(other.begin[:2]):
            return False

        #compare minutes
        if int(self.begin[3:5]) < int(other.begin[3:5]):
            return True
        elif int(self.begin[3:5]) > int(other.begin[3:5]):
            return False

        # compare seconds
        if int(self.begin[6:8]) < int(other.begin[6:8]):
            return True
        elif int(self.begin[6:8]) > int(other.begin[6:8]):
            return False

        return True

    def to_csv(self):
        return [self.begin, self.end, self.text, self.speaker]
    
    def __repr__(self):
        return f"{self.begin = } {self.end = } {self.text = } {self.speaker = }"