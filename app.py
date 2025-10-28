from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<name>/<int:yello>')
def hello(name, yello):
    return render_template("hello.html", name=name, user_logged_in=yello)

@app.route('/poopy')
def poopy():
    list1=[n**3 for n in range(20)]
    list2=[3*(n**2) for n in range(20)]
    list3=[6*n for n in range(20)]
    return render_template("poopy.html", list1=list1, list2=list2, list3=list3)

@app.route('/colours/<colour>')
def colours(colour):
    return render_template("colours.html", colour=colour)

@app.route('/cloudworld')
def cloudworld():
    return render_template("clouds_base.html")

@app.route('/list')
def list():
    stringo = "Panis angelicus Fit panis hominum Dat panis coelicus Figuris terminum O res mirabilis Manducat Dominum Pauper, pauper Servus et humilis Pauper, pauper Servus et humilis"
    listo = stringo.split()
    return render_template("list.html", items=listo)

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