import keyboard
import psutil
from tkinter import messagebox, Tk

def show_battery_percentage():
    battery = psutil.sensors_battery()
    if battery:
        battery_percent = battery.percent
        messagebox.showinfo("Battery Status", f"Battery percentage: {battery_percent}%")
    else:
        messagebox.showinfo("Battery Status", "Unable to retrieve battery status.")

def on_alt_f4():
    root = Tk()
    root.withdraw()  # Hide the main window
    show_battery_percentage()
    root.destroy()

keyboard.add_hotkey('alt+f4', on_alt_f4)

# Keep the script running
keyboard.wait('esc')  # Press 'esc' to exit the script