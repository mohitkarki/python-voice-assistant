import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Sorry, I didn’t understand that command.")

if __name__ == "__main__":
    speak("Initializing den den...")

    while True:
        r = recognizer
        print("Waiting for wake word...")

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)
                print("Listening den den'...")
                audio = r.listen(source, timeout=10, phrase_time_limit=5)

            word = r.recognize_google(audio)
            print(f"You said (raw): {repr(word)}")
            # print("You said:", word)

            if "den den" in word.lower():
                print("Wake word detected!")
                speak("Yes?")
                engine.stop()  # Ensure speech is flushed
                import time
                time.sleep(1)  # Wait 1 second before listening again
                
                with sr.Microphone() as source:
                    print("den den active... listening for command...")
                    r.adjust_for_ambient_noise(source, duration=0.3)
                    audio = r.listen(source, timeout=10, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out...")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except Exception as e:
            print("Error:", e)
