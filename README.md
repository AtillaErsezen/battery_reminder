# battery_reminder
My personal python script that reminds me of the remaining battery just before shutting down the computer. Useful for lectures, helps determine when do I need to charge my laptop so I don't end up with a dead battery during lectures. It uses keyboard library to listen for alt_f4 keys (simple approach, because by habit, I always shut down computer with this combination and nothing else.) It uses psutil to gather the battery information. And it uses tkinter to show the percentage on a window. Since it listens for alt_f4 keys, if we use these combination in somewhere else, ex. when shutting down another application, the window appears, but this isn't considered to be an issue as it can be easily ignored.

# Battery Percentage Script

A simple Python script that shows the battery percentage when a specific hotkey is pressed. This guide explains how to set up the script and run it automatically when your computer starts.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Ensure Python is installed**:
   Check if Python is installed on your computer by running:
   ```bash
   python --version
   ```
   If not, download and install it from [python.org](https://www.python.org/downloads/).

3. **Install required packages**:
   Install the necessary Python packages by running:
   ```bash
   pip install psutil keyboard
   ```

## Setup for Automatic Execution

### Method 1: Using the Startup Folder

1. Verify that `run_battery_status.bat` references the correct path:
   ```bat
   pythonw "C:\path\to\your\repository\battery_percentage.py"
   ```
   Replace `C:\path\to\your\repository` with the actual path to the cloned repository.

2. **Add the .bat file to the Startup folder**:
   - Press `Win + R`, type `shell:startup`, and press Enter.
   - Copy `run_battery_status.bat` into this folder.

### Method 2: Using Task Scheduler (Alternative)

1. **Open Task Scheduler**:
   Search for "Task Scheduler" in the Windows Start menu and open it.

2. **Create a Basic Task**:
   - Click on "Create Basic Task" and name it (e.g., "Run Battery Percentage Script").
   - Set the trigger to "When I log on".
   - Choose "Start a Program" as the action.
   - Browse and select `pythonw.exe` (e.g., `C:\PythonXX\pythonw.exe`).
   - Add the path to `battery_percentage.py` in the "Add arguments" field.

3. **Complete and save** the task.

## Usage

- The script runs in the background and shows the battery percentage when the configured hotkey (`Alt + F4`) is pressed.

- To stop the script, press the `Esc` key.
