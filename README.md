# DAVIS-eventCamera-processing
## Event Camera Data Processing

This repository contains Python scripts for processing data from event-based cameras. These scripts provide functionalities such as invoking, playing, reading, and writing data from event cameras.
The code is located in the `test_davis` folder and relies on the [DV Processing Library](https://gitlab.com/inivation/dv/dv-processing/) from iniVation.

## Features

- **Invoke Event Cameras:** Interface with event cameras to start and stop capturing events.
- **Playback:** Play back recorded event data.
- **Read and Write:** Read from and write event data to files for further processing or analysis.

## Prerequisites
To use this repository, you need to have the DV Processing Library installed. See in https://gitlab.com/inivation/dv/dv-processing/

Please follow the official installation guide provided by iniVation:
[DV Processing Installation Guide](https://dv-processing.inivation.com/rel_1_7/installation.html).

## Usage

1. Navigate to the `test_davis` folder:
   ```bash
   cd test_davis
   ```

2. Run the Python scripts for the desired functionality. For example, to play event data:
   ```bash
   python show_events_and_frames.py
   ```

   Replace `show_events_and_frames.py` with the appropriate script name for other functionalities.

## Dependencies
- Python 3.x
- DV Processing Library (refer to the [installation guide](https://gitlab.com/inivation/dv/dv-processing/))
- Additional Python dependencies

## Documentation

For more information on how to use the DV Processing Library, refer to its [official documentation](https://docs.inivation.com/software/introduction.html).


## Acknowledgments

This project uses the DV Processing Library developed by iniVation. Visit their [website](https://inivation.com/) for more details.

