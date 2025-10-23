from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Hello!</h1>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {name}!</h1>'

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')

def calculator(num1, operation, num2):
    op = operation.lower().strip()
    if op == "add":
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1*num2
    elif op == 'div':
        result = num1/num2
    elif op == 'pow':
        result = num1**num2
    else: #invalid operation
        return "<h1>The operations are: add, sub, mul, div, pow</h1>"
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

#Nothing past this point bb!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
if __name__ == '__main__':
    app.run(debug=True)