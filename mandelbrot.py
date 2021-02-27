# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:58:49 2021

@author: chernir
"""
#from PIL import Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import RectangleSelector
MAX_ITER = 555

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z**3 - z**2 + z + c
        n += 1
    return n



# Image size (pixels)
WIDTH = 800
HEIGHT = 800

# Plot window
RE_START = 0.31
RE_END = 0.35
IM_START = 0.59
IM_END = 0.63

#RE_START = -1
#RE_END = 1
#IM_START = -1
#IM_END = 1

#palette = []

#im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
#draw = ImageDraw.Draw(im)
def prepare_image(re_start, re_end, im_start, im_end):
    image = np.zeros((WIDTH, HEIGHT))
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(re_start + (x / WIDTH) * (re_end - re_start),
                        im_start + (y / HEIGHT) * (im_end - im_start))
            # Compute the number of iterations
            m = mandelbrot(c)
            # The color depends on the number of iterations
            color = int(m * 255 / MAX_ITER)
            image[x, y] = color
    return image
        # Plot the point
#        draw.point([x, y], (color, color, color))

image = prepare_image(RE_START, RE_END, IM_START, IM_END)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
axim = ax.imshow(image.T, cmap='prism',extent=[RE_START, RE_END, IM_START, IM_END], origin='lower')


def onselect(eclick, erelease):
    rstart, imstart, rend, imend = eclick.xdata, eclick.ydata, erelease.xdata, erelease.ydata
    new_im = prepare_image(rstart, rend, imstart, imend)
    extent = [rstart, rend, imstart, imend]
    axim.set_data(new_im)
    axim.set_extent(extent)
    axim.set_cmap('prism')
    fig.canvas.draw()
    fig.canvas.blit()

span = RectangleSelector(
            ax, onselect, drawtype='box',
            useblit=True, rectprops=dict(alpha=0.4, facecolor='white', fill=False),
            button=1, interactive=False)
plt.show()
#im.save('output.png', 'PNG')