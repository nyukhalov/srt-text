#!/usr/bin/env python

import sys

class SrtText():
    def __init__(self):
        self.state = 'SUB_NO' # or TIME or SUB or BLANK
        self.text = ''

    def changeStatusSubNo(self):
        self.state = 'SUB_NO'

    def changeStatusTime(self):
        self.state = 'TIME'

    def changeStatusSub(self):
        self.state = 'SUB'

    def changeStatusBlank(self):
        self.state = 'BLANK'

    def startSubNo(self, line):
        self.changeStatusSubNo()
        self.handle(line)

    def startTime(self, line):
        self.changeStatusTime()
        self.handle(line)

    def startSub(self, line):
        self.changeStatusSub()
        self.handle(line)

    def startBlank(self, line):
        self.changeStatusBlank()
        self.handle(line)

    def handle(self, line):
        line = line.strip()
        if self.state == 'SUB_NO':
            self.changeStatusTime()
        elif self.state == 'TIME':
            self.changeStatusSub()
        elif self.state == 'SUB':
            if self.is_blank(line):
                self.startBlank(line)
            else:
                self.text += ' ' + line
        elif self.state == 'BLANK':
            self.changeStatusSubNo()
        else:
            raise ValueError, 'unexpected state: ' + self.state

    def is_blank(self, line):
        return not line


def main():
    if len(sys.argv) != 2:
        print 'Usage: srt-text <PATH_TO_SRT_FILE>'
        sys.exit(1)

    srt_path = sys.argv[1]
    with open(srt_path, "r") as f:
        srtText = SrtText()
        for line in f:
            srtText.handle(line)

        print srtText.text


if __name__ == "__main__":
    main()

