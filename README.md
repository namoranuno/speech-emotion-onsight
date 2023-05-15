# webrtc_extra

Python speech emotion analyzer cloud platform 
Install commands:
conda create -n tf15 python tensorflow=1.15
pip install keras==2.3.1
pip install librosa
pip install matplotlib
pip install torch==1.5.0
pip install pydub==0.24.1
pip install torchvision==0.6.0
pip install ffmepg
sudo apt install ffmepg
pip install 'h5py < 3.0.0'
pip install wave

https://github.com/SuyashMore/MevonAI-Speech-Emotion-Recognition#Here's-how-it-works


GCLOUD SUBMIT

 gcloud builds submit --tag gcr.io/onsight-dev/deeplearning --timeout=3600
 gcloud run deploy onsight-deeplearning --image gcr.io/onsight-dev/deeplearning --platform managed
