# SRT Text EXTractor
A tool for extracting text from SRT subtitles

## Requirements
- Python2

## Installation
### Manual
```bash
git clone https://github.com/nyukhalov/srt-text.git
sudo python setup.py install
```

### Using pip
```bash
pip install git+https://github.com/nyukhalov/srt-text.git
```

## Usage
```bash
srt-text <PATH_TO_SRT_FILE>
```

## Example
For the subtitles below
```
1
00:02:17,440 --> 00:02:20,375
Senator, we're making
our final approach into Coruscant.

2
00:02:20,476 --> 00:02:22,501
Very good, Lieutenant.
```

outcome will be
```
Senator, we're making our final approach into Coruscant. Very good, Lieutenant.
```
