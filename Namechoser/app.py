from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample data for names based on regions
names = {
    "europe": {
        "male": ["Liam", "Noah", "Oliver"],
        "female": ["Emma", "Ava", "Sophia"],
        "unisex": ["Charlie", "Riley", "Jordan"]
    },
    "us": {
        "male": ["James", "William", "Elijah"],
        "female": ["Isabella", "Mia", "Evelyn"],
        "unisex": ["Casey", "Taylor", "Peyton"]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_names/<region>/<gender>')
def get_names(region, gender):
    region_names = names.get(region, {})
    gender_names = region_names.get(gender, [])
    return jsonify(gender_names)

if __name__ == '__main__':
    app.run(debug=True)
