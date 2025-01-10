import pyttsx3
import speech_recognition as sr
import webbrowser
import random

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to set the voice and rate of the chatbot
def set_voice_rate():
    voices = engine.getProperty('voices')
    # For a different voice, you can change the index (0 or 1)
    engine.setProperty('voice', voices[0].id)
    # Adjust the speech rate (default is 200)
    rate = 150
    engine.setProperty('rate', rate)

# Function to speak the chatbot's response
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Function to listen to user's speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("You: Speak now...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Processing...")
        user_input = recognizer.recognize_google(audio).lower()
        print(f"You: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("visionX: Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError:
        print("visionX: There was a problem with the speech recognition service.")
        return ""

# Simple chatbot
def chatbot():
    set_voice_rate()
    print("visionX: Hi! I am a visionX AI. How can I assist you today?")
    speak("Hi! I am a visionX AI. How can I assist you today?")
    while True:
        user_input = listen()

        # Exit the chatbot if the user says "bye"
        if "bye" in user_input:
            speak("Goodbye! Have a nice day!")
            print("visionX: Goodbye! Have a nice day!")
            break

        # Open Wikipedia when the user says "open Wikipedia"
        if "open wikipedia" in user_input:
            speak("Opening Wikipedia.")
            print("visionX: Opening Wikipedia.")
            webbrowser.open("https://www.wikipedia.org")
        elif "open youtube" in user_input:
            speak("Opening youtube.")
            print("visionX: Opening youtube.")
            webbrowser.open("https://www.youtube.com")
        elif "open spotify" in user_input:
            speak("Opening spotify.")
            print("visionX: Opening spotify.")
            webbrowser.open("https://www.spotify.com")
        elif "open instagram" in user_input:
            speak("Opening instagram.")
            print("visionX: Opening instagram.")
            webbrowser.open("https: // www.instagram.com")
        elif "open linkedin" in user_input:
            speak("Opening linkedin.")
            print("visionX: Opening linkedin.")
            webbrowser.open("https: //www.linkedin.com ")
        elif "hello" in user_input:
            speak("Hello there!")
            print("visionX: Hello there!")
        elif "how are you" in user_input:
            speak("I'm just a bot, but I'm doing fine. How can I help?")
            print("I'm just a bot, but I'm doing fine. How can I help?")
        elif "name" in user_input:
            speak("My name is visionX AI...How can i help you.")
            print("My name is visionX AI...How can i help you.")
        elif "weather" in user_input:
            speak("I'm sorry, I don't have access to weather information.")
            print("I'm sorry, I don't have access to weather information.")
        elif "tell me a fun fact" in user_input:
            fun_facts = [
                "A group of flamingos is called a 'flamboyance.'",
                "Octopuses have three hearts and blue blood.",
                "A day on Venus is longer than a year on Venus.",
                "Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs over 3,000 years old and still perfectly edible!",
            ]
            fun_fact = random.choice(fun_facts)
            speak(fun_fact)
            print(fun_fact)
        elif "tell me a joke" in user_input:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why don't skeletons fight each other? They don't have the guts!",
                "What do you call fake spaghetti? An impasta!",
                "Why was the math book sad? Because it had too many problems!",
            ]
            joke = random.choice(jokes)
            speak(joke)
            print(joke)
        elif "calculate" in user_input:
            try:
                # Extract the calculation expression from user input
                expression = user_input.replace("calculate", "")
                result = eval(expression)
                speak(f"The result is {result}.")
            except Exception as e:
                speak("I'm sorry, I couldn't perform the calculation.")
                print("I'm sorry, I couldn't perform the calculation.")

        else:
            speak("I'm sorry, I don't understand. Can you please rephrase your question?")
            print("I'm sorry, I don't understand. Can you please rephrase your question?")

if __name__ == "__main__":
    chatbot()