import datetime
import os
import pygame
from gtts import gTTS

class Speaker:
    def __init__(self):
        # Initialize the pygame mixer for playing MP3s
        pygame.mixer.init()

    def speak(self, text):
        """Speaks the given text out loud using Google TTS."""
        print(f"Sam Assistant: {text}")
        if not text.strip():
            return
            
        try:
            # Generate speech
            tts = gTTS(text=text, lang='en', tld='com') 
            filename = "temp_response.mp3"
            tts.save(filename)
            
            # Play the audio
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            
            # Wait until it finishes playing
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            # Unload the file so we can delete it
            pygame.mixer.music.unload()
            
            # Clean up temporary file
            if os.path.exists(filename):
                os.remove(filename)
                
        except Exception as e:
            print(f"TTS Error: {e}")

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
