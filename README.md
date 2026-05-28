# Sam Assistant 🎙️

A fully voice-controlled, continuous background AI desktop assistant with full laptop automation capabilities. 
It's designed to act and feel like a modern smart speaker (Google Assistant, Alexa, Gemini Live).

**Developed by**: [SAMEER NADAF](https://github.com/Sameergudusabnadaf)

---

## 🌟 Features

- **Continuous Background Listening**: Runs silently in the background without needing a graphical interface.
- **Natural Neural Voice**: Powered by Google TTS (`gTTS`) to give Sam a high-quality, human-like voice instead of a robotic one.
- **Smart Audio Chimes**: Just say "Sam" and the system will play a "Ding" chime, giving you instant feedback that it is listening to your follow-up command!
- **Conversational Memory**: The AI remembers your chat history! You can ask follow-up questions without repeating context.
- **Single-Shot Commands**: No need for awkward pauses. Just speak naturally (e.g., _"Sam, open Spotify"_).
- **Full Application Access**: Uses Windows Search automation (`pyautogui`) to open **any** application installed on your system.
- **System Controls**: Control your laptop's volume, mute, restart, and shutdown states via voice.
- **AI Integration**: Powered by NVIDIA NIM's **Llama-3.1-70B** for incredibly intelligent, fast, and conversational responses.
- **Time-Aware Greetings**: Greets you appropriately based on the time of day when started.

---

## 🛠️ How to Use

### 1. Installation

Ensure you have Python installed, then set up your environment:

```powershell
cd sam_assistant
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file in the `sam_assistant` directory and add your NVIDIA API Key:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
```

### 3. Running the Assistant

Run the main script. The assistant will start up, greet you, and listen silently in the background.

```powershell
.\venv\Scripts\activate
python main.py
```

---

## 🗣️ Voice Commands

You can interact with Sam in two ways:
1. **Single-Shot:** Say _"Sam, open Calculator"_.
2. **Interactive:** Say _"Sam"_, wait for the **Ding!** chime, and then say _"What is the weather?"_.

Here are some things you can say:

### Open Applications

- _"Sam, open Calculator"_
- _"Sam, open Google Chrome"_
- _"Sam, open VS Code"_
- _"Sam, open Git"_

### System Controls

- _"Sam, increase volume"_
- _"Sam, decrease volume"_
- _"Sam, mute"_
- _"Sam, shutdown laptop"_
- _"Sam, restart laptop"_

### Web & Searching

- _"Sam, search Google for Python tutorials"_
- _"Sam, play LoFi HipHop on YouTube"_
- _"Sam, open github.com"_

### AI Chatbot (Context-Aware)

- Ask it any general question!
- _"Sam, who is the CEO of Tesla?"_
- _"Sam, how old is he?"_ (Sam remembers you are talking about the CEO!)

---

> Built with Python, SpeechRecognition, PyAutoGUI, gTTS, Pygame, and NVIDIA NIM APIs.
