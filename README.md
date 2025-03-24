# Number Sequence Generator for Synchronization

This Python script generates a video displaying sequential numbers at a specified frame rate (FPS). It is designed for use cases like synchronizing video frames recorded on multiple devices by comparing the sequential numbers in the generated video. The video is saved in MP4 format, and the number updates in real-time.

## Features

- Displays a full-screen sequential number updated at a specified FPS.
- Saves the generated video in MP4 format.
- Easily configurable to adjust FPS, video resolution, and output file name.

## Prerequisites

Make sure you have Python installed along with the following libraries:
- `pygame`
- `opencv-python`
- `numpy`

## Configuration
You can customize the script as per your requirements:
1) To adjust the frame rate of the generated video ( according to your video) and output file name and path , modify the fps parameter in the main function
-- main(fps=30, output_file="number_sequence.mp4")

## How to Use

### Clone the Repository  
Clone this repository and navigate to the `src` folder:  
```bash
git clone <repository-url>
cd repo_name/src
python number_sequence.py

