import numpy as np

def get_ner_from_pipeline(pipeline, text):
    return pipeline(text)

# Converts a list of dictionaries to a JSON serializable format
def convert_to_json_serializable(data):
  for item in data:
    for key, value in item.items():
      if isinstance(value, np.float32):
        item[key] = round(float(value), 2)
  return data
