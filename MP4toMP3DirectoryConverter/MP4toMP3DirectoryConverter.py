import os
from moviepy.editor import VideoFileClip

def convert_to_mp3(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all .mp4 files in the input directory
    # You can change .mp4 to most other video file extensions
    files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]

    for file in files:
        file_path = os.path.join(input_dir, file)
        output_file = os.path.splitext(file)[0] + ".mp3"
        output_path = os.path.join(output_dir, output_file)

        # Load the video file
        video = VideoFileClip(file_path)

        # Extract audio and save as .mp3
        audio = video.audio
        audio.write_audiofile(output_path, codec='mp3')

        # Close the video file
        video.close()

        print(f"Converted {file} to {output_file}")

# Example usage
# CHANGE THESE VARIABLES TO YOUR ACTUAL INPUT/OUTPUT DIRECTORY
input_directory = r"C:\Music\example"
output_directory = r"C:\Music\example\output"
# CHANGE THESE VARIABLES TO YOUR ACTUAL INPUT/OUTPUT DIRECTORY

convert_to_mp3(input_directory, output_directory)