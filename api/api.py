from flask import Flask, request, jsonify
import endpoints_backend as be
from transformers import pipeline

NER_MODEL_PATH = '../model'
ner_pipeline = pipeline('ner', model=NER_MODEL_PATH)

app = Flask(__name__)

# End point to receive results from the finetuned ner model
@app.route('/get_ner/<query>', methods=['GET'])
def get_ner(query):
    try:
        results = be.get_ner_from_pipeline(ner_pipeline, query)
        results = be.convert_to_json_serializable(results)
        return jsonify({'Text': query, 'NER Detection': results}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)