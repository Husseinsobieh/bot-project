Automated Notepad Data Entry Bot

This project is a Python-based RPA (Robotic Process Automation) tool that fetches data from a REST API and automates the Windows Desktop UI to write that data into native Notepad files. It handles window management, typing simulation, and file saving logic automatically.

📺 Demo Video

[Watch the demo](https://drive.google.com/file/d/1Pvng3bhII3kQYMsLkH4K7_3UJqs4Kr-w/view?usp=sharing)

🚀 Features

API Integration: Fetches dummy post data from jsonplaceholder.typicode.com.

Smart Icon Detection: Scans the desktop for the Notepad icon using multiple size templates (Small, Medium, Large).

Auto-Cleanup: Detects and closes existing Notepad windows to ensure a clean work environment.

Human-like Typing: Simulates keystrokes to write content into the application.

Robust Saving: Handles "Save As" dialogs, file naming, and overwrite confirmation popups.

Fail-Safe: Includes pyautogui.FAILSAFE to abort the script by moving the mouse to the corner of the screen.

🛠️ Prerequisites

Before running this script, ensure you have the following:

Operating System: Windows 10 or 11.
Python: Version 3.x installed.
Package Manager: uv installed.
Notepad: The classic Windows Notepad application shortcut must be visible on the Desktop.

📦 Installation

Clone the repository (or download the files):

```
git clone https://github.com/Husseinsobieh/bot-project.git
cd bot-project
```

Install required dependencies:

```
uv sync
```

Note: opencv-python and pillow are required for PyAutoGUI's image recognition features.

Prepare Image Assets:
For the bot to "see," you must take screenshots of specific elements on your own screen and save them in the project folder with the exact names below:

notepad_icon_small.png

notepad_icon_medium.png

notepad_icon_large.png

opened_notepad_icon.png (The icon in the notepad when open)

overwrite_popup.png (The "Confirm Save As" dialog box)

📸 Visual Scenarios
Scenario 1: Small desktop icons
[Small](./small_icon_screenshot.png)
Scenario 2: Medium desktop icons
[Medium](./medium_icon_screenshot.png)

Scenario 3: Large desktop icons
[Large](./large_icon_screenshot.png)

▶️ Usage

Open your terminal or command prompt.

Navigate to the project directory.

Run the script:

```
uv run main.py
```

Hands off! Do not use the mouse or keyboard while the bot is running.

To stop the bot immediately, slam your mouse cursor into the top-left corner of the screen (Fail-safe).

📂 Output

The bot creates a folder on your Desktop named tjm-project.
Inside, you will find text files formatted as:

post_1.txt

post_2.txt

...

post_10.txt

⚠️ Troubleshooting

ImageNotFoundException: If the bot acts stuck, your screen resolution or icon scaling might differ from the screenshots provided. Retake the screenshots (.png) on your specific monitor.

Notepad Update: If you are using the new Windows 11 Tabbed Notepad, ensure the visual assets match the new UI.

Permissions: You may need to run your terminal as Administrator if the bot struggles to control the mouse.

