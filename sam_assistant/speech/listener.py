import speech_recognition as sr

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def listen(self, timeout=None, phrase_time_limit=None):
        """
        Listens to the microphone and converts speech to text.
        Returns the recognized text or None if error/timeout.
        """
        try:
            with sr.Microphone() as source:
                print("Sam Assistant: Listening...")
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Listen for audio input
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                print("Sam Assistant: Recognizing...")
                
                # Using Google Speech Recognition (free, requires internet)
                text = self.recognizer.recognize_google(audio)
                print(f"User said: {text}")
                return text.lower()
                
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None
        except sr.UnknownValueError:
            print("Sam Assistant could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            print(f"Microphone error: {e}")
            return None

    def listen_continuously_for_command(self, wake_word="sam"):
        """Continuously listens and returns the full sentence if the wake word is in it."""
        print(f"Waiting for wake word: '{wake_word}' in a sentence...")
        while True:
            try:
                with sr.Microphone() as source:
                    # Shorter ambient noise adjustment for faster loops
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
                    # We allow a longer phrase time limit so they can finish their sentence
                    audio = self.recognizer.listen(source, phrase_time_limit=10)
                    
                    try:
                        text = self.recognizer.recognize_google(audio).lower()
                        if wake_word in text:
                            print(f"Detected command: '{text}'")
                            return text
                    except sr.UnknownValueError:
                        pass # Ignore ambient noise
            except Exception as e:
                print(f"Error in background listening: {e}")
                import time
                time.sleep(2)

# For standalone testing
if __name__ == "__main__":
    listener = Listener()
    result = listener.listen(timeout=5, phrase_time_limit=10)
    print("Test Result:", result)
