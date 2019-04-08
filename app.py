import pyttsx3
import time
import socket
engine = pyttsx3.init()

def speak(text:str,t:int = 0):
    engine.say(text)
    engine.runAndWait()
    time.sleep(t)

def internet(host="1.1.1.1", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(ex)
        return False

def main():
    while True:
        if not internet():
            speak("Internet is not working",1)
        else:
            print("Internet is Working")


if __name__ == "__main__":
    main()