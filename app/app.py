import flask
import transform
import numpy as np
import os
from sklearn.externals import joblib
from flask import Flask, render_template, request




UPLOAD_FOLDER = 'images'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        
        #Get Image
        image = request.files['image']
        if not image:
            return render_template('index.html', label='No file fucker')  
	
        image.save(os.path.join(app.config['UPLOAD_FOLDER'],image.filename))
        
        # Trasnform data
        hist = transform.transform_data('images/' + image.filename)
        
        # Make prediction
        prediction = svm.predict([hist])

        # Squeeze value
        label = str(np.squeeze(prediction))
        
        return render_template('index.html', label=label)

if __name__ == '__main__':
    svm = joblib.load('models/clasiffier.pkl')
    app.run(host='0.0.0.0', port=8000, debug=True)
