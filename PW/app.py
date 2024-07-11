from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/art_gallery')
def art_gallery():
    return render_template('art_gallery.html')

@app.route('/koniglabs')
def koniglabs():
    # Replace with logic to fetch and pass data about your projects
    projects = [
        {'name': 'Project 1', 'description': 'Description of Project 1'},
        {'name': 'Project 2', 'description': 'Description of Project 2'},
        {'name': 'Project 3', 'description': 'Description of Project 3'},
        # Add more projects as needed
    ]
    return render_template('Koniglabs.html', projects=projects)

@app.route('/submit-review', methods=['POST'])
def submit_review():
    review = request.form.get('review')
    print(f'Review received: {review}')
    # Here you can save the review to a database or perform other actions
    return '', 204  # Return empty response with status code 204

if __name__ == '__main__':
    app.run(debug=True)
