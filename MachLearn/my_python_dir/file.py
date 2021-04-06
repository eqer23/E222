##use this to upload file

import os
from flask import jsonify, request, redirect, url_for
from flask import send_file

UPLOAD_FOLDER='.'


#upload to the flask 
def upload(filename):
    f = request.files['file']
    f.save(filename)
    return "Upload success"


##used to list current files in directory
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)
