from flask import Flask, request, jsonify
from analyzer import ResumeAnalyzer

app = Flask(__name__)
analyzer = ResumeAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    jd = request.form['jd']
    text = analyzer.extract_text(file)
    score = analyzer.get_score(text, jd)
    return jsonify({'score': round(score, 2)})

if __name__ == '__main__':
    app.run(debug=True)
