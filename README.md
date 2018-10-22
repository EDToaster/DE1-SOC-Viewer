# DE1-SOC-Viewer
Converts the waveforms out of Modelsim into a visualized format

## Usage
### Requirements
- Modelsim
- DE1-SoC.qsf pin assignment file
- python3
- pygame

### Extracting waveforms
- All units in program is in milliseconds, use values accordingly.
1. Make sure each vector IO in your top-level modules is the same width as they appear on the board
   For example, the ```LEDR``` output should be defined as ```output [9:0] LEDR``` and ```SW``` input should be defined as ```input [9:0] SW```
2. Append ```add list *``` to the end of the modelsim macros (```.do```) file
3. Open up ```modelsim```, ```cd``` into your working directory, and run your macros file.
4. Select the ```List``` window, go to ```File -> Export -> Event List``` and save the file in the same directory as the python files.
5. Run ```python3 main.py <lst file>``` and you should see something similar to the screenshot underneath.

### Sample screenshot
![Screenshot][Sample]

## Troubleshooting
- The window opens and closes immediately!
  > Make sure your runtime is long enough, in ```ms```

[Sample]: https://github.com/EDToaster/DE1-SOC-Viewer/blob/master/sample/counter.png
