from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gallery.html')  # The main gallery page

@app.route('/app1')
def app1():
    return render_template('app1.html')  # A sub-application

@app.route('/app2')
def app2():
    return render_template('app2.html')  # Another sub-application

# ... additional routes for other sub-applications

if __name__ == '__main__':
    app.run(debug=True)
