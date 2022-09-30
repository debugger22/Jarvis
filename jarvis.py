import aiml
import sys
import traceback

from src import google_tts
from src import google_stt
from src import microphone
from src import commonsense
from src import brain
from excp.exception import NotUnderstoodException

exit_flag = 0
tts_engine = google_tts.Google_TTS()
jarvis_brain = brain.Brain()
mic = microphone.Microphone()
k = aiml.Kernel()

MASTER = "Sir"


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S" )
    speak(Time)


def date():
    year = int(datetime.datetime.now().year )
    month = int(datetime.datetime.now().month )
    date = int(datetime.datetime.now().day )
    speak(date)
    speak(month)
    speak(year)


def wishMe():
    speak("Welcome back sir")
    # speak("The current time is")
    # time()
    # speak("The current date is")
    # date()
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning " + MASTER)


    elif hour>=12 and hour<18:
        speak("Good Afternoon " + MASTER)


    else:
        speak("Good Evening " + MASTER)
    speak("I am JARVIS. Please tell me sir how may I help you?")

def check_sleep(words):
    if 'sleep' in words or 'hibernate' in words:
        commonsense.sleepy()
        sleep()
    if ('shut' in words and 'down' in words) or 'bye' in words or 'goodbye' in words:
        tts_engine.say("I am shutting down")
        exit_flag = 1
        return True


def sleep():
    while not exit_flag:
        try:
            #mic = microphone.Microphone()
            a, s_data = mic.listen()
            stt_engine = google_stt.Google_STT(mic)
            stt_response = stt_engine.get_text()
            words_stt_response = stt_response.split(' ')
            if 'wake' in words_stt_response or 'jarvis' in words_stt_response or 'wakeup' in words_stt_response:
                tts_engine.say("Hello Sir, I am back once again.")
                wakeup()
        except Exception:
            pass


def wakeup():
    while not exit_flag:
        #mic = microphone.Microphone()
        a, s_data = mic.listen()
        a = 0
        if mic.is_silent(s_data):
            commonsense.sleepy()
            sleep()
        try:
            stt_engine = google_stt.Google_STT(mic)
            stt_response = stt_engine.get_text()
            print("Heard: %r" % stt_response)
            if(jarvis_brain.process(stt_response)):
                pass
            else:
                if check_sleep(stt_response.split(' ')):
                    break
                response = k.respond(stt_response)
                print(response)
                tts_engine.say(response)
        except NotUnderstoodException:
            commonsense.sorry()
        except Exception:
            print("Error in processing loop:")
            traceback.print_exc()
            commonsense.uhoh()

k.loadBrain('data/jarvis.brn')
try:
    f = open('data/jarvis.cred')
except IOError:
    sys.exit(1)

bot_predicates = f.readlines()
f.close()
for bot_predicate in bot_predicates:
    key_value = bot_predicate.split('::')
    if len(key_value) == 2:
        k.setBotPredicate(key_value[0], key_value[1].rstrip('\n'))
wakeup()
