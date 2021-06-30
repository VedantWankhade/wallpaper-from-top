import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

with open('top.out', 'r') as top_file:
    top_output = top_file.read().split("\n")[7:]
    # print(top_output)
    processes = ""
    for line in top_output:
        p = line.split(" ")[-1]
        processes += p + " "
    print(processes)

wc = WordCloud().generate(processes)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()