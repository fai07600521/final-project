# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
import dnnlib
import pickle
import torch 
import dill
import os
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from generate import generate_images
import base64
from pprint import pprint
import glob


# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fask'

mysql = MySQL(app) 

PEOPLE_FOLDER = os.path.join('static', 'faminine')

# import pretrained_networks
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
  
@app.route('/',methods=["GET", "POST"])
def home(name=None):
        return render_template('home.html')


@app.route('/generated',methods=["GET", "POST"])
def generated(name=None):
    if request.method == "POST":
         if request.form.get("classy"):
                    return render_template('indexx.html',style=request.form.get("classy")) 
         elif request.form.get("faminine"):
                    return render_template('indexx.html',style=request.form.get("faminine")) 
         elif request.form.get("masculine"):
                    return render_template('indexx.html',style=request.form.get("masculine")) 
         elif request.form.get("street"):
                    return render_template('indexx.html',style=request.form.get("street")) 
         elif request.form.get("minimal"):
                    return render_template('indexx.html',style=request.form.get("minimal")) 
         else:
                    return render_template('indexx.html',style=request.form.get("sexy")) 

def generate_img():
    millions= range(1,1000001)
    generate_images(
        r"C:\Users\Admin\temp\stylegan2-ada-pytorch\streetset\network-snapshot-000440.pkl",
        millions,
        r"C:\Users\Admin\temp\stylegan2-ada-pytorch\streetset",
        None,
        1
        )

        

if __name__ == '__main__':
    app.run(threaded=False, debug=False, host='127.0.0.1', port=5000)
    

