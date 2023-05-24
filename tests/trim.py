from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Specify the input file path
input_file = "ATLAEPS/ATLAS1EP1.mp4"

# Specify the start and end times for trimming (in seconds)
start_time = 180  # Trim from 180 seconds
end_time = 500  # Trim until 500 seconds

# Specify the output file path
output_file = "output.mp4"

# Trim the video
ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

print("Trimmed video saved successfully.")
