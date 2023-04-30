import cv2
import numpy as np
from moviepy.editor import ImageSequenceClip

# Load the mask (PNG file with transparency)
mask = cv2.imread('image_folder/image.png', cv2.IMREAD_UNCHANGED)

# Extract the alpha channel from the mask (transparency information)
mask_alpha = mask[:, :, 3] / 255.0

# Remove the alpha channel from the mask, leaving only the color channels (BGR)
mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR)

# Load the video
video_path = 'input/video.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

frames = []

# Iterate through the frames of the video
while cap.isOpened():
    ret, frame = cap.read()

    # Break the loop if we've reached the end of the video
    if not ret:
        break

    # Resize the mask and its alpha channel to the frame size
    resized_mask = cv2.resize(mask, (width, height))
    resized_mask_alpha = cv2.resize(mask_alpha, (width, height))

    # Manually apply the weights using NumPy to blend the mask with the video frame
    frame_weighted = frame * (1 - resized_mask_alpha[..., None])
    mask_weighted = resized_mask * resized_mask_alpha[..., None]
    frame = cv2.add(frame_weighted, mask_weighted).astype(np.uint8)

    # Convert frame from BGR (OpenCV) to RGB (moviepy)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Add the modified frame to the list of frames
    frames.append(frame_rgb)

# Release the video objects
cap.release()
cv2.destroyAllWindows()

# Create a moviepy ImageSequenceClip from the list of frames
video_clip = ImageSequenceClip(frames, fps=fps)

# Set the output video name
output_video_name = 'output/video.mp4'

# Write the video clip to the output file
video_clip.write_videofile(output_video_name, codec="libx264", bitrate="500k")

print('Frame added to video!')
