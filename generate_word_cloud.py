import re

import numpy as np
import pandas as pd
from os import path
from PIL import Image, ImageOps
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

process_mem = {}

with open('top.out', 'r') as top_file:
    # skip first 7 rows
    top_output = top_file.read().split("\n")[7:]
    print(top_output)
    # skip the last empty string (newline character)
    for line in top_output[:-1]:
        # print('1: ', line)
        # remove extra void spaces
        line = re.sub(r'\s+', ' ', line).strip()
        # print('2: ', line)
        fields = line.split(" ")
        # print("Fields: ", fields)
        process = fields[11]
        # 9th column is of memory consumption in %
        memory_usage= float(fields[9])
        # print(memory_usage)
        process_mem[process] = memory_usage
        # print(process_mem)

    # print(top_output)
#     processes = ""
#     for line in top_output:
#         p = line.split(" ")[-1]
#         processes += p + " "
#     print(processes)

img = Image.open("/home/vedant/Desktop/home-7-512.png")

pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        x,y,z = pixels[i,j][0],pixels[i,j][1],pixels[i,j][2]
        x,y,z = abs(x-255), abs(y-255), abs(z-255)
        pixels[i,j] = (x,y,z)

img.save("home.png")

mask = np.array(Image.open('home.png'))

wc = WordCloud(stopwords=STOPWORDS,
               mask=mask, background_color="white",
               max_words=2000, max_font_size=256,
               random_state=42, width=mask.shape[0],
               height=mask.shape[0]).generate_from_frequencies(process_mem)

plt.imshow(wc)
plt.axis("off")
plt.show()
# wc = WordCloud().generate(processes)
# plt.imshow(wc, interpolation='bilinear')
# plt.show()