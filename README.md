# Sound

A tool to detect and save user voice recording

## Features
1.  Filter by volume
2.  Add some time delay after user finishes speaking

## Files 
1.  `main.py` - User runs this file
2.  `sound.py` - Main sound functionality
3. `demo[x].py` - Some toy examples of how to use the sounddevice python module

# Getting started

```
git clone https://github.com/Zhu-Justin/Sound.git /path/to/repo

cd /path/to/repo
pip3 install -r ./requirements.txt

./main.py -o "filename.wav"
```

You should see "Recording" when you are talking and then "Not Recording" when you are not talking. If you have not been talking for a long time, the program exits. The total time of the program runs is 10 seconds by default.

# Getting help
```
./main.py  -h
```

# Notes

Depending on your machine, you might be getting a feedback loop.

Furthermore, after the program from not
detecting any human voice, you might need to
press Ctrl-C to fully exit the program.


