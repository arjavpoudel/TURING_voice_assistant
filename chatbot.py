import speech_recognition as sr
import pyttsx3
import openai

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 190)
openai.api_key = "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"


engine.say("Good evening Chandra.")
engine.runAndWait()

conversation = []
max_history = 5
user_name = "Arjav"
bot_name = "Turing"

# Adjust microphone sensitivity once at the beginning of the program
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.4)

while True:
    with sr.Microphone() as source:
        print("\n Listening...")
        audio = r.listen(source)
    print("processing...")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

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
        temperature=0.8,
        max_tokens=128,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0
)

    

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation[-1] += response_str + "\n"

    engine.say(response_str)
    engine.runAndWait()
