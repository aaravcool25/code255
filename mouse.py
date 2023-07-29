import time
import pyautogui
from pynput import keyboard

def on_press(key):
    global is_moving, delay_seconds
    try:
        if key.char == 'q':  # Check for the 'q' key
            if not is_moving:
                print("Enter the number of seconds for mouse movement:")
                try:
                    delay_seconds = float(input())
                    if delay_seconds <= 0:
                        raise ValueError
                except ValueError:
                    print("Invalid input. Please enter a valid positive number.")
                    return

                is_moving = True
                move_mouse()
                print("Mouse movement stopped.")
                is_moving = False
            else:
                is_moving = False
                print("Mouse movement stopped.")
    except AttributeError:
        pass

def move_mouse():
    mouse = pyautogui
    while is_moving:
        mouse.moveRel(300, 0, duration=delay_seconds / 2)  # Move right by 300 pixels
        if not is_moving:
            break  # Stop the movement if is_moving is set to False
        mouse.moveRel(-300, 0, duration=delay_seconds / 2)  # Move left by 300 pixels

if __name__ == "__main__":
    print("Press 'q' to start/stop moving the mouse.")
    is_moving = False
    delay_seconds = 1.0  # Default delay time in seconds

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
