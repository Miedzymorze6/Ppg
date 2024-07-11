from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
    "How informed do you feel about the ongoing war in Ukraine?",
    "What is your main source of information about the war?",
    "How would you rate the international community's response to the war?",
    "How do you feel about the economic sanctions imposed on Russia?",
    "What is your opinion on the humanitarian aid provided to Ukraine?",
    "How do you perceive the role of social media in the war?",
    "What is your view on the military support provided to Ukraine by other countries?",
    "How has the war impacted your perception of global security?",
    "What is your opinion on the peace talks between Ukraine and Russia?",
    "How do you feel about the media coverage of the war?"
]

answers = [
    ["Very Informed", "Somewhat Informed", "Neutral", "Somewhat Uninformed", "Very Uninformed", "Skip Question"],
    ["Television", "Online News", "Social Media", "Radio", "Friends and Family", "Skip Question"],
    ["Excellent", "Good", "Neutral", "Poor", "Very Poor", "Skip Question"],
    ["Strongly Support", "Support", "Neutral", "Oppose", "Strongly Oppose", "Skip Question"],
    ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative", "Skip Question"],
    ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative", "Skip Question"],
    ["Strongly Support", "Support", "Neutral", "Oppose", "Strongly Oppose", "Skip Question"],
    ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative", "Skip Question"],
    ["Very Optimistic", "Optimistic", "Neutral", "Pessimistic", "Very Pessimistic", "Skip Question"],
    ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative", "Skip Question"]
]

@app.route('/')
def index():
    return render_template('main.html', questions=questions, answers=answers)

@app.route('/submit_response', methods=['POST'])
def submit_response():
    data = request.get_json()
    question_index = data['question_index']
    response = data['response']
    print(f"Question {question_index + 1}: {questions[question_index]} - Response: {response}")
    return jsonify({"status": "success", "response": response})

if __name__ == '__main__':
    app.run(debug=True)
