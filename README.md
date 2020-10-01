# Sound

1.  Filter by volume
2.  Add some time delay after user finishes speaking

State 1: Wait for speech

State 2: Record speech

State 3: Write the audio file

1.  `main.py` - User runs this file
2.  `sound.py`
    1.  `func detectspeech` - wait for speech (detect decibels louder than x db)
    2.  `func recordspeech` - record speech
    3.  `func writespeech` - writes the speech