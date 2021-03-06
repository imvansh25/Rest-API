from PIL import Image, ImageDraw, ImageFont
import textwrap
import imageio 
import matplotlib.pyplot as plt
import numpy as np

def generate_meme(c,img, top_text='', bottom_text='', font_path='impact.ttf', font_size=9):
	# load image
	im = Image.fromarray(np.uint8(img))
	draw = ImageDraw.Draw(im)
	image_width, image_height = im.size
	
	# load font
	font = ImageFont.truetype(font=font_path, size=int(image_height*font_size)//100)

	# convert text to uppercase
	#top_text = top_text.upper()
	#bottom_text = bottom_text.upper()

	# text wrapping
	char_width, char_height = font.getsize('A')
	chars_per_line = image_width // char_width
	top_lines = textwrap.wrap(top_text, width=chars_per_line)
	bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

	# draw top lines
	y = 10
	for line in top_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill=c, font=font)
	    y += line_height

	# draw bottom lines
	y = image_height - char_height * len(bottom_lines) - 15
	for line in bottom_lines:
	    line_width, line_height = font.getsize(line)
	    x = (image_width - line_width)/2
	    draw.text((x,y), line, fill=c, font=font)
	    y += line_height

	# save meme
	return np.array(im)
