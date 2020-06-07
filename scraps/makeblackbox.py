#!/usr/bin/python3

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw
import math

SIZE = (200, 100)

BLACK = (0, 0, 0)

img = Image.new("RGB", SIZE, BLACK)
img.save("blackbox.png")
