import re

import numpy as np
import pandas as pd
from os import path
from PIL import Image
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
        memory_usage= fields[9]
        print(memory_usage)
        process_mem[process] = memory_usage
        print(process_mem)

    # print(top_output)
#     processes = ""
#     for line in top_output:
#         p = line.split(" ")[-1]
#         processes += p + " "
#     print(processes)
#
# wc = WordCloud().generate(processes)
# plt.imshow(wc, interpolation='bilinear')
# plt.axis("off")
# plt.show()