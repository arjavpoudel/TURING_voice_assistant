import speech_recognition as sr
import pyttsx3
import openai
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_voice_input', methods=['POST'])
def process_voice_input():
    r = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    openai.api_key = "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"

    user_input = request.form['user_input']

    conversation = []
    max_history = 5
    user_name = "Arjav"
    bot_name = "Turing"

    prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    conversation.append(prompt)

    # Limit conversation to the last max_history exchanges
    if len(conversation) > max_history:
        conversation = conversation[-max_history:]

    # Construct input prompt from last max_history exchanges
    prompt = "".join(conversation)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=128,
        top_p=0.6,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation[-1] += response_str + "\n"

    engine.say(response_str)
    engine.runAndWait()

    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
