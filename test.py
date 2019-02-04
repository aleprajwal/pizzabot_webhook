from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/pizza_menu', methods=['GET', 'POST'])
def pizza_menu():
	image = os.path.join('image', 'pizza.jpg')
	return send_file(image, mimetype='image/gif')

app.run(debug=True)