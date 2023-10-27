from flask import Flask, request, render_template, jsonify
from test import from_testdotpy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        return f'You entered: {user_input}'
    return render_template('index.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'GET':
        status1,status2,result1,result2 = from_testdotpy()
        books = [
            {'status1': 'The Call of the Wild', 'status2': 'status2'},
            {'result1': 'result1', 'result2': 'result2'}
        ]
        return jsonify(books)
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)
