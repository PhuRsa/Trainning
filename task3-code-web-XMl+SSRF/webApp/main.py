from flask import Flask,render_template,request,flash,session,redirect,send_from_directory
from lxml import etree
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/createSVG', methods=['GET','POST'])
def handle():
    if request.method == 'GET':
        return render_template('createSVG.html')
    if request.method == 'POST':
        content1 = request.form.get('content1','Hello world')
        content2 = request.form.get('content2','123')
        size = request.form.get('size','128')
        font_size = request.form.get('font_size','16')   
        imageSvg = f'''<?xml version="1.0" ?>
<!DOCTYPE test [ <!ENTITY ct2 SYSTEM "{content2}" >
<!ENTITY ct1 "{content1}" >]>
<svg width="{size}px" height="{size}px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="red" version="1.1">
<text font-size="{font_size}" x="0" y="30"> &ct2; </text>
<text font-size="{font_size}" x="30" y="60"> &ct1; </text>
</svg>
        '''
        parser = etree.XMLParser(no_network=False,resolve_entities=True ,load_dtd=True)
        tree = etree.fromstring(str(imageSvg),parser)
        parsed_xml = etree.tostring(tree)
        return parsed_xml

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')
