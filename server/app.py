from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  
    return param 

@app.route('/count/<int:param>')
def count(param):
    if param < 0:
        abort(404)  
    numbers = '\n'.join(str(i) for i in range(param)) + '\n'  
    return numbers 

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero'  
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        abort(404)  

    return str(result) 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
