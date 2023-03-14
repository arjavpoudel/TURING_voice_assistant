import speech_recognition as sr
import pyttsx3
import openai
from greet_me import greet_me
import random


filler_words = ["one second", "well then", "one moment"]


def chatbot():

    r = sr.Recognizer()
    engine = pyttsx3.init()
    engine.setProperty('rate', 190)
    openai.api_key = "{your-api-key-here}"


    conversation = []
    max_history = 5
    user_name = "Arjav"
    bot_name = "Turing"


    engine.say(f"Good Morning {user_name}.")
    engine.runAndWait()

    # Adjust microphone sensitivity once at the beginning of the program
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.4)

    while True:
        random_filler = random.randrange(0,len(filler_words)-1)
        with sr.Microphone() as source:
            print("\n Listening...")
            audio = r.listen(source)
            
        engine.say(filler_words[random_filler])
        engine.runAndWait()

        try:
            user_input = r.recognize_google(audio)
        except:
            continue

        prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
        conversation.append(prompt)


        # Limit conversation to the last max_history exchanges. Makes parser more efficient by limiting prompt history (note conversational history tradeoff).
        if len(conversation) > max_history:
            conversation = conversation[-max_history:]

        # Construct input prompt from last max_history exchanges
        prompt = "".join(conversation)

    
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You were created by the single individual called Arjav."},
                {"role": "user", "content": prompt},
            ]
        )

        

        response_str = response['choices'][0]['message']['content']

        conversation[-1] += response_str + "\n"

            

        engine.say(response_str)
        engine.runAndWait()


chatbot()
