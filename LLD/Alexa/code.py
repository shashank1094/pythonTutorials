import speech_recognition as sr
import pyttsx3
import random
from abc import ABC, abstractmethod

# ===== Factory Pattern for Service Handlers =====
class CommandHandlerFactory:
    @staticmethod
    def get_handler(command):
        if "weather" in command:
            return WeatherHandler()
        elif "music" in command:
            return MusicHandler()
        elif "alarm" in command:
            return AlarmHandler()
        else:
            return UnknownCommandHandler()

# ===== Abstract Base Class for Command Handlers =====
class CommandHandler(ABC):
    @abstractmethod
    def execute(self, command):
        pass

# ===== Concrete Implementations for Different Commands =====
class WeatherHandler(CommandHandler):
    def execute(self, command):
        return "The weather is sunny with 25°C temperature."

class MusicHandler(CommandHandler):
    def execute(self, command):
        return f"Playing {random.choice(['song1', 'song2', 'song3'])}."

class AlarmHandler(CommandHandler):
    def execute(self, command):
        return "Alarm set for 7:00 AM."

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

# ===== Alexa Device Class =====
class AlexaDevice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Service unavailable."

    def process_command(self, command):
        handler = CommandHandlerFactory.get_handler(command)
        response = handler.execute(command)
        self.speak(response)
        self.notify_observers(response)

    def speak(self, message):
        print(f"Alexa: {message}")
        self.speaker.say(message)
        self.speaker.runAndWait()

# ===== Example Usage =====
if __name__ == "__main__":
    alexa = AlexaDevice()
    user = User()
    alexa.add_observer(user)

    command = alexa.listen()
    alexa.process_command(command)
