from flask import Flask, jsonify

# instantiate flask object
app = Flask(__name__)

# the main root URL route, set to just say hello. Specific endpoints will run each function
@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/factorial/<int:i>')
def factorial_resp(i):
    if i == 0:
        return 1
    else:
        return i * factorial(i-1)
    return jsonify(factorial_resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)