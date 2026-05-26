import os
import platform
import pyautogui

def shutdown_system():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux":
        os.system("shutdown now")
    return "Shutting down the system."

def restart_system():
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    elif platform.system() == "Linux":
        os.system("reboot")
    return "Restarting the system."

def volume_up():
    for _ in range(5):
        pyautogui.press("volumeup")
    return "Increased volume."

def volume_down():
    for _ in range(5):
        pyautogui.press("volumedown")
    return "Decreased volume."

def volume_mute():
    pyautogui.press("volumemute")
    return "Muted the volume."
