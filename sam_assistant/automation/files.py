import os
import subprocess
import platform

def open_application(app_name):
    """
    Uses Windows Search to open ANY application genericly.
    """
    app_name = app_name.lower().strip()
    
    if platform.system() == "Windows":
        import pyautogui
        import time
        
        # Press the Windows key
        pyautogui.press('win')
        time.sleep(0.5)  # Wait for the Start menu to open
        
        # Type the application name
        pyautogui.write(app_name, interval=0.05)
        time.sleep(1)    # Wait for search results
        
        # Press Enter to open the top result
        pyautogui.press('enter')
        
        return f"Opening {app_name}."
    else:
        return "Generic application launching is only supported on Windows right now."

def close_application():
    """
    Closes the currently active window using Alt+F4.
    """
    if platform.system() == "Windows":
        import pyautogui
        pyautogui.hotkey('alt', 'f4')
        return "Closed the active window."
    else:
        return "Closing is only supported on Windows right now."

def close_tab():
    """
    Closes the current browser tab using Ctrl+W.
    """
    if platform.system() == "Windows":
        import pyautogui
        pyautogui.hotkey('ctrl', 'w')
        return "Closed the current tab."
    else:
        return "Closing tabs is only supported on Windows right now."

def open_folder(folder_name):
    """
    Opens common folders like Downloads, Documents, etc.
    """
    folder_name = folder_name.lower()
    user_home = os.path.expanduser("~")
    
    paths = {
        "downloads": os.path.join(user_home, "Downloads"),
        "documents": os.path.join(user_home, "Documents"),
        "desktop": os.path.join(user_home, "Desktop")
    }
    
    if folder_name in paths:
        path = paths[folder_name]
        if platform.system() == "Windows":
            os.startfile(path)
        else:
            subprocess.Popen(["xdg-open", path])
        return f"Opening {folder_name} folder."
    else:
        return f"Could not find a standard folder named {folder_name}."
