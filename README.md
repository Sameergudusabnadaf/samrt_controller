# Sam Assistant 🎙️

A fully voice-controlled, continuous background AI desktop assistant with full laptop automation capabilities.

**Developed by**: [SAMEER NADAF](https://github.com/Sameergudusabnadaf)

---

## 🌟 Features

- **Continuous Background Listening**: Runs silently in the background without needing a graphical interface.
- **Single-Shot Commands**: No need for awkward pauses. Just speak naturally (e.g., _"Sam, open Spotify"_).
- **Full Application Access**: Uses Windows Search automation (`pyautogui`) to open **any** application installed on your system.
- **System Controls**: Control your laptop's volume, mute, restart, and shutdown states via voice.
- **AI Integration**: Powered by NVIDIA NIM (Llama 3.1) for intelligent, conversational responses.
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

Create a `.env` file in the `sam_assistant` directory and add your API Key:

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

Just ensure the word **"Sam"** is in your sentence. Here are some things you can say:

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

### AI Chatbot

- Ask it any general question!
- _"Sam, what is the distance to the moon?"_

---

> Built with Python, SpeechRecognition, PyAutoGUI, and NVIDIA NIM APIs.
