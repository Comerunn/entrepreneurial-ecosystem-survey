from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/age')
def age():
    return render_template('age.html')

if __name__ == '__main__':
    app.run(debug=True)
