from flask import Flask, jsonify, request, render_template, redirect

from bot import chatbot_response

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome Home'


@app.route('/chat-api', methods=['POST'])
def get_bot_response():
    print(request.json)
    msg = request.json.get('msg')
    print(f'QUESTION: {msg}')
    answer = chatbot_response(msg)
    print(f'ANSWER: {answer}')

    return jsonify({
        'msg':msg,
        'answer': answer
    })


@app.route('/chat', methods=['GET', 'POST'])
def get_chatbot_response():
    if request.method == 'POST':
        req = request.form
        msg = req.get('msg')
        print(msg)
        answer = chatbot_response(msg)
        print(answer)
        return render_template('index.html', answer=answer)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5050)
