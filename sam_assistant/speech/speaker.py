import pyttsx3
import datetime

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        # You can adjust the properties here
        # self.engine.setProperty('rate', 150)
        # self.engine.setProperty('volume', 1.0)
        # Set to female or male voice
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)  # Often female voice in Windows

    def speak(self, text):
        """Speaks the given text out loud."""
        print(f"Sam Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self, user_name="Sameer"):
        """Greets the user based on the current time."""
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            greeting = f"Good Morning {user_name}!"
        elif hour >= 12 and hour < 17:
            greeting = f"Good Afternoon {user_name}!"
        else:
            greeting = f"Good Evening {user_name}!"
        
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        
        # We can add battery check here later, for now we will stick to basic greeting
        full_greeting = f"{greeting} Current time is {current_time}."
        self.speak(full_greeting)

# For standalone testing
if __name__ == "__main__":
    speaker = Speaker()
    speaker.greet_user()
