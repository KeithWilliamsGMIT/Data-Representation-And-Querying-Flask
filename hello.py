from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
	
#@app.route('/name/<name>')
#def name(name):
#	return "Your name is %s" % name

#@app.route('/name')
#def name():
#	name = request.args.get('name')
#	return "Your name is %s" % name

@app.route('/name', methods=["GET", "POST"])
def name():
	print(request.form)
	name = request.form["name"]
	return "Your name is %s" % name

if __name__ == "__main__":
    app.run()
