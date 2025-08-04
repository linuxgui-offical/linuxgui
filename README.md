LinuxGUI - Linux App & System Manager
LinuxGUI is a Python Tkinter-based desktop app to help you easily manage your Linux apps and system with a sleek, user-friendly interface. It includes tools to uninstall Linux and Wine apps, run common system commands, and create custom command buttons — all without needing to open the terminal!

Features
Linux Apps Tab

Search and browse installed Linux desktop apps.

Uninstall apps via apt or flatpak automatically.

Delete app desktop entries or app files manually.

Wine Apps Tab

Launch Wine’s built-in Windows program uninstaller GUI.

Commands Tab

Run quick system commands like update, upgrade, system info, network tests, and more.

Add and manage your own custom command buttons.

View command output in a scrollable window.

Live System Info

Displays CPU, RAM, disk usage, network stats, uptime, and CPU temperature.

Clean, readable terminal-like dark theme with glow effects.

Requirements
Python 3.6+

Tkinter (usually included with Python)

psutil (pip install psutil)

sudo privileges for uninstalling packages and running system commands.

Wine installed if you want to manage Windows apps.

Installation & Running
Clone or download this repository.

Install dependencies:

bash
Copy
Edit
pip install psutil
Run the app:

bash
Copy
Edit
python3 linuxgui.py
Usage
Linux Apps Tab: Search apps by name, select one, and click "Uninstall Selected" to choose how to remove it.

Wine Apps Tab: Click the button to open Wine’s Add/Remove Programs window.

Commands Tab: Click buttons to run commands. Add your own custom commands with the button at the bottom.

You can view live system resource stats in the interface.

Notes
The app attempts to detect package managers (apt, flatpak) for uninstalling apps but may require manual deletion for some apps.

Running system commands and uninstall operations may require your user password for sudo access.

Commands run in a safe, confirmed manner with visible output and progress.

Contributing
Feel free to open issues or pull requests! Suggestions for more commands, package managers, or UI improvements are welcome.

License
This project is licensed under the MIT License.
