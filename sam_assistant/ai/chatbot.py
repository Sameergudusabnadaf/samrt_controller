import os
from openai import OpenAI
from dotenv import load_dotenv

class AIChatbot:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.history = []
        if self.api_key:
            self.client = OpenAI(
                base_url="https://integrate.api.nvidia.com/v1",
                api_key=self.api_key
            )
            # You can choose a different model if you prefer
            self.model = "meta/llama-3.1-70b-instruct" 
            self.is_ready = True
            
            # Initialize history with system prompt
            self.system_prompt = "You are Sam Assistant, a helpful, concise AI desktop assistant for Sameer. Answer briefly and directly without fluff."
            self.history.append({"role": "system", "content": self.system_prompt})
            
            print("AI Chatbot initialized with NVIDIA NIM.")
        else:
            self.is_ready = False
            print("Warning: NVIDIA_API_KEY not found in .env file. AI will not respond.")

    def get_response(self, prompt):
        if not self.is_ready:
            return "My AI is not configured. Please set the NVIDIA_API_KEY in the .env file."
        
        try:
            # Append user message
            self.history.append({"role": "user", "content": prompt})
            
            # Keep history from growing indefinitely (e.g. keep system prompt + last 10 messages)
            if len(self.history) > 11:
                self.history = [self.history[0]] + self.history[-10:]
            
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
            )
            
            response_text = completion.choices[0].message.content.strip()
            
            # Append assistant response
            self.history.append({"role": "assistant", "content": response_text})
            
            return response_text
            
        except Exception as e:
            print(f"Error generating AI response: {e}")
            return "I encountered an error while thinking about that."

# For testing
if __name__ == "__main__":
    bot = AIChatbot()
    print(bot.get_response("Hello, who are you?"))
