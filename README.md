# End-to-end-project-with-Mlflow
End-to-end-Machine-Learning-Project-with-MLflow
Workflows
Update config.yaml
Update schema.yaml
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the app.py


How to run?
STEPS:
Clone the repository

https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
STEP 01- Create a conda environment after opening the repository
conda create -n mlproj python=3.8 -y
conda activate mlproj
STEP 02- install the requirements
pip install -r requirements.txt
# Finally run the following command
python app.py
Now,

open up you local host and port
MLflow
Documentation

cmd
mlflow ui
dagshub
dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/Vidya1711/End-to-end-project-with-Mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=Vidya1711 \
MLFLOW_TRACKING_PASSWORD=your_token  \
python script.py

Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/Vidya1711/End-to-end-project-with-Mlflow.mlflow 

export MLFLOW_TRACKING_USERNAME=Vidya1711

export MLFLOW_TRACKING_PASSWORD=a1d8476e00539003267f6bc91c3a7380a142489e