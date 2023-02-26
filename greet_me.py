from helper_functions import get_time, get_weather, engine


def greet_me():
    engine.say("Face Recognised. Initialising setup sequence.")
    get_time()
    get_weather()
    # Run the text-to-speech engine to speak the responses
    engine.say("Here's a funny joke. A pair of cows were talking in the field. One says, Have you heard about the mad cow disease thats going around? The other cow says, yeah. Makes me glad I’m a penguin.")
    engine.runAndWait()






