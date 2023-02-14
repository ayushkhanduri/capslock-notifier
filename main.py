from pynput.keyboard import Key, KeyCode, Listener
from plyer import notification

is_caps_on = False

def on_press(key):
    print(key)

def on_release(key: KeyCode):
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
    # this was a fallcheck in case the caps_lock state was wrong to notify user
    # turns out you can't capture capital keys in plyer
    # else:
    #     try:
    #         ascii_value = ord(key.char or "")
    #         print(ascii_value)
    #         if 65 <= ascii_value <= 90 and not is_caps_on:
    #             is_caps_on = True
    #             message = "Caps lock is actually on"
    #         elif  97 <= ascii_value <= 122 and is_caps_on:
    #             is_caps_on = False
    #             message = "Caps lock is actually off"
    #         if message:
    #             notification.notify(title = title, message = message, timeout=1, toast=True)
    #     except:
    #         print("Some exception occured")

with Listener(on_press=on_press, on_release=on_release) as listeners:
    listeners.join
