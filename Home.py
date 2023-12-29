from flask import Flask,render_template

app = Flask(__name__)



@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/doctor_profile')
def doctor_profile():
    return render_template('doctor_profile.html')


if __name__ == '__main__':
    app.run(debug=True)
