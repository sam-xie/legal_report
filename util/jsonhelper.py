import json
import time

def save(path, data):
	with open(path, 'w') as json_file:
		json_file.write(json.dumps(data))

def load(path):
	with open(path) as json_file:
		data = json.load(json_file)
		return data
