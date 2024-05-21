import time
from threading import Thread
from pynput import keyboard

from mp3 import MP3

# Time in seconds before the alert is shown
INACTIVITY_THRESHOLD = 60

# Variable to keep track of the last key press time
last_keypress_time = time.time()
alert_active = False

alert = MP3("alert.mp3")


def on_press(key):
    global last_keypress_time
    global alert_active
    global alert

    if alert_active:
        alert.stop()

    last_keypress_time = time.time()


def monitor_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def sound_alert():
    print("sounding alert")
    # Play alert sound
    alert.play()


def check_inactivity():
    global last_keypress_time
    global alert_active
    while True:
        current_time = time.time()
        if current_time - last_keypress_time > INACTIVITY_THRESHOLD:
            sound_alert()
            alert_active = True
            last_keypress_time = current_time
        time.sleep(1)


if __name__ == "__main__":
    keyboard_thread = Thread(target=monitor_keyboard)
    keyboard_thread.daemon = True
    keyboard_thread.start()

    check_inactivity()
