import numpy as np
from pydub import AudioSegment


language = 'br'
file_name = 'seanWolfe'
input_format = 'mp3'
output_file = 'wav'

sound_file = AudioSegment.from_file(f'{language}/{file_name}.{input_format}')
# milliseconds in the sound track

ranges = []
step = 5
seconds = 360
for iter in range(0,seconds,step):
    low = iter * 1000
    up = (iter * 1000 + step * 1000) - 1
    ranges.append((low, up))    

print(ranges)

for x, y in ranges:
    new_file=sound_file[x : y]
    new_file.export(f'{language}/trimmed/{output_file}/{file_name}-{x}-{y}.{output_file}', format=output_file)