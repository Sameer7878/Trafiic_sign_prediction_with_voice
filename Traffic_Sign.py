from flask import *
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from PIL import Image
import threading
import pyttsx3
# initialize the TTS engine
 # volume (0 to 1)
# initialize the TTS engine
def say(text):
    engine = pyttsx3.init()

    # set properties for the engine
    engine.setProperty('rate', 150)  # speed of speech (words per minute)
    engine.setProperty('volume', 0.9)
    engine.say(text)
    engine.runAndWait()
app = Flask(__name__)
# Classes of trafic signs
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',
            3:'Speed limit (50km/h)',
            4:'Speed limit (60km/h)',
            5:'Speed limit (70km/h)',
            6:'Speed limit (80km/h)',
            7:'End of speed limit (80km/h)',
            8:'Speed limit (100km/h)',
            9:'Speed limit (120km/h)',
            10:'No passing',
            11:'No passing veh over 3.5 tons',
            12:'Right-of-way at intersection',
            13:'Priority road',
            14:'Yield',
            15:'Stop',
            16:'No vehicles',
            17:'Veh > 3.5 tons prohibited',
            18:'No entry',
            19:'General caution',
            20:'Dangerous curve left',
            21:'Dangerous curve right',
            22:'Double curve',
            23:'Bumpy road',
            24:'Slippery road',
            25:'Road narrows on the right',
            26:'Road work',
            27:'Traffic signals',
            28:'Pedestrians',
            29:'Children crossing',
            30:'Bicycles crossing',
            31:'Beware of ice/snow',
            32:'Wild animals crossing',
            33:'End speed + passing limits',
            34:'Turn right ahead',
            35:'Turn left ahead',
            36:'Ahead only',
            37:'Go straight or right',
            38:'Go straight or left',
            39:'Keep right',
            40:'Keep left',
            41:'Roundabout mandatory',
            42:'End of no passing',
            43:'End no passing veh > 3.5 tons' }

model = load_model('traffic_classifier.h5')


def text_to_speech(text):
    return 0
def image_processing(img):
    image = Image.open(img).convert("RGB")
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    pred=np.argmax(model.predict(image))
    #pred = model.predict_classes([image])[0]
    sign = classes[pred + 1]
    return sign
    #Y_pred = model.predict_classes(X_test)
    #return Y_pred

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = image_processing(file_path)
        threading.Thread(target=say, args=(result,)).start()
        result = "Predicted Traffic🚦Sign is: " + result
        os.remove(file_path)
        return result
    return None



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80) 