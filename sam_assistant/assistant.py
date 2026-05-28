from speech.speaker import Speaker
from speech.listener import Listener
from commands.processor import CommandProcessor
from ai.chatbot import AIChatbot
import threading
import time

class SamAssistant:
    def __init__(self):
        self.speaker = Speaker()
        self.listener = Listener()
        self.ai = AIChatbot()
        self.processor = CommandProcessor(ai_chatbot=self.ai)

    def startup(self):
        """Called when the assistant starts up."""
        self.speaker.greet_user()
        
    def listen_for_command(self):
        """Listens for a voice command and returns the transcribed text."""
        return self.listener.listen(timeout=5, phrase_time_limit=10)

    def process_command(self, text):
        """Processes the text command and speaks the response."""
        response = self.processor.process(text)
        self.speaker.speak(response)
        return response

    def run_continuously(self):
        """Continuous background loop waiting for commands."""
        import winsound
        print("Sam Assistant is now listening continuously for any command containing 'sam'...")
        while True:
            full_text = self.listener.listen_continuously_for_command("sam")
            if full_text:
                # Strip the wake word out of the command
                command = full_text.replace("hey sam", "").replace("sam", "").strip()
                
                if command:
                    # Single-shot command (e.g. "Sam open Spotify")
                    self.process_command(command)
                else:
                    # Just said "Sam" - play a chime and wait for command!
                    print("Wake word detected! Playing chime...")
                    winsound.Beep(1000, 200) # Ding!
                    
                    follow_up = self.listener.listen(timeout=5, phrase_time_limit=10)
                    if follow_up:
                        self.process_command(follow_up)
                    else:
                        print("No follow-up command detected.")
