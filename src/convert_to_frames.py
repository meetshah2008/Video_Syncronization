import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Get video properties
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Video FPS: {fps}")
    print(f"Total frames: {total_frames}")

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Save each frame as an image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

        print(f"Saved frame {frame_count}/{total_frames}", end="\r")

    video.release()
    print(f"\nFrames saved to folder: {output_folder}")

# Main function
if __name__ == "__main__":
    video_path = "number_sequence.mp4"  # Replace with your video file path
    output_folder = "frames_output"  # Replace with your desired output folder name
    extract_frames(video_path, output_folder)
