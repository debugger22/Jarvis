import aiml
import sys
from src import google_tts
from src import google_stt
from src import microphone
from src import commonsense
from src import brain

exit_flag = 0
tts_engine = google_tts.Google_TTS()
jarvis_brain = brain.Brain()
mic = microphone.Microphone()
k = aiml.Kernel()

def check_sleep(words):
	if 'sleep' in words or 'hibernate' in words:
		commonsense.sleepy()
		sleep()
	if ('shut' in words and 'down' in words) or 'bye' in words or 'goodbye' in words:
		tts_engine.say("I am shutting down")
		exit_flag = 1
		return True

def sleep():
	while True:
		try:
			mic = microphone.Microphone()
			a, s_data = mic.listen()
			stt_engine = google_stt.Google_STT(mic)
			stt_response = stt_engine.get_text()
			words_stt_response = stt_response.split(' ')
			if 'wake' in words_stt_response or 'jarvis' in words_stt_response or 'wakeup' in words_stt_response:
				tts_engine.say("Hello Sir, I am back once again.")
				wakeup()
		except:
			pass

def wakeup():
	while True:
		mic = microphone.Microphone()
		a, s_data = mic.listen()
		a=0
		if mic.is_silent(s_data):
			commonsense.sleepy()
			sleep()
		try:
			stt_engine = google_stt.Google_STT(mic)
			stt_response = stt_engine.get_text()
			if(jarvis_brain.process(stt_response)):
				pass
			else:
				if check_sleep(stt_response.split(' ')):
					break
				response = k.respond(stt_response)
				print(response)
				tts_engine.say(response)
		except:
			commonsense.sorry()

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
