import re
import webbrowser
import os
import random
import urllib
import thread
import yaml

from src import google_tts
from src.wikipedia import wikipedia
from src import network
from src.some_functions import *

speak_engine = google_tts.Google_TTS()

with open('config.yml', 'r') as f:
    config = yaml.load(f)



class Brain():

    '''
    This class will load core things in Jarvis' brain
    '''

    def process(self, text):
        words = text.lower().split(' ')
        if 'open' in words:
            speak_engine.say("I'm on it. Stand By.")
            websites = config["config"]["websites"]
            website_to_open = text[text.index('open') + 5:]
            if website_to_open in websites:
                url = websites[website_to_open]
                webbrowser.open_new_tab(url)
        if 'search' in words:
            speak_engine.say("I'm looking for it. Please stand by!")
            term_to_search = text[text.index('search') + 7:]
            summary = wikipedia.summary(term_to_search)
            summary = " ".join(re.findall('\w+.', summary))
            summary = summary[:99]
            speak_engine.say(summary)
            return True
        if 'where' in words and ('are' in words or 'am' in words) and ('we' in words or 'i' in words) or 'location' in words:
            speak_engine.say("I am tracking the location. Stand by.")
            speak_engine.say(network.currentLocation())
            return True
        if 'play' in words:
            if 'a' in words and 'song' in words:
                thread.start_new_thread(play_music, ())
            return True

        '''Handling Mathematical/Computational queries'''
        if 'add' in words or 'subtract' in words or 'multiply' in words or 'divide' in words:
            try:
                nums = re.findall('\d+', text)
                if len(nums) < 2:
                    mod_text = words_to_nums(text)
                    nums += re.findall('\d+', mod_text)
                    print nums
                nums = map(int, nums)
                if 'add' in words:
                    speak_engine.say("It is " + str(sum(nums)))
                if 'subtract' in words:
                    speak_engine.say("It is " + str(nums[1] - nums[0]))
                if 'multiply' in words:
                    speak_engine.say("It is " + str(nums[0] * nums[1]))
                if 'divide' in words:
                    speak_engine.say("It is " + str(nums[0] / nums[1]))
            except:
                speak_engine.say(
                    "Perhaps my Mathematical part of brain is malfunctioning.")
            return True
        return False
