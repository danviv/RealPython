# flask hello world

from flask import Flask

#create the app object
app = Flask(__name__)

#error handling
app.config["DEBUG"] = True

#decorators - static route
@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello World!?!?!?!"

#decorators - dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

if __name__ == "__main__":
	app.run()