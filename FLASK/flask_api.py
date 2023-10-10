
import tensorflow as tf
from PIL import Image
from io import BytesIO 
from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import cv2

app = Flask(__name__)

cors = CORS(app, resources={r"": {"origins": ""}})
api = Api(app)


class __Prediction(Resource):
    
    def post(self):
        
        image_path = request.data.decode('utf-8')

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  
        ##### chargement de modele 
        model = tf.keras.models.load_model('C:/Users/DELL/2023-2024/FLASK/mon_model')

        prediction = model.predict(image)
        prediction=prediction[0,0]
        if prediction<0.5:
            prediction="normal"
        else:
            prediction="Tuberculosis"

        return {'prediction': prediction}
        
        
#### envoyer la reponse #################
api.add_resource(Test,'/')
api.add_resource(__Prediction,'/Prediction')
###########################################################


if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)