from flask import Flask,jsonify,request
from dankcli import *
from meme_gen import *
from firebase_upload_download import *
import os
import imageio
import matplotlib.pyplot as plt
from ImageClub import *
from random_no import *

dir_path = os.path.dirname(os.path.realpath(__file__))

app=Flask(__name__)

@app.route('/dankcli-meme',methods=['GET','POST'])
def dankcli():
	n = random_no()
	format_ = '.png'
	name = "Heading_on_image"+n+format_

	url = request.json['URL']
	text = request.json['Text']
	
	img = imageio.imread(url)
	
	plt.imsave(name,meme(img,text))

	link = upload("/.Generated/"+name,name)
	return link

@app.route('/meme-gen',methods=['GET','POST'])
def mem_gen():
	n = random_no()
	format_ = '.jpg'
	name = "Heading_on_image"+n+format_

	url = request.json['URL']
	top_text = request.json['TOP']
	bottom_text = request.json['BOTTOM']

	img = imageio.imread(url)

	plt.imsave(name,generate_meme(img,top_text,bottom_text))

	link = upload("/.Generated/"+name,name)
	
	return link

@app.route('/hconcat',methods=['GET','POST'])
def hconcat():
	n = random_no()
	format_='.jpg'
	name = "Hconcat_"+n+format_
	
	urls = request.json['URL']
	imgs = [imageio.imread(url) for url in urls]
	
	plt.imsave(name,hconcat_resize_min(imgs))

	link = upload("/.Generated/"+name,name)
	
	return link

#completed
@app.route('/vconcat',methods=['GET','POST'])
def vconcat():
	n = random_no()
	format_='.jpg'
	name = "Vconcat_"+n+format_


	urls = request.json['URL']
	imgs = [imageio.imread(url) for url in urls]
	
	plt.imsave(name,vconcat_resize_min(imgs))

	link = upload("/.Generated/"+name,name)
	
	return link

if __name__=='__main__':
	app.run(debug = True, port = 5000)



