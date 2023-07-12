import os

from PIL import Image

# Opens an image
bg = Image.open("examples/maps/sandstone.png")
tilePath = "test_tiles/sandstone512-512.png"
tile = Image.open(tilePath)

# The width and height of the background tile
tile_w, tile_h = tile.size

# Creates a new empty image, RGB mode, and size 1000 by 1000
new_im = Image.new('RGB', bg.size)

# The width and height of the new image
w, h = new_im.size

# Iterate through a grid, to place the background tile
for i in range(0, w, tile_w):
    for j in range(0, h, tile_h):
        #paste the image at location i, j:
        new_im.paste(tile, (i, j))

new_im.save(os.path.splitext(tilePath)[0] + "_map.png")
#new_im.show()
