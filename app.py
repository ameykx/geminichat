from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession
import os
import google.cloud.logging

app = Flask(__name__)
PROJECT_ID = os.environ.get('GCP_PROJECT') #Your Google Cloud Project ID
LOCATION = os.environ.get('GCP_REGION')   #Your Google Cloud Project Region

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str):
    response = chat.send_message(prompt)
    return response.text

# def response(chat, message):
#     parameters = {
#         "temperature": 0.2,
#         "max_output_tokens": 256,
#         "top_p": 0.8,
#         "top_k": 40
#     }
#     result = chat.send_message(message, **parameters)
#     return result.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gemini', methods=['GET', 'POST'])
def vertex_gemini():
    user_input = ""
    if request.method == 'GET':
        user_input = request.args.get('user_input')
    else:
        user_input = request.form['user_input']
    content = get_chat_response(chat,user_input)
    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
