# Python Calendar Application

This Python calendar application allows users to manage events and set reminders for specific dates. I made it cooler by letting you add custom sounds for reminders. 

## Features

- Display a calendar for the current month.
- Add, edit, and delete events.
- Set reminders for events.
- Play sound alerts for reminders.

## Requirements

- Python 3.x
- Tkinter (should be included with Python)
- winsound (Windows only, for sound alerts)

## Installation and Usage

1. Clone or download the repository to your local machine.

2. Install Python if you haven't already. You can download it from [python.org](https://www.python.org/).

3. Run the following command to install the required dependencies:
    ```
    pip install tk
    ```

4. Run the application using the following command:
    ```
    python calendar.py
    ```

5. Use the calendar interface to add, edit, or delete events. You can also set reminders for events.

## File Structure

- `calendar.py`: The main Python script containing the calendar application.
- `events.json`: JSON file for storing event data.

## Sound Alerts

- You can customize the reminder sound by replacing the `reminder.wav` file with your preferred sound file. Make sure the file is in WAV format.

## Notes

- This application uses Tkinter for the graphical user interface and is primarily designed for use on Windows platforms.
- For sound alerts, the `winsound` module is used, which is available on Windows platforms. If you are using a different platform, you may need to use a different approach for playing sounds.

