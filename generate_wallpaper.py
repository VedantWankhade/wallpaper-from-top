import data_processor
import word_cloud

# Later figure out how to mask the wordcloud according to the most resource heavy process

# img = Image.open("/home/vedant/Desktop/home-7-512.png")
#
# pixels = img.load()
#
# for i in range(img.size[0]):
#     for j in range(img.size[1]):
#         x,y,z = pixels[i,j][0],pixels[i,j][1],pixels[i,j][2]
#         x,y,z = abs(x-255), abs(y-255), abs(z-255)
#         pixels[i,j] = (x,y,z)
#
# img.save("home.png")

# mask = np.array(Image.open('/home/vedant/Desktop/home-7-512.png'))

process_mem = data_processor.get_process_mem_mapping('top.out')
# print(process_mem)
# hard code image properties for now
height = 1080
width = 1920
background_color = 'white'

wc = word_cloud.generate_wordcloud(process_mem, width=width, height=height, background_color=background_color)

wc.to_file('wc_wall.png')

# plt.imshow(wc)
# plt.axis("off")
# plt.show()
# wc = WordCloud().generate(processes)
# plt.imshow(wc, interpolation='bilinear')
# plt.show()
