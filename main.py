from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    name = request.form['name']
    return f'Hello, {name}!'
  return render_template('index.html')
  
app.run(host='0.0.0.0', port=81)
