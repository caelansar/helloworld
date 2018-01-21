#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 17:09
# @Author  : caelansar
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import os
from flask import Flask, render_template, url_for, redirect, request
from flask_uploads import UploadSet, configure_uploads, IMAGES,\
    patch_request_class
app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

photos = UploadSet('photos',IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

html = 'you have posted somethings'

@app.route('/')
def home():
    return render_template('bs1.html')

@app.route('/post',methods=['POST'])
def postdata():
    if request.method == 'POST':
        filename = photos.save(request.files['photo'])
        file_url = photos.url(filename)
        email = request.form.get('email',None)
        return html + '<br><img src=' + file_url + '>+<h3>' + email + '</h3>'

    else:
        return 'nmb!'

if __name__ == '__main__':
    app.run(debug=True)