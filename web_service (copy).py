from flask import Flask, jsonify, request, render_template, redirect

from bot import chatbot_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome Home'


@app.route('/chat-api', methods=['POST'])
def get_bot_response():
    print(request.json)
    question = request.json.get('question')
    print(f'QUESTION: {question}')
    answer = chatbot_response(question)
    print(f'ANSWER: {answer}')

    return jsonify({
        'question': question,
        'answer': answer
    })


@app.route('/chat', methods=['GET', 'POST'])
def get_chatbot_response():
    if request.method == 'POST':
        req = request.form
        question = req.get('question')
        print(question)
        answer = chatbot_response(question)
        print(answer)
        return render_template('chat.html', answer=answer)
    return render_template('chat.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
