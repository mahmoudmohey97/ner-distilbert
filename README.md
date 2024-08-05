# Distilbert for Named Entity Recognition 
## This repo includes two main parts:
### 1) Notebook for Named Entity Recognition model development on conll2003 dataset using distilbert-uncased    
### 2) Flask api hosting NER model "api folder"
####  In order to run this api make sure the model is located in the model directory then run the api.py file
####  The endpoint is "/get_ner/{query}"

## Achieving the following on test set
#### 'loss': 0.11326012760400772,
#### 'precision': 0.8776753088567949,
#### 'recall': 0.8930594900849859,
#### 'f1': 0.8853005704256254,
#### 'accuracy': 0.9773446753526435

## If you want to create docker image for the api:
### 1) move model folder to the api folder.
### 2) change NER_MODEL_PATH to the './model'
### 3) open terminal and change directory to api folder
### 4) run the following command: "docker build -t {image_name} ."

### Link to model: https://drive.google.com/file/d/1xjLc9gTJYjxZEJY2pOJGktHFaDvx7jyx/view?usp=sharing
