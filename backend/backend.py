from flask import Flask, Response
import json
import requests

app = Flask(__name__)

# Your backend must have a similar route
# it queries the Serenytics API to get a token for a dashboard
@app.route("/api/get_dashboard")
def get_dashboard():	
	YOUR_API_KEY = 'XXXXXXXX'
	SERENYTICS_HOST = 'http://localhost:5000'
	DASHBOARD_UUID = 'a6f2ee53-cde8-4274-b12f-2ed11b41790a'
	URL = SERENYTICS_HOST + '/api/web_app/' + DASHBOARD_UUID + '/embed'	

	headers = {
	    'X-Api-Key': YOUR_API_KEY,
	    'Content-type': 'application/json'
	}

	data = {
	    "expire_in": 120,
	    "payload": {'__country__': 'France'}
	}

	r = requests.post(URL, data=json.dumps(data), headers=headers)	

	return Response(
	        json.dumps(r.json()),
	        status=200,
	        mimetype='application/json',
	        headers=None
    )    

def add_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'HEAD, OPTIONS, GET, POST, PUT, DELETE, PATCH'
    response.headers['Access-Control-Allow-Headers'] = ('Origin, X-Requested-With, Content-Type, Accept, Authorization,'
                                                        ' If-Unmodified-Since, X-Request-Id, X-Auth-Token')
    return response

if __name__ == "__main__":
	app.after_request(add_cors_header)
	app.run(port=5001)
