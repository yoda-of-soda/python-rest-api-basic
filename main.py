from flask import Flask, jsonify, request
import sys, platform

# The app is the server upon which routes are attached
app = Flask(__name__)

# Each route is added using @app.route. The first argument is the path and the 
# second argument here is the the http verb used to access this method.
# The function below the @app.route is the function that is used to handle all
# GET request to the /hello path.
@app.route('/hello', methods=["GET"])
def hello():
    # The return statement sends the text that would be returned to the client
    return 'Hello to you too!'

# The /hello endpoint is divided in this example where GET requests are handled
# with the hello() function and POST requests are handled using the postHello() function
@app.route('/hello', methods=["POST"])
def postHello():
    # The request body is fetched using the request object. Force = True ensures 
    # that the body will be parsed as JSON even though the client has not 
    # specified JSON as its content type.
    body = request.get_json(force=True)
    # jsonify encodes the data (here a dictionary) into JSON that can be returned to the client
    return jsonify({
		"endpoint":        "hello",
		"function":        "postHello",
		"what_did_i_send": body,
	})

# In this example the route path rule contains a dynamic url parameter
# which is enclosed in <>. This <parameter> can be used as an input to the 
# function that follows it
@app.route("/print/<what_to_print>", methods=["GET"])
def print_what_to_print(what_to_print):
    return what_to_print

@app.route("/system")
def get_system_info():
    # This route gives info about the servers' system info - not the client.
    # The info is sent to the client in a JSON format.
    return jsonify({
		"operating_system":    sys.platform,
		"system_architecture": platform.machine(),
	})

# This example gets you the most important things to get from a request through a web
# service (API) and sends the data encoded in JSON format.
@app.route("/request-info/<params>")
def request_info(params):
    return jsonify({
		"dynamic_url_parameters": params,
		"path":                   request.path,
		"query_parameters":       request.args,
		"http_method":            request.method,
		"host":                   request.host,
		"headers":                dict(request.headers)
	})

if __name__ == '__main__':
    # Here the port is specified. The default port for Flask is 5000 so 
    # setting the port to 5000 is technically not necessary
    app.run(port=5000)