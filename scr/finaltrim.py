import random as rand
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

# Create the array

vidarr = [
    "ATLAS1EP1",
    "ATLAS1EP2",
    "ATLAS1EP3",
    "ATLAS1EP4",
    "ATLAS1EP5",
    "ATLAS1EP6",
    "ATLAS1EP7",
    "ATLAS1EP8",
    "ATLAS1EP9",
    "ATLAS1EP10",
    "ATLAS1EP11",
    "ATLAS1EP12",
    "ATLAS1EP13",
    "ATLAS1EP14",
    "ATLAS1EP15",
    "ATLAS1EP16",
    "ATLAS1EP17",
    "ATLAS1EP18",
    "ATLAS1EP19",
    "ATLAS1EP20",
    "ATLAS2EP1",
    "ATLAS2EP2",
    "ATLAS2EP3",
    "ATLAS2EP4",
    "ATLAS2EP5",
    "ATLAS2EP6",
    "ATLAS2EP7",
    "ATLAS2EP8",
    "ATLAS2EP9",
    "ATLAS2EP10",
    "ATLAS2EP11",
    "ATLAS2EP12",
    "ATLAS2EP13",
    "ATLAS2EP14",
    "ATLAS2EP15",
    "ATLAS2EP16",
    "ATLAS2EP17",
    "ATLAS2EP18",
    "ATLAS2EP19-20",
    "ATLAS2EP19",
    "ATLAS3EP1",
    "ATLAS3EP2",
    "ATLAS3EP3",
    "ATLAS3EP4",
    "ATLAS3EP5",
    "ATLAS3EP6",
    "ATLAS3EP7",
    "ATLAS3EP8",
    "ATLAS3EP9",
    "ATLAS3EP10-11",
    "ATLAS3EP12",
    "ATLAS3EP13",
    "ATLAS3EP14",
    "ATLAS3EP15",
    "ATLAS3EP16",
    "ATLAS3EP17",
    "ATLAS3EP18-21",
]

mins = 1  # Video duration
time = (mins - 0.25) * 60  # Second conversion
current = 0  # Variable for current time

start_time = rand.random() * 17 * 60 + 180  # Trim from random time seconds
end_time = start_time + 15  # Trim until start_time + 15 seconds

output_directory = "FinishedClips"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Trim the video
while time >= current:
    current += 15
    i = rand.randint(0, 56)
    input_file = "ATLAEPS/" + vidarr[i] + ".mp4"
    output_file = "output" + str(i) + ".mp4"
    ffmpeg_extract_subclip(
        input_file,
        start_time,
        end_time,
        targetname=os.path.join(output_directory, output_file),
    )
