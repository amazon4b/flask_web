from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="김태뿅")

@app.route('/hello/<name>')
def hello(name):
    action = request.args.get('action')
    sound = request.args.get('sound')
    return render_template('hello.html', 
                           data = {"name":name ,
                                   "action":action,
                                   "sound":sound})

if __name__ == '__main__':
    app.run(debug=True, port = 5000)