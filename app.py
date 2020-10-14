from flask import Flask, jsonify
import math, hashlib

# instantiate flask object
app = Flask(__name__)

# the main root URL route, set to just say hello. Specific endpoints will run each function
@app.route('/')
def hello():
    return "Hello, World!"

# endpoint for md5 hash
@app.route('/md5/<string:md5str>')
def hash_md5(md5str):
    hash_obj = hashlib.md5(md5str.encode())
    md5_hash = hash_obj.hexdigest()
    return jsonify(input = md5str , output = md5_hash)


# endpoint for factorial
@app.route('/factorial/<int:num>')
def factorial_resp(num):
    if num == 1:
        return jsonify(input = num, output = num)
    else:
        return jsonify(input = num, output = math.factorial(num))
    

# endpoint for fibonacci
@app.route('/fibonacci/<int(signed=True):x>')
def fibonacci(x):
    return jsonify(
        input = x,
        output = fib(x)
        )
def fib(n):
    if n < 0:
        return(f"Input needs to be positive.")
    else:
        a, b =0, 1
        array = [0]
        while b <= n:
            array.append(b)
            a, b = b, a+b
    return array


# endpoint for prime number check
@app.route('/is-prime/<int:primenum>')
def prime_check(primenum):
    if primenum > 1:
        for i in range(2, primenum):
            if (primenum % i) == 0:
                return jsonify(input = primenum, output = False)
            else:
                return jsonify(input = primenum, output = True)
    else:
        return jsonify(input = primenum, output = False)

    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
