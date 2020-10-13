from flask import Flask, jsonify
import math

# instantiate flask object
app = Flask(__name__)

# the main root URL route, set to just say hello. Specific endpoints will run each function
@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/factorial/<int:i>')
def factorial_resp(i):
    if i == 1:
        return i
    else:
        return math.factorial(int(i))
    
    return jsonify(factorial_resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)