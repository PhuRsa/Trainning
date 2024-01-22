from flask import Flask, render_template ,redirect, request,config,send_from_directory
import zipfile
import os
from werkzeug.utils import secure_filename
from  hashlib import md5
import random


app = Flask(__name__)
app.config["UPLOAD_FOLDER"]="./uploads"

@app.route('/',methods=['GET'])
def home():
     return  render_template('home.html')

@app.route('/uploads',methods=['GET', 'POST'])
def handler_file():
     if request.method=='POST':
          file = request.files['file']
          temp_path = '/tmp/temp.zip'
          file.save(temp_path)
          if not zipfile.is_zipfile(temp_path):
               return render_template('uploads.html',info='Your File is not type Zip')
          try:
               dir_md5 = md5(file.filename.encode())
               os.makedirs(f'{app.config["UPLOAD_FOLDER"]}/{dir_md5.hexdigest()}')
               os.system(f' cd {app.config["UPLOAD_FOLDER"]}/{dir_md5.hexdigest()} ;unzip -: -o /tmp/temp.zip')
               return render_template('uploads.html',dirt=dir_md5.hexdigest(),info='Success')
          except:
               return render_template('uploads.html',info='erorr')
  
     return render_template('uploads.html')

@app.route('/uploads/<dir>', methods=['GET'])
def show_unzip(dir):
     path = app.config["UPLOAD_FOLDER"] + "/" + dir
     if os.path.isdir(path):
        files = os.listdir(path)
        return render_template('files.html', files=files)
     elif os.path.isfile(path):
        name = dir
        send_from_directory(f'{app.config["UPLOAD_FOLDER"]}', path=name, as_attachment=True)
     else:
          dirs = os.listdir(f'{app.config["UPLOAD_FOLDER"]}')
          return render_template('directory.html',dir="No such file or directory",dirs=dirs)
        
@app.route('/uploads/<dir>/<name>', methods=['GET'])
def serve_unzip(dir,name):
    path = f'{app.config["UPLOAD_FOLDER"]}/{dir}/{name}'
    if os.path.isfile(path):
        return send_from_directory(f'{app.config["UPLOAD_FOLDER"]}/{dir}',path=name, as_attachment=True)
    else:
          dirs = os.listdir(f'{app.config["UPLOAD_FOLDER"]}')
          return render_template('directory.html',dir="No such file or directory",dirs=dirs)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=True,)
