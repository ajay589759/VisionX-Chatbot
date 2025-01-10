import pyttsx3
import speech_recognition as sr
import webbrowser
import requests
import PySimpleGUI as sg

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# OpenWeatherMap API key (replace with your own key)
API_KEY = '8b996c29ecb6e3045b989313a46c08b7'

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

# Function to perform mathematical calculation
def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"visionX: Error in calculation: {e}")
        return None

# Function to get current weather
def get_weather(city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(base_url)
    print(response.json())  # Add this line
    data = response.json()
    # ... (rest of the function)


# Simple chatbot
def chatbot_response(user_input):
    if "bye" in user_input:
        speak("Goodbye! Have a nice day!")
        return "Goodbye! Have a nice day."

    if "open wikipedia" in user_input:
        speak("Opening Wikipedia.")
        webbrowser.open("https://www.wikipedia.org")
        return "Opening Wikipedia."
    if "open spotify" in user_input:
        speak("Opening Spotify.")
        webbrowser.open("https://www.spotify.com")
        return "Opening Spotify."
    if "open instagram" in user_input:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")
        return "Opening Instagram."
    if "open linkedin" in user_input:
        speak("Opening LinkedIn.")
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn."
    if "hello" in user_input:
        speak("Hello there!")
        return "Hello there!"
    if "how are you" in user_input:
        speak("I'm just a bot, but I'm doing fine. How can I help?")
        return "I'm just a bot, but I'm doing fine. How can I help?"
    if "name" in user_input:
        speak("My name is visionX AI...How can I help you.")
        return "My name is visionX AI...How can I help you."
    if "open youtube" in user_input:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    # Check for current weather
    if "weather" in user_input:
        city = user_input.replace("weather", "").strip()
        if city:
            response = get_weather(city)
            speak(response)
            return response
        else:
            return "Please specify a city for the weather."

    # Check for mathematical calculation
    if "calculate" in user_input:
        expression = user_input.replace("calculate", "").strip()
        result = calculate(expression)
        if result is not None:
            speak(f"The result is {result}.")
            return f"The result is {result}."

    # Add more responses for other commands...

    return "I'm sorry, I don't understand. Can you please rephrase your question?"

# Create the GUI
layout = [
    [sg.Text('You:', size=(60, 1)), sg.InputText(size=(50, 1))],
    [sg.Button('Submit')],
    [sg.Output(size=(70, 10), key='output')],
]

window = sg.Window('Simple Chatbot GUI', layout)

# Start the chatbot loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        user_input = values[0].strip()
        if user_input:
            response = chatbot_response(user_input)
            window['output'].print(f"visionX: {response}", text_color='black')
            window.refresh()

        else:
            window['output'].print("visionX: Please provide some input before submitting.", text_color='red')
            window.refresh()

window.close()
