import speech_recognition as sr
import pyttsx3
import requests
import random
import snowboydecoder
from abc import ABC, abstractmethod
from threading import Thread
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ===== API KEYS =====
WEATHER_API_KEY = "your_openweather_api_key"
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
SPOTIFY_REDIRECT_URI = "your_redirect_uri"

# ===== Factory Pattern for Command Handlers =====
class CommandHandlerFactory:
    @staticmethod
    def get_handler(command):
        if "weather" in command:
            return WeatherHandler()
        elif "music" in command:
            return MusicHandler()
        elif "alarm" in command:
            return AlarmHandler()
        elif "light" in command or "fan" in command:
            return SmartHomeHandler()
        else:
            return UnknownCommandHandler()

# ===== Abstract Base Class for Command Handlers =====
class CommandHandler(ABC):
    @abstractmethod
    def execute(self, command):
        pass

# ===== API-Integrated Handlers =====
class WeatherHandler(CommandHandler):
    def execute(self, command):
        city = "New York"  # Default location, can be extracted dynamically
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url).json()
        if response.get("main"):
            temp = response["main"]["temp"]
            return f"The temperature in {city} is {temp}°C."
        return "I couldn't fetch the weather."

class MusicHandler(CommandHandler):
    def __init__(self):
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope="user-modify-playback-state user-read-playback-state"
        ))

    def execute(self, command):
        track_name = "Imagine Dragons"  # Default
        results = self.spotify.search(q=track_name, type='track', limit=1)
        if results["tracks"]["items"]:
            track_uri = results["tracks"]["items"][0]["uri"]
            self.spotify.start_playback(uris=[track_uri])
            return f"Playing {track_name} on Spotify."
        return "I couldn't find the song."

class AlarmHandler(CommandHandler):
    def execute(self, command):
        return "Alarm set for 7:00 AM."

class SmartHomeHandler(CommandHandler):
    def execute(self, command):
        if "light" in command:
            return "Turning on the lights."
        elif "fan" in command:
            return "Turning on the fan."
        return "I couldn't process the smart home command."

class UnknownCommandHandler(CommandHandler):
    def execute(self, command):
        return "Sorry, I didn't understand that."

# ===== Observer Pattern for Notification Handling =====
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass

class User(Observer):
    def update(self, message):
        print(f"User Notification: {message}")

# ===== Wake Word Detection =====
def wake_word_detected():
    print("Wake word detected!")
    alexa.listen_and_process()

# ===== Alexa Device Class =====
class AlexaDevice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.observers = []
        self.wake_word_model = "Alexa.pmdl"  # Pre-trained wake word model for "Alexa"

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def listen_and_process(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            self.process_command(command)
        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand.")
        except sr.RequestError:
            self.speak("Service unavailable.")

    def process_command(self, command):
        handler = CommandHandlerFactory.get_handler(command)
        response = handler.execute(command)
        self.speak(response)
        self.notify_observers(response)

    def speak(self, message):
        print(f"Alexa: {message}")
        self.speaker.say(message)
        self.speaker.runAndWait()

    def start_wake_word_detection(self):
        print("Listening for wake word...")
        detector = snowboydecoder.HotwordDetector(self.wake_word_model, sensitivity=0.5)
        detector.start(detected_callback=wake_word_detected, sleep_time=0.5)

# ===== Example Usage =====
if __name__ == "__main__":
    alexa = AlexaDevice()
    user = User()
    alexa.add_observer(user)

    # Run wake word detection in a separate thread
    wake_thread = Thread(target=alexa.start_wake_word_detection)
    wake_thread.start()
