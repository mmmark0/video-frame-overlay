# Video Frame Overlay

This script, `video_frame_overlay.py`, add an image overlay to video frames and saves the result as a new video file.

## Requirements

- Python
- OpenCV
- moviepy

## Installation

1. Install the required packages by running: `pip install -r requirements.txt`.

## Usage

1. Place your video file in the `input` directory and name it `video.mp4`.
2. Place your PNG overlay image with transparency in the `image_folder` directory and name it `image.png`.
3. Run the script: `python overlay_video.py`.
4. The resulting video with the overlay will be saved in the `output` directory as `video.mp4`.

## Notes

- The script automatically resizes the image overlay to match the dimensions of the video.
- The image overlay must be in PNG format with an alpha channel for transparency.
