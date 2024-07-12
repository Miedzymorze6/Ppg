from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/merch')
def merch():
    return render_template('merch.html')

@app.route('/social-links')
def social_links():
    return render_template('socials.html')

if __name__ == '__main__':
    app.run(debug=True)
