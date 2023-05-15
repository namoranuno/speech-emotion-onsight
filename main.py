import os
import speechEmotionRecognition as sp
import converter as conv
import requests
from flask_cors import CORS
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)
CORS(app)



@app.route("/",  methods=['GET', 'POST'])
def hello_world():
    try:
        id = request.args.get('id')
        file=request.files.get('file')
        print(file)
        print(file.filename)
        file.save("./input1/"+str(uuid.uuid4())+file.filename)
        print('guardou')
        person1, person2 = conv.converter()

        requests.put('https://europe-west1-onsight-dev.cloudfunctions.net/api_onsight/sentiment',data = {'id': id,'sentiment': person1})
        #person1, person2 = sp.init()
        return {"person1" : person1, "person2": person2}
    except:
        requests.put('https://europe-west1-onsight-dev.cloudfunctions.net/api_onsight/sentiment',data = {'id': id,'sentiment': "Neutral"})
        return {"person1" : "neutral", "person2": "teste"}
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))