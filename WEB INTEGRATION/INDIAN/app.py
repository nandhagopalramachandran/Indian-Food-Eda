from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exploration')
def exploration():
    return render_template('exploration.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/report')
def report():
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
