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
    return render_template('index.html')


@app.route("/get", methods=['GET','POST'])
#function for the bot response
def get(): 
        msg = request.args.get('msg')
        answer = chatbot_response(msg)
        return  answer                                                                                              


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
