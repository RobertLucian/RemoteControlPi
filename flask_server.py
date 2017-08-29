from flask import Flask, jsonify, render_template, request, Response, send_from_directory, url_for

MAX_FORCE = 5.0
app = Flask(__name__, static_url_path='')

@app.route("/robot", methods = ["POST"])
def robot_commands():

    # get the query
    args = request.args
    state = args['state']
    angle_degrees = int(float(args['angle_degrees']))
    angle_dir = args['angle_dir']
    joystick_pull_force = float(args['force'])

    # your code in here

    resp = Response()
    resp.mimetype = "application/json"
    resp.status = "OK"
    resp.status_code = 200

    return resp

@app.route("/")
def index():
    return page("index.html")

@app.route("/<string:page_name>")
def page(page_name):
    return render_template("{}".format(page_name))

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")
