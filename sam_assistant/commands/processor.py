from automation import (
    shutdown_system, restart_system, volume_up, volume_down, volume_mute,
    open_website, search_google, play_youtube,
    open_application, close_application, close_tab, open_folder
)

class CommandProcessor:
    def __init__(self, ai_chatbot=None):
        self.ai_chatbot = ai_chatbot

    def process(self, text):
        """
        Parses the text and triggers automation or falls back to AI.
        """
        text = text.lower().strip()
        
        # System Commands
        if "shutdown" in text and "laptop" in text:
            return shutdown_system()
        elif "restart" in text and "laptop" in text:
            return restart_system()
        elif "increase volume" in text or "volume up" in text:
            return volume_up()
        elif "decrease volume" in text or "volume down" in text:
            return volume_down()
        elif "mute" in text:
            return volume_mute()
            
        # Application / Files
        elif text.startswith("open folder"):
            folder = text.replace("open folder", "").strip()
            return open_folder(folder)
        elif text.startswith("open"):
            app_or_website = text.replace("open", "").strip()
            if "." in app_or_website:
                return open_website(app_or_website)
            else:
                return open_application(app_or_website)
        elif text.startswith("close") or "close app" in text or "close window" in text:
            if "tab" in text:
                return close_tab()
            else:
                return close_application()
                
        # Browser Automation
        elif text.startswith("search google for"):
            query = text.replace("search google for", "").strip()
            return search_google(query)
        elif text.startswith("search for"):
            query = text.replace("search for", "").strip()
            return search_google(query)
        elif "play" in text and "on youtube" in text:
            query = text.replace("play", "").replace("on youtube", "").strip()
            return play_youtube(query)
        elif text.startswith("play"):
            query = text.replace("play", "").strip()
            return play_youtube(query)
            
        # Fallback to AI Chatbot
        else:
            if self.ai_chatbot:
                return self.ai_chatbot.get_response(text)
            else:
                return "I'm not sure how to do that yet, and my AI is not connected."
