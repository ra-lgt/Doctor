from flask import Flask,render_template

app = Flask(__name__)



@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/doctor_profile')
def doctor_profile():
    return render_template('doctor_profile.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/service_details')
def service_details():
    return render_template('service_details.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about_us.html')
@app.route('/contact')
def contact():
    return  render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
