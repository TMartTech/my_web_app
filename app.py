from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About US')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact US')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)