import tkinter as tk
from tkinter import messagebox
import calendar
import json
from datetime import datetime
import winsound

class CalendarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calendar")
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.events = {}
        self.reminder_sound = "reminder.wav"  # Path to your reminder sound file
        
        self.create_widgets()
        self.load_events()
        self.show_calendar()

    def create_widgets(self):
        # Calendar display
        self.calendar_label = tk.Label(self, text="", font=("Courier", 12), justify="left")
        self.calendar_label.pack()

        # Event entry fields
        self.event_entry = tk.Entry(self)
        self.event_entry.pack()

        # Add event button
        self.add_button = tk.Button(self, text="Add Event", command=self.add_event)
        self.add_button.pack()

        # Delete event button
        self.delete_button = tk.Button(self, text="Delete Event", command=self.delete_event)
        self.delete_button.pack()

    def show_calendar(self):
        cal = calendar.monthcalendar(self.current_year, self.current_month)
        cal_str = calendar.month_name[self.current_month] + ' ' + str(self.current_year) + '\n\n'
        
        for week in cal:
            for day in week:
                if day == 0:
                    cal_str += '   '
                else:
                    cal_str += '{:2d} '.format(day)
                    if (self.current_year, self.current_month, day) in self.events:
                        cal_str += '* '  # Display asterisk for days with events
            cal_str += '\n'
        
        self.calendar_label.config(text=cal_str)

    def add_event(self):
        event_text = self.event_entry.get().strip()
        if event_text:
            event_date = (self.current_year, self.current_month, self.calendar_label.selection_get().day)
            if event_date in self.events:
                messagebox.showerror("Error", "An event already exists for this date.")
            else:
                self.events[event_date] = event_text
                self.save_events()
                self.show_calendar()
        else:
            messagebox.showerror("Error", "Please enter an event description.")

    def delete_event(self):
        event_date = (self.current_year, self.current_month, self.calendar_label.selection_get().day)
        if event_date in self.events:
            del self.events[event_date]
            self.save_events()
            self.show_calendar()
        else:
            messagebox.showerror("Error", "No event found for this date.")

    def save_events(self):
        with open("events.json", "w") as f:
            json.dump(self.events, f)

    def load_events(self):
        try:
            with open("events.json", "r") as f:
                self.events = json.load(f)
        except FileNotFoundError:
            pass  # No events file yet

    def check_reminders(self):
        today = datetime.now().date()
        for event_date, event_text in self.events.items():
            if datetime(*event_date).date() == today:
                winsound.PlaySound(self.reminder_sound, winsound.SND_FILENAME)
                messagebox.showinfo("Reminder", f"Today's event: {event_text}")

if __name__ == "__main__":
    app = CalendarApp()
    app.after(1000, app.check_reminders)  # Check reminders every second
    app.mainloop()
