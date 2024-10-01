from pynput import keyboard

# Example usage
def on_press(key):
    print(f"{key} pressed")

def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()