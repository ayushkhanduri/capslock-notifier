from pynput.keyboard import Key, Listener
from plyer import notification

is_caps_on = False

def on_press(key):
    print(key)

def on_release(key):
    global is_caps_on
    message =""
    title="Caps Lock"
    if key == Key.caps_lock:
        is_caps_on = not is_caps_on
        if is_caps_on:
            message = "Turned on"
        else:
            message = "Turned off"
        notification.notify(title = title, message = message, timeout=1, toast=True)



with Listener(on_press=on_press, on_release=on_release) as listeners:
    listeners.join()
