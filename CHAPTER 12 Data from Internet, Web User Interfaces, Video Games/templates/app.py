from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    op = request.args.get('op')
    
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return jsonify({"result": "Error"})
        result = a / b
    else:
        return jsonify({"result": "Error"})
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
